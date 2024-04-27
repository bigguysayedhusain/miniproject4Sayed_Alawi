from django.views.generic import TemplateView
from django.db.models import Exists, OuterRef
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
