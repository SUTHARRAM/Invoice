"""
URL configuration for invoiceapis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apis.services.billview.fetch_bill_detail_view import FetchBillDetailView
from apis.services.billview.test import fetch_data_from_postgres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/', FetchBillDetailView.as_view(), name='fetch-bill-detials-by-id'),
    path('fetch-data/', fetch_data_from_postgres, name='fetch-data'),
]
