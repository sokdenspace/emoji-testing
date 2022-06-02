from django.urls import path
from . import views

urlpatterns = [
    path('', views.efeed, name='eFeed'),
    path('echat/', views.echat, name='eChat'),
    path('eread/', views.eread, name='eRead'),
    path('ewatch/', views.ewatch, name='eWatch'),
    path('emusic/', views.emusic, name='eMusic'),
]
