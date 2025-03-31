# from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('',views.home,name="home"),
    path('add_product/',views.add_product,name="add_product"),
    path('product/',views.view_product,name='view_product'),
    path('all_products/',views.all_products,name='all_products'),
    path('delete/',views.delete_product,name="delete_product"),
    path('login/',views.login_view,name="login"),
    path('Signup/',views.signup,name="signup"),
    path('log_out/',views.log_out,name="log_out"),
    path('edit_product/',views.edit_product,name="edit_product"),
    path('buy_product/',views.buy_product , name="buy_product"),
]