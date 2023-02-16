from django.contrib import admin
from .models import Movie 

# Registered backend_api models 

class MovieAdmin(admin.ModelAdmin):
    list = ('name', 'genre', 'starring') 
    
    admin.site.register(Movie) 