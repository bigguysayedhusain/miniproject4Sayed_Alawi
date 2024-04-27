from django.core.management.base import BaseCommand
from travelblog.models import Country
import csv
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Load a list of countries from a CSV file into the database'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'travelblog/data/worldcountries.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                Country.objects.get_or_create(name=row[0])
            self.stdout.write(self.style.SUCCESS('Successfully imported countries'))
