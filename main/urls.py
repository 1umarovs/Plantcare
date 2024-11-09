from django.urls import path
from .views import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view() ,name = 'home'),
    path('plantsgramm', Plantsgramm.as_view() ,name = 'plantsgramm'),
    path('my_plants', My_plants.as_view() ,name = 'my_plants'),
    path('plants', Plantes.as_view() ,name = 'plants'),
    path('register', UserRegisterView.as_view(), name = 'register'),
    path('add_plants', Addplants.as_view() ,name = 'add_plants'),
    path('add_blog', Add_blog.as_view() ,name = 'add_blog'),
    path('result', views.result_page , name = 'result'),
    path('blogs', pgramm.as_view() , name = 'blogs'),
    path('test', Test.as_view() , name = 'test'),
    path('category',views.category, name = 'category')
]