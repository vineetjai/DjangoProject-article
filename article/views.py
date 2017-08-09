# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
#from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article
from forms import ArticleForm
from django.shortcuts import render
#from django.core.context_processors import csrf

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
	language ="en-gb"
	session_language ='en-gb'
	if 'lang' in request.COOKIES:
		language =request.COOKIES['lang']
	if 'lang' in request.session:
		session_language =request.session['lang']
	return render_to_response('articles.html',{'articles':Article.objects.all(),'language':language,'session_language':session_language})
def article(request,article_id=1):
	return render_to_response('article.html',{'article':Article.objects.get(id=article_id)})
def language(request,language='en-gb'):
	response =HttpResponse("setting language to %s"%language)
	response.set_cookie('lang',language)
	request.session['lang']=language
	return response

def create(request):
	if request.POST:
		form=ArticleForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/articles/all')
	else:
		form = ArticleForm()

	args={}
	args['form']=form
	return render(request,'create_article.html',args)