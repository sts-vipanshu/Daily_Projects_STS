from django.urls import path, include
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='upload/', view=views.uploadFile, name='uploadFile'),
    path(route='extract/', view=views.logicForRegexPattern, name='logicForRegexPattern'),
]