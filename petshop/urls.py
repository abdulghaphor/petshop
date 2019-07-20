"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pets import views as _

urlpatterns = [
	path('admin/', admin.site.urls),
	path('pets/', _.index, name='index'),
	path('pets/add',_.pet_add,name='pet-add'),
	path('pets/delete/<int:pet_id>',_.pet_delete,name='pet-delete'),
	path('pets/details/<int:pet_id>',_.pet_details,name='pet-details'),
	path('pets/update/<int:pet_id>',_.pet_update,name='pet-update'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)