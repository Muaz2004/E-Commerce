from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.add,name="add"),
    path('<int:list_id>/', views.display, name="display"),
    path('login',views.login_request,name="login"),
    path('logout',views.logout_request,name="logout"),
    path('cdisplay/',views.cat_display,name="cdisplay"),
    path('remove/<int:list_id>/', views.remove, name="remove"),
    path('addtw/<int:list_id>/', views.add_to_watchlist, name="addtw"),
    path('wdisplay',views.wat_display,name="wdisplay"),
    path('acom/<int:list_id>/',views.add_comment,name="acom"),
    path('pbid/<int:list_id>/',views.place_bid,name="pbid"),
    path('close/<int:list_id>/',views.close_bid,name="close"),

    
]

