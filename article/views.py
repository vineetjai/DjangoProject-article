# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article


def hello(request):
	name="Vineet"
	html="<html><body>Hi %s, this seems to be working!</body></html>" % name
	return HttpResponse(html)
def hello_template(request):
	name="Vineet"
	t=get_template('hello.html')
	html=t.render({'name':name})
	return HttpResponse(html)
def hello_template_simple(request):
	name="VINEET"
	return render_to_response('hello.html',{'name':name})
class HelloTemplate(TemplateView):
	template_name='hello_class.html'
	def get_context_date(self ,**kwargs):
		context=super(HelloTemplate,self).get_context_date(**kwargs)
		context['name']='VINEET'
		return context

def articles(request):
	return render_to_response('articles.html',{'articles':Article.objects.all()})
def article(request,article_id=1):
	return render_to_response('article.html',{'article':Article.objects.get(id=article_id)})
