from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.Login_View,name='Login_View'),
    path('signup/',views.Signup_View,name='Signup_View'),
    path('logout/',views.Logout,name='Logout'),
    path('home',views.Home,name='Home'),
    path('homepage/',views.News_Feed,name='News_Feed'),
    path('',views.blank,name='blank'),
    path('edit/',views.EditProfile,name='EditProfile'),
    
]+ static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
