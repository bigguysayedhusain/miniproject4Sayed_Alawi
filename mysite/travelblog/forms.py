from django import forms
from .models import Post, Activity, City


class PostForm(forms.ModelForm):

    city = forms.ModelChoiceField(
        queryset=City.objects.select_related('country').order_by('country__name', 'name')
    )
    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'images', 'tags', 'location', 'city']

    def save(self, commit=True):  # This has to be removed when it doesn't add the country automatically
        instance = super().save(commit=False)
        if instance.city:  # Check if the city is set
            instance.country = instance.city.country

        if commit:
            instance.save()
            self.save_m2m()  # In case there are many-to-many fields on the form

        return instance


class ActivityForm(forms.ModelForm):

    city = forms.ModelChoiceField(
        queryset=City.objects.select_related('country').order_by('country__name', 'name')
    )
    class Meta:
        model = Activity
        fields = ['name', 'description', 'duration', 'cost', 'suitability', 'image', 'location', 'city']

    def save(self, commit=True):  # This has to be removed when it doesn't add the country automatically
        instance = super().save(commit=False)
        if instance.city:  # Check if the city is set
            instance.country = instance.city.country

        if commit:
            instance.save()
            self.save_m2m()  # In case there are many-to-many fields on the form

        return instance


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        country = cleaned_data.get('country')

        if City.objects.filter(name=name, country=country).exists():
            self.add_error('name', 'City with this name already exists in the selected country.')

        return cleaned_data

