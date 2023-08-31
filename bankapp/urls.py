from django.urls import path
from .views import *
urlpatterns=[
    path('index/',index),
    path('register/',register),
    path('login/',login),
    path('profile',profile),
    path('edit/<int:id>',edit),
    path('imageedit/<int:id>',imageedit),
    path('addmoney/<int:id>',addmoney),
    path('success/',success),
    path('widrawmoney/<int:id>',widrawmoney),
    path('widrawdisplay/',widrawdisplay),
    # path('balance/',balance),
    # path('balance1/',balance1)
    path('checkbalance/<int:id>',checkbalance),
    path('checkbalance1/',checkbalance1),
    path('statement/<int:id>',statement),
    path('depdisplay/',depdisplay),
    path('withdisplay/',withdisplay),
    # path('statementdisplay/',statementdisplay)
    path('news/',news),
    path('admin/',admin),
    path('newsdisplay/',newsdisplay),
    path('adminnewsdelete/<int:id>',adminnewsdelete),
    path('adminnewsedit/<int:id>',adminnewsedit),
    path('display/',display),
    path('wish/<int:id>',wish),
    path('wishlistview/',wishlistview),
    path('logoutt/',logoutt),
    path('forgotpassword/',forgot_password),
    path('change/',change),
    path('change_password/<int:id>',change_password),
    # path('moneytransferhtml/',moneytransferhtml),
    path('moneytransfer/',moneytransfer),
    path('profilebank/',profilebank)
]