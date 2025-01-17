from django.urls import path 
from serviceapp import views 
urlpatterns = [
   
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('homelog/', views.homelog,name='homelog'),
    path('aboutlog/',views.aboutlog,name='aboutlog'),
    path('register/',views.register,name='register'),
    path('company/',views.company,name='company'),
    path('store/',views.store,name='store'),
    path('shop/<int:id>',views.shop,name='shop'),
    path('company/<str:name>',views.companyview,name="company"),
    path('company/<str:cname>/<str:pname>',views.oneproduct,name="oneproduct"),
    path('centerpaycheck/<str:obj>',views.centerpaycheck,name='centerpaycheck'),
    path('centerpay/',views.centerpay,name='centerpay'),
    path('signup/',views.signup,name='signup'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('centernewlog/',views.centernewlog,name='centernewlog'),
    path('centernewlog/centerprofile/',views.centerprofile,name='centerprofile'),
    path('centernewlog/centerprofile/<int:id>/centerupdate/',views.centerupdate,name='centerupdate'),
    path('centernewlog/centerprofile/<int:id>/centerupdate/centerupdateperson/',views.centerupdateperson,name='centerupdateperson'),
    path('centernewlog/centerprofile/<int:id>/centerdelete/',views.centerdelete,name='centerdelete'),
    path('signup/',views.signup,name='signup'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userprofile/<int:id>',views.userprofile,name='userprofile'),
    path('userprofile/<int:id>/userupdate',views.userupdate,name='userupdate'),
    path('userprofile/<int:id>/userupdate/userupdateperson/',views.userupdateperson,name='userupdateperson'),
    path('userprofile/<int:id>/userdelete/',views.userdelete,name='userdelete'),
    path('userpaycheck/<str:name>',views.userpaycheck,name='userpaycheck'),
    path('userpay/<int:price>/<int:id>',views.userpay,name='userpay'),
    path('orders/<int:id>',views.orders,name='orders'),
    path('ordered/',views.ordered,name='ordered'),
    path('myorders/<str:userfname>',views.myorders,name='myorders'),
    path('centerorder/<str:comname>',views.centerorder,name='centerorder'),
]
