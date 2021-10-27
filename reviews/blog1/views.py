from django.shortcuts import render
from .models import Post

from django.db import models
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import ArticleData, Category, Keyword
import requests
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# from wordcloud import WordCloud
# from wordcloud import STOPWORDS

import matplotlib.pyplot as plt
import io
import urllib, base64

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog1/post_list.html',{
        'post_list': qs
    })

# def word_cloud(text):
#     plt.figure(figsize = (20,5))
#     #plt.imshow(whale_mask , cmap = plt.cm.gray , interpolation = 'bilinear')
# #     font_path = './NanumBarunGothic.ttf'
#     wc = WordCloud(background_color = 'white', max_words=5)
#     wc= wc.generate(text)
#     plt.figure(figsize= (10,5))
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis("off")
#     image = io.BytesIO()
#     plt.savefig(image, format='png')
#     image.seek(0)  # rewind the data
#     string = base64.b64encode(image.read())
#     image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
#     return image

# def cloud_gen(request):
#     text = ''
#     for i in Article.objects.all():
#         if __name__ == '__main__':
#             text += i.text
#     wordcloud = word_cloud(text)
#     return render(request, 'post_list.html', {'wordcloud':wordcloud})
    