"""colonialsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
import menus.views
import cas.views

router = routers.DefaultRouter()
router.register(r'api/menus', menus.views.MenuViewSet)
router.register(r'api/dishes', menus.views.DishViewSet)
router.register(r'api/ratings', menus.views.DishViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reservations/', include('reservations.urls')),
    url(r'^menus/', include('menus.urls')),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^$', include('dashboard.urls', namespace='dashboard')),
    url(r'^accounts/login/$', cas.views.login, name='login'),
    url(r'^accounts/logout/$', cas.views.logout, name='logout'),
]

urlpatterns += router.urls
