from django.conf.urls import url
from simple_pages import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),

]
