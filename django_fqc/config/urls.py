"""django_fqc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r'^password-reset/$',
            TemplateView.as_view(template_name="password_reset.html"),
            name='password-reset'),
    re_path(r'^password-reset/confirm/$',
            TemplateView.as_view(template_name="password_reset_confirm.html"),
            name='password-reset-confirm'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
            TemplateView.as_view(template_name="password_reset_confirm.html"),
            name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    # path('api/employees/', include('employee.routers')),
    path('api/patients/', include('patient.routers')),
    path('api/products/', include('product.routers')),
    # path('api/purchases/', include('purchase.routers')),
    path('api/sales/', include('sale.routers')),
    # path('api/warehouses/', include('warehouse.routers')),
    path('api/users/', include('userapi.routers')),
    path('api/healthinsurances/', include('healthinsurance.routers')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
