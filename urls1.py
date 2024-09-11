from django.contrib import adminhttps://www.onlinegdb.com/online_python_compiler#_editor_8142346861
from django.urls import path,include

urlspatterns = [
    path('admin/',admin.site.urls),
    path('api/',include('products.urls')),
    ]