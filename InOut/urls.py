from django.urls import path
from . import views
#from .views import AssetAutocomplete


#urls go here
urlpatterns = [
    path('index/', views.html_index),
    path('forms/', views.forms, name = 'forms'),
    path('getvalue/', views.html_forms_get, name = 'getforms'),
    path('try/', views.tryy, name = 'try'),
    #path('asset-autocomplete/', AssetAutocomplete.as_view(), name='asset-autocomplete'),
    path('asset/', views.assett, name = 'asset'),
    path('assetlist/', views.asset_list, name='asset_list'),
]