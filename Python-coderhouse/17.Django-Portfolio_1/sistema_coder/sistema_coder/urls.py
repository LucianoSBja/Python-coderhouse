"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from sistema_coder.views import saludar
from sistema_coder.views import saludar_con_fecha
urlpatterns = [
    path('admin/', admin.site.urls),
    # Aqui agregar mis URLS
    # path(RUTA, VIEW)
    # La RUTA de la URL puede ser diferente al nombre de la view
    path("hello/", saludar),
    path("saludar-fecha/", saludar_con_fecha),
]
