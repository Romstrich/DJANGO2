
from django.urls import path

from .views import index,products


app_name='mainapp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('products/',products,name='products'),
]
