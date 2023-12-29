from django.shortcuts import redirect, render
from myapp.models import Image, Category

def show_home_page(request):
    category = Category.objects.all()
    image = Image.objects.all()
    context = {"image":image,"category":category}
    return render(request, "home.html",context)

def show_category_page(request,cid):
    category = Category.objects.all()
    cat = Category.objects.get(pk=cid)

    image = Image.objects.filter(cat=cat)
    context = {"image":image,"category":category}
    return render(request, "home.html",context)