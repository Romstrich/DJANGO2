

from django.urls import path,include

from .views import login,register,profile

app_name='authapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    #path('',include('mainapp.urls',namespace='mainapp')),
   ]

#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)