from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Country, City, Post, Activity


class HomeView(TemplateView):
    template_name = 'travelblog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # First get all cities that have posts or activities
        cities_with_content = City.objects.filter(
            Exists(Post.objects.filter(city=OuterRef('pk'))) |
            Exists(Activity.objects.filter(city=OuterRef('pk')))
        ).distinct()

        # Get countries that have these cities
        countries_with_content = Country.objects.filter(
            cities__in=cities_with_content
        ).distinct().order_by('name').prefetch_related(
            'cities__posts',
            'cities__activities'
        )

        country_city_data = []
        for country in countries_with_content:
            city_data = [{
                'name': city.name,
                'posts': list(city.posts.all()[:5]),
                'activities': list(city.activities.all()[:5])
            } for city in country.cities.filter(id__in=cities_with_content)]

            country_city_data.append({
                'name': country.name,
                'cities': city_data
            })

        context['countries'] = country_city_data
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'travelblog/post_detail.html'
    context_object_name = 'post'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'travelblog/activity_detail.html'
    context_object_name = 'activity'


class MyHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'travelblog/myhome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['posts'] = Post.objects.filter(author=user)
        context['activities'] = Activity.objects.filter(author=user)
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'travelblog/registration/register.html', {'form': form})
