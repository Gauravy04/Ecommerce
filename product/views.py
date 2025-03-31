from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Product, User
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth import logout, login
# Create your views here.
def home(request):
    user_id = request.session.get('id')
    user = User.objects.get(id=user_id) if user_id else None
    product = Product.objects.all()
    print(user)
    return render(request, "product/index.html", {"products": product, "user": user})

@csrf_exempt
def test_view(request):
    if request.method=="POST":
        name= request.POST.get("name")
        age= request.POST.get("age")
        email= request.POST.get("email")
        data = {"name":name,"age":age,"email":email}
        return render(request,'product/test2.html',{"data":data.values()})
    return render(request,'product/test.html')

@csrf_exempt
def add_product(request,product=None):
    if request.method=='POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        category = request.POST.get("category")
        images = request.FILES.get("images")
        product_id = request.POST.get("product_id")
        print("----",product_id)
        if product_id:
            print("okkkkk")
            print(product_id)
            product = Product.objects.get(id=product_id)
            product.name = name
            product.price = price
            product.quantity = quantity
            product.category = category
            product.images = images
            product.description = description
            product.save()
            return redirect('home')
        else:
            image_path = images if images else None
            product = Product.objects.create(name=name,price=price,quantity=quantity,description=description,category=category,images=image_path)
    return render(request,'product/add_product.html')

def view_product(request):
    product_id=request.GET.get("product_id")
    user_id = request.GET.get("user_id")
    print(product_id)
    print(type(product_id))
    print(user_id)
    product = Product.objects.get(id=product_id)
    if user_id:
        user = User.objects.get(id=int(user_id))
        return render(request,'product/view_product.html',{"product":product, "user":user})
    return render(request,'product/view_product.html',{"product":product})
    

def all_products(request):
    products = Product.objects.all()
    print(products)
    return render(request,'product/all_products.html',{"products":products})

def delete_product(request):
    # if request.method=="DELETE":
        product_id = request.GET.get("product_id")
        products = Product.objects.get(id=product_id)
        products.delete()
        return redirect('all_products')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if password==password:
            request.session['id']=user.id
            print(user.username,"okkkkkkkk")
            print(user.id,"okkkkkkkk")
            return redirect('home')  # Redirect to a success page.
        else:
            # return HttpResponse("invalid")
            return redirect('login')
    return render(request, 'product/login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password==confirm_password:
            user = User(username=username,email=email,phone=phone,password=password)
            print(user)
            user.save()
        return redirect('home')
    user = User.objects.all()
    return render(request,'product/signup.html')

def edit_product(request):
    product_id = request.GET.get("product_id")
    product = Product.objects.filter(id=product_id).first()
    return render(request,"product/add_product.html",{'product':product})

def log_out(request):
    logout(request)
    request.session.flush()
    return render(request,'product/login.html')


def buy_product(request,user=None):
    product_id = request.GET.get("product_id")
    product= Product.objects.get(id=product_id)
    user_id = request.GET.get("user_id")
    print(user_id)
    if user_id==None:
        return redirect('login')
    user_id = int(user_id)
    user = User.objects.get(id=user_id)
    return render(request,'product/order_confirmation.html',{"product":product,"user":user})
    
def order_confirmation(request):
    pass

