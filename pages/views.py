from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render



def home_page_view(request):
	context = {
		"inventory_list":["Widget 1","Widget 2","Widget 3"],
		"greetings": "Thank you for visiting."

	}
	return render(request,"home.html",context )


class AboutPageView(TemplateView):
	template_name = "about.html" # the html to use in making the view
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["contact_address"] = "123 Main Street"
		context["phone_number"] = "555-555-5555"
		return context
	
class ProductsPageView(TemplateView):
	template_name="products.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["products_list"] = ["Cheese","Pencils","Cheese","More Cheese"]
		return context
	
class MessagesPageView(TemplateView):
	template_name="messages.html"
	#def get_context_data(self, **kwargs):

from .models import Page, Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#def post_list(request):
	#posts = Page.objects.all()
	#return render(request,"post_list.html",{"posts":posts})
	
class post_list(ListView):
	model = Page
	template_name = "post_list.html"
		

class posts(ListView):
	model = Post
	template_name = "posts.html"

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,"post_detail.html",{"post":post})
#gets the post object or raises an error but also has it so it bases in a post element
#with primary key of pk, as based in 

class BlogDetailView(DetailView):
	model = Post
	template_name = "post_detail.html"

class BlogCreateView(CreateView): #this will be the generic thing to bulid a new blog post page
	model = Post
	template_name = "post_new.html"
	fields = ["title","author","body"] #going to pass these to a form


class BlogUpdateView(UpdateView):
	model = Post
	template_name = "post_edit.html"
	fields = ["title","body"]

class BlogDeleteView(DeleteView):
	model = Post
	template_name = "post_delete.html"
	success_url = reverse_lazy("home") #when it happens, it goes to the url of the home name