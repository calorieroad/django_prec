from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView, TemplateView


urlpatterns = [
    # path('',TemplateView.as_view(template_name = 'root.html'),name = 'root'),
    path('',RedirectView.as_view(
        pattern_name = 'instagram:post_list')
        # url='/instagram/')
        ,name = 'root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    
]

# 실제 서비스에서는 DEBUG가 FALSE이기에 설정이 필요없음. 하지만 학습 단계에서 조금 더 명시적으로 표기
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        ]


    
# # 파일 불러오기에 사용
# settings.MEDIA_URL

# # 파일 저장에 사용
# settings.MEDIA_ROOT