from django.conf.urls import *
from article.views import articles
from article.views import article
from article.views import hello
from article.views import hello_template
from article.views import HelloTemplate
from article.views import hello_template_simple

from django.contrib import admin
admin.autodiscover()
urlpatterns=[
	url(r'^admin/', admin.site.urls),
	url(r'^articles/all/$',articles,name='articles'),
	url(r'^article/get/(?P<article_id>\d+)/$',article,name='article'),
    url(r'^hello/$',hello,name='hello'),
    url(r'^hello_class_view/$',HelloTemplate.as_view()),
    url(r'^hello_template/$',hello_template,name='hello_template'),
    url(r'^hello_template_simple/$',hello_template_simple,name='hello_template_simple')
]