from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
def login(request):
    if request.method=="POST":
        ps=request.POST['pwd']
        ur=request.POST['username']
        user=auth.authenticate(username=ur,password=ps)
        if user is not None:
            auth.login(request,user)
            return redirect("index")
        else:
            messages.info(request,"Invalid Creds !")
            return render(request,"register.html")
    return render(request,"login.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def index(request):
    return render(request,"index.html")
def support(request):
    return render(request,"support.html")
def register(request):
    if request.method=="POST":
        un=request.POST['Username'] #username
        em=request.POST['email'] #email
        pd=request.POST['password']
        rpd=request.POST['rpwd'] #repeat password
        if pd==rpd:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username already exists !")
                return render(request,"register.html")
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email already exists !")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=un,email=em,password=pd)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Passwords not matching !")
            return render(request,"register.html")
    else:
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("index")