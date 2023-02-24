from django.urls import path, include
from useradmin import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.signin,name="signin"),
    path('logout',views.logout_view,name='logout'),
    path('custom-admin/',views.home,name='home'),
    path('ml',views.dfmodule),
    path('custom-admin/dashboard2',TemplateView.as_view(template_name='admin-lte/index2.html'),name='home2'),
    path('custom-admin/dashboard3',TemplateView.as_view(template_name='admin-lte/index3.html'),name='home3'),
    path('calender',TemplateView.as_view(template_name='admin-lte/pages/calendar.html'),name='calender')
]
