from django.urls import path
from .views import  (
    index,
    category_detail,
    product_detail,
    contact_us,
     
)


app_name = 'spectr'


urlpatterns = [
    path('', index, name = "index" ),    
    path('category/<int:pk>/', category_detail, name = "category_detail" ),
    path('product/<int:pk>/', product_detail, name = "product_detail"),
    path('contact_us', contact_us, name = "contact_us"),
    ]