from django.urls import path , re_path, register_converter
from . import views
from .converters import *


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')



app_name = 'instagram'

urlpatterns = [
    path('new/', views.post_new, name = 'post_new'),
    path('', views.post_list, name = 'post_list'),
    path('<int:pk>/', views.post_detail, name = 'post_detail'),
    
    # 위와 똑같음
    # re_path(r'(?P<pk>\d+)/$', views.post_detail)
    
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    # 20으로 시작하는거만 매칭
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),

    # 4자리수로 매칭
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('archive/', views.post_archive, name = 'post_archive'),
    path('archive/<year:year>', views.post_archive_year, name = 'post_year_archive'),
    path('kakaomap/', views.kakao_map, name = 'kakao_map'),
    path('kakaomap1/', views.kakao_map1, name = 'kakao_map1'),
    path('kakaomap2/', views.kakao_map2, name = 'kakao_map1'),
    
]
