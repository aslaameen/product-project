from django.urls import path

from product_app import views

urlpatterns = [
    path("add",views.product,name="add"),
    path("view",views.view,name="View"),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('index',views.index,name='index'),

]
