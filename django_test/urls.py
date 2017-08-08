"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
'''from article.views import hello
from article.views import hello_template
from article.views import HelloTemplate
from article.views import hello_template_simple'''

'''urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello,name='hello'),
    url(r'^hello_class_view/$',HelloTemplate.as_view()),
    url(r'^hello_template/$',hello_template,name='hello_template'),
    url(r'^hello_template_simple/$',hello_template_simple,name='hello_template_simple'),
]'''
urlpatterns =[
	url(r'^admin/', admin.site.urls),
	url(r'',include('article.urls')),

]