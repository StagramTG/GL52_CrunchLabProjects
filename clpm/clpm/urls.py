"""clpm URL Configuration

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
from django.urls import path, include

from restapi.views import (
    index,
    userviews,
    projectsviews,
    walletviews,
    shopviews,
)

from restapi.views.authenticate import (
    LoginView, 
    LogoutView, 
    RegisterView,
)

loginview = LoginView.as_view({
    'post': 'login'
})

logoutview = LogoutView.as_view({
    'post': 'logout'
})

registerview = RegisterView.as_view({
    'post': 'register'
})


urlpatterns = [
    # Main page
    path('', index.main),

    # User api
    path('api/user/list', userviews.users_list),
    path('api/user/search/<str:username>', userviews.users_search),
    path('api/user/details', userviews.user_details),
    path('api/user/selfupdate', userviews.user_selfupdate),
    path('api/user/<int:id>/update', userviews.user_update),
    path('api/user/<int:id>/info', userviews.user_info),
    path('api/user/<int:id>/delete', userviews.user_delete),

    # Project api
    path('api/project/list', projectsviews.project_list),
    path('api/project/<int:id>/details', projectsviews.project_details),
    path('api/project/create', projectsviews.project_create),
    path('api/project/update', projectsviews.project_update),
    path('api/project/delete', projectsviews.project_delete),

    # Project roles api
    path('api/project/role/list', projectsviews.projectrole_list),
    path('api/project/role/create', projectsviews.projectrole_create),
    path('api/project/role/delete', projectsviews.projectrole_delete),

    # Project User api
    path('api/user/<int:userid>/projects', projectsviews.user_project_list),
    path('api/project/<int:projectid>/users', projectsviews.project_user_list),
    path('api/project/adduser', projectsviews.add_user_to_project),
    path('api/project/deleteuser', projectsviews.delete_user_from_project),

    #Account api
    path('api/account/<int:id>/details', walletviews.account_details),
    path('api/account/transaction', walletviews.account_transaction),
    path('api/account/<int:id>/transactionlist', walletviews.transaction_list),
    path('api/account/reload', walletviews.account_reload),
    path('api/account/<int:id>/reloadlist', walletviews.reload_list),
    path('api/account/supply', walletviews.account_supply),
    path('api/account/<int:id>/update', walletviews.amount_update),

    #Products api
    path('api/products/list', shopviews.product_list),
    path('api/products/create', shopviews.create_product),
    path('api/products/<int:id>/details', shopviews.product_details),
    path('api/products/<int:id>/delete', shopviews.product_delete),
    path('api/products/<int:id>/update', shopviews.product_update),

    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('auth/login/', loginview, name='login'),
    path('auth/logout/', logoutview, name='logout'),
    path('auth/register/', registerview, name='register'),
]
