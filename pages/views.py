from django.shortcuts import render
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