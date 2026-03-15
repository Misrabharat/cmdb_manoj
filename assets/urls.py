from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_asset, name='search_asset'),
    path('asset/<int:id>/', views.asset_detail, name='asset_detail')
]