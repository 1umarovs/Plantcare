from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic
from django.urls import reverse_lazy
from .forms import register_form,Blog_Form
from .models import *


class Test(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'test.html'
# Create your views here.
class HomePage(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'index.html'

class Plantsgramm(ListView):
    model = Addblog
    context_object_name = 'blog'
    template_name = 'plantsgramm.html'
    def get_queryset(self):
        return Addblog.objects.order_by('-id')[:2]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class pgramm(ListView):
    model = Addblog
    context_object_name = 'blog'
    template_name = 'blogs.html'
    def get_queryset(self):
        return Addblog.objects.order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class Add_blog(CreateView):
    model = Addblog
    form_class = Blog_Form
    template_name = 'add_blog.html'
    success_url = reverse_lazy('main:plantsgramm')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class My_plants(TemplateView):
    template_name = 'myplants.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class Addplants(ListView):
    template_name = 'add.html'
    model = Addition
    context_object_name = 'add'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class Plantes(ListView):
    template_name = 'plants.html'
    model = Plants
    context_object_name = 'Plants'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class UserRegisterView(generic.CreateView):
    form_class = register_form
    template_name = 'registration.html' 
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

def result_page(request):
    q = request.GET.get('query')
    if len(q)>=2:
        query1 = Plants.objects.filter(title__icontains = q)
        query2 = Addition.objects.filter(title__icontains = q)

    return render(request,'result.html',{'plant':query1,'add':query2})

def category(request):
    c = request.GET.get('category')
    plant = Plants.objects.filter(category__name = c)
    category1 = Category.objects.all()
    return render(request,'category.html',{'plants':plant,'categories':category1})