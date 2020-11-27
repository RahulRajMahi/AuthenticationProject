from django.urls import path, include
from testapp import views

urlpatterns = [
    path('', views.homepage_view),
    path('language/', views.language_view_page_view),
    path('dbms/', views.dbms_page_view),
    path('cn/', views.cn_page_view),
    path('se/', views.se_page_view),
    path('ai/', views.ai_page_view),
    path('dmi/', views.dmi_page_view),
    path('cc/', views.cc_page_view),
    path('dm/', views.dm_page_view),
    path('em/', views.em_page_view),
    path('toc/', views.toc_page_view),
    path('comc/', views.comc_page_view),
    path('quiz/', views.quiz_page_view),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls'))

]
