from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse, reverse_lazy
from .models import Country, City, Post, Activity
from .forms import PostForm, ActivityForm, CityForm


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


class PostCreateView(LoginRequiredMixin, View):
    template_name = 'travelblog/post_create.html'

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the newly created post detail page
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):  # This has to be removed when it doesn't add the country automatically
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'travelblog/edit_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'travelblog/confirm_delete.html'
    success_url = reverse_lazy('myhome')  # Redirect to 'myhome' after a post is deleted

    def get_queryset(self):
        # Ensure that users can only delete their own posts
        return self.model.objects.filter(author=self.request.user)


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'travelblog/activity_form.html'
    success_url = reverse_lazy('myhome')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'travelblog/activity_form.html'
    success_url = reverse_lazy('myhome')


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = 'travelblog/activity_confirm_delete.html'
    success_url = reverse_lazy('myhome')


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'travelblog/city.html'
    success_url = reverse_lazy('myhome')  # Redirect to 'home' after successfully creating a city.

    def form_valid(self, form):
        # Add any additional logic here if necessary
        return super().form_valid(form)


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
