how to connect multiple DBMS into Django project
------------------------------------------------------
#make sure driver is installed like pip install mysql
#visit django site for guidance
https://docs.djangoproject.com/en/5.0/topics/db/multi-db/
#we're going to be using database routers
#we create a database called auth_db
""""
DATABASES = {
    'default': {},
    'auth_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
""""
#since there is nothing in default, when you migrate it, you'll get an error
#we need to define our routers
#paste it into settings at the very end
DATABASE_ROUTERS = ["routers.db_routers.AuthRouter"]
#create a folder called "routers"
#create file inside it with name, "db_routers.py"
#copy the router class into the file, "db_routers"
""""
class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"auth", "contenttypes", "admin", "sessions"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "auth_db"
        return None
""""
#in the terminal, run migration
python manage.py migrate --database=auth_db

Getting Access to the backend
------------------------------------------------------
#type the following into the terminal (PS)
python manage.py createsuperuser --database=auth_db
#username : Admin
#Email address : admin@gmail.com
#password : "admin" then y for yes
#start server again
python manage.py runserver
#visit backend by adding "admin" to the URL
#use "DB Browser for SQlite" to visualize the data
#so everything we save as long as user is concern gets saved in SQlite3

How to add another database (MySQL)
---------------------------------------------------
#add it into the settings.py, DATABASES dictionary
""""
"workshopinv_db": {
        "NAME": "workshopinv",
        "ENGINE": "django.db.backends.mysql",
        "USER": "root",
        "PASSWORD": os.environ.get('MySQL_password'),
        "PORT": 3306
    },
""""

How to use Environment variables to hide passwords and secret data
---------------------------------------------------------------------
#lunch control panel
#go into system and security
#go into systems
#click on advance system settings
#go to environment variables
#under user variable, go to new
""""
password = 'root'
variable name = variable value
"""
#then okay then okay
#to access it
""""
import os

key = os.environ.get('variable name')
""""

Recording new database added
--------------------------------------------------
#in settings.py, modify this to 
DATABASE_ROUTERS = [
    "routers.db_routers.AuthRouter",
    "routers.db_routers.workshopinvRouter",
    ]
#go into routers and create a class called workshopinvRouter
#just copy the initial class and rename the class
""""
class workshopinvRouter:
    route_app_labels = {"InOut"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "workshopinv_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "workshopinv_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "workshopinv_db"
        return None

""""
#make migration to see if it worked
python manage.py makemigrations

Create a model in model.py
----------------------------------------------- 
""""
class inout(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
""""
#go into admin.py and register the model
from .models import inout
admin.site.register(inout)
#type the following into the terminal
python manage.py makemigrations
python manage.py migrate --database=workshopinv_db
python manage.py runserver 
#go into your Django Admin site to see the changes

Connecting database to webpage pt 1
--------------------------------------------
#in order for user to communicate with the DBMS,
#the model must be imported
#in views.py
from .models import inout
#define codes inside the tryy function
#inside the try.html, create a for loop to display the
#content of the dictionary
""""
{% for x in inout %}
{{x.name}} <br>
{% endfor %}
"""""

Connecting database to webpage pt 2
--------------------------------------------
#create a forms.py
""""
from django import forms
from .models import inout

class inoutforms(forms.ModelForm):
    class Meta:
        model = inout
        fields = '__all__'
        #fields = ['user', 'address']
""""
#in views.py
""""
from .models import inout
from .forms import inoutforms
from django.shortcuts import redirect


def tryy(request):
    in_out = inout.objects.all()
    if request.method == 'POST':
        form = inoutforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('InOut/index.html')
    else:
        form = inoutforms()
    dic = {
        'inout': in_out,
        'form': form,
    }
    return render(request, 'try.html', dic)
""""

Adding csv data to model
-------------------------------------------------- 
# models.py
""""
import csv
from django.db import models

class Asset(models.Model):
    asset_names = []  # Define an empty list to be populated dynamically

    # Read asset names from CSV and update the choices list
    with open('path/to/your/file.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            asset_names.append((row['asset_name'], row['asset_name']))

    name_of_asset = models.CharField(max_length=255, choices=asset_names)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_asset
""""

Adding auto complete 
---------------------------
#model.py
""""
import csv
from django.db import models
from dal import autocomplete

# Populate asset_names from CSV
asset_names = []
with open('operatingCost.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        asset_names.append((row['DESCRIPTION'], row['DESCRIPTION']))

class Asset(models.Model):
    name_of_asset = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_asset


class AssetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Asset.objects.none()

        if self.q:
            qs = Asset.objects.filter(name_of_asset__istartswith=self.q)

        return qs

""""
#urls.py
"""""
from django.urls import path
from .views import AssetAutocomplete

urlpatterns = [
    path('asset-autocomplete/', AssetAutocomplete.as_view(), name='asset-autocomplete'),
    # Add other URL patterns as needed
]
""""""
#forms.py
""""
from dal import autocomplete
from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name_of_asset', 'quantity']
        widgets = {
            'name_of_asset': autocomplete.ModelSelect2(url='asset-autocomplete')
        }

""""