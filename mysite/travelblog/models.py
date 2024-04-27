from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    content = models.TextField()
    images = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    location = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='posts')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    suitability = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='activities')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activities_images/', blank=True, null=True)

    def __str__(self):
        return self.name
