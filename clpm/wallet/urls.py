from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reload/<int:id>', views.reload, name='reload'),
    path('shop/<int:id>', views.shop, name='shop'),
    path('account/<int:id>', views.account_index, name='account'),
]