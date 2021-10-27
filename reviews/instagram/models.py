from django.db import models
from django.db.models.fields import DateField
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators = [MinLengthValidator(3)]
    )
    # %y%m%d 年月日 
    photo = models.ImageField(blank = True, upload_to= 'instagram/post/%y%m%d')
    tag_set = models.ManyToManyField('Tag', blank = True)
    # tag가 없는 상황도 있을 수 있기에 blank는 True 해야함.
    is_public = models.BooleanField(default=False, verbose_name = '공개여부')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    # instagram의 admin에 message 내용 그대로 보여지기
    def __str__(self):
        # return "Custom object ({self.id})"
        return self.message
    
    def message_length(self):
        return len(self.message)

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args = [self.pk])
            

    # 원하는 description으로 변경
    # 인자 없는것만 가능
    message_length.short_description = "메세지 글자수"
    
    class Meta:
        ordering = ['-id']
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id 필드가 생성.
    # 이런식으로 import해서 사용도 가능.
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCAD)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name= models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    # 여기에 이렇게 관계를 만들어도 되고, 위 Post에 
    # tag_set = models.ManyToManyField(Tag) 이런식으로도 가능
    # python은 스크립트 언어이기에 Tag를 Post 위에 만들던지
    # tag_set = models.ManyToManyField('Tag')
    # 이렇게 문자열로 설정하면 됨.

    def __str__(self):
        return self.name
