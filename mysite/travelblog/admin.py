from django.contrib import admin

from .models import Country, City, Post, Activity

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Post)
admin.site.register(Activity)
