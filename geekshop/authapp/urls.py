

from django.urls import path,include

from .views import login,register,logout

app_name='authapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    #path('',include('mainapp.urls',namespace='mainapp')),
   ]

#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)