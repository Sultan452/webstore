from django.shortcuts import render,redirect,get_object_or_404
from .models import Product, Payment,Cart,CartItem,Category,Brand
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
       username = request.POST['signup_username']
       password1 = request.POST['signup_password1']
       password2 = request.POST['signup_password2']
       email = request.POST['signup_email']
       if password1 == password2:
           user = User.objects.create(username=username, email=email) 
           user.set_password(password1)
           user.save()
           login(request, user)
       return redirect('landing') 
    return render(request,'auth.html') 



def main(request):
    products= Product.objects.all()
    categories= Category.objects.all()
    brand = Brand.objects.all()
    return render(request,'index.html',{'products':products, 'categories':categories, 'brand':brand})

def detail(request, product_id):
    product= get_object_or_404(Product, id=product_id)
    return render(request,'details.html',{'product':product})

def logout_user(request ):
       logout(request)
       return redirect('signup')
   
def login_user(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user.is_valid():
            login(request, user)
            return redirect('landing')
        return redirect(request, 'login.html')
         

# Create your views here.
