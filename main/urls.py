from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views 
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.signup,name='signup'),
    path('intro/',views.intro,name='intro'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('setting/',views.setting,name='setting'),
    path('setting_blog/',views.setting_blog,name='setting_blog'),
    path('setting_work/',views.setting_work,name='setting_work'),
    path('blog/',views.blog,name='blog'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)