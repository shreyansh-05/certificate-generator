from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="Home page"),
    path('gencertificate',views.writeonimage,name="bulk creator"),
    path('readdata',views.readata,name="Read from csv"),
    path("generate",views.writeonimage,name="start writing"),
    path("result",views.result,name='result'),
    path('accounts/signup/', views.signup, name='signup'),
]
