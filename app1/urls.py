"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
   path('home/',views.Home),
    path('cart/',views.Cart,name='cart'),
    path('cart/remove/',views.removeFromCart),
    path('cart/checkout/',views.checkout),
    path('cart/checkout/complete/',views.completeOrders),
    path("admin-login/",views.adminLogin),
    path("admin-panel/",views.adminDashboard,name="admin"),
]
