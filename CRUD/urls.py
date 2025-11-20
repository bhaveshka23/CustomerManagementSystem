from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.DisplayCustomer ,name="DisplayCustomers"),
    path('add-customer/',views.AddCustomer , name="AddCustomers"),
    path('update-customer/<int:Cst_id>',views.UpdateCustomer,name="UpdateCustomer"),
    path('delete-customer/<int:Cst_id>',views.DeleteCustomer,name="DeleteCustomer"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)