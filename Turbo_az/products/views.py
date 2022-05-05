from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  categories = Category.objects.all()
  products = Product.objects.all()

  context = {
    'products' : products,
    'categories' : categories
  }

  return render(request, "all_products.html", context)


@login_required(login_url = "user_login")
def image_upload_view(request):
  if (request.method == 'POST'):
    form = ImageForm(request.POST, request.FILES)

    if (form.is_valid()):
      form.save()
      img_obj = form.instance
      context = {
        'form' : form,
        'img_obj' : img_obj
      }

      return redirect('index')
  
  else:
    form = ImageForm()
  
  context = {
    'form' : form
  }
  
  return render(request, "add_product.html", context)