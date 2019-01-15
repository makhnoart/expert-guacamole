from django.conf.urls import url, include

from library import views

urlpatterns = [
    url(r'^library/', views.library, name='library'),

]

