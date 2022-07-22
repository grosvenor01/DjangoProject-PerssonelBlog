from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import profile,work,post,certificate,skille
# Create your views here.
def index(request):
    
    context={
        'profile':profile.objects.get(user=request.user),
        'work':work.objects.filter(user=request.user),
        'post':post.objects.filter(user=request.user),
        'certificate':certificate.objects.filter(user=request.user),
        'skille':skille.objects.filter(user=request.user)
    }
    return render(request ,'index.html',context)
def setting(request):
    return render(request,'contact.html')
def setting_blog(request):
    if request.method=='POST':
        description_blog=request.POST.get('desc')
        pic_cerf=request.POST.get('pic_cerf')
        titre=request.POST.get('titre_blog')
        date=request.POST.get('date_blog')
        site=request.POST.get('site')
        if certificate.objects.filter(titre_blog=titre,user=request.user).exists():
            messages.info(request,"somthing goes wrong")
            return redirect('setting')
        else:
            new_blog=certificate.objects.create(user=request.user,titre_blog=titre,pic_cerf=pic_cerf,description_cerf=description_blog,site=site,date=date)
            new_blog.save()
            return redirect('/')
    print("dady")
    return render(request ,'contact.html')
def setting_work(request):
    if request.method=='POST':
        description_work=request.POST.get('description_certificate')
        pic_work=request.POST.get('work_pic')
        titre=request.POST.get('titre_work')
        date=request.POST.get('date_work')
        if work.objects.filter(titre_work=titre,user=request.user).exists():
            messages.info(request,"somthing goes wrong")
            return redirect('setting')
        else:
            new_work=work.objects.create(user=request.user,titre_work=titre,pic=pic_work,année=date,description_work=description_work)
            new_work.save()
            return redirect('/')
        
    return render(request ,'contact.html')
def blog(request):
    context={
        'blog':certificate.objects.filter(user=request.user)
    }
    return render(request ,'blog.html',context)
def portfolio_details(request):
    return render(request ,'portfolio-detail.html')
def portfolio(request):
    context={
        'work':work.objects.filter(user=request.user)
    }
    return render(request ,'portfolio.html',context)
def blog_details(request):
    return render(request ,'blog-detail.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or User.objects.filter(password=password).exists():
            messages.info(request,'somthing goes wrong')
            return redirect('/login/')
        else:
            user =User.objects.create(username=username , email=email , password=password)
            user.set_password(password)
            user.save()
            return redirect('/signin/')
    return render(request,'signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            prf=profile.objects.get(user=request.user)
            if prf.profile_pic is None and prf.description is None:
                return redirect('/intro/')
            else:
                return redirect('/') 
            
        else :
            messages.info(request,"somthing goes wrong")
            return redirect('login')
    return render(request,'signup.html')
def logout(request):
    
    auth.logout(request)
    return redirect("/login/")
def intro(request):
    if request.method=='POST':
        profile_pic=request.POST.get('profile_pic')
        desc=request.POST.get('description')
        if profile.objects.filter(user=request.user).exists():
            return redirect('/')
        else:
            new_profile=profile.objects.create(user=request.user,profile_pic=profile_pic,description_profile=desc)
            new_profile.save()
            return redirect('/')     
    return render(request,'intro.html')