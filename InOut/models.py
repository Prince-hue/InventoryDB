from django.db import models
import csv


# Create your models here.
class inout(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Populate asset_names from CSV
asset_names = []
with open('operatingCost.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        asset_names.append((row['DESCRIPTION'], row['DESCRIPTION']))


class Asset(models.Model):
    name_of_asset = models.CharField(max_length=255, choices=asset_names)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name_of_person = models.CharField(max_length=25, default='Unknown')

    def __str__(self):
        return self.name_of_asset