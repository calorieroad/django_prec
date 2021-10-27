from django.contrib import admin
from .models import Post, Comment, Tag

# 장고에서 보안으로 링크가 이스케이프 처리가 되는데 그걸 안전하다고 내용을 보여달라는거
from django.utils.safestring import mark_safe
# Register your models here.

# admin.site.register(Post)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag','message', 'message_length','is_public','created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    # 검색 옵션
    search_fields = ['message']
    
    
# admin.site.register(Post)
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:80px;"/>')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass