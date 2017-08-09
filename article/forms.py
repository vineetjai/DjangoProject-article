from django import forms
from models import Article

class ArticleForm(forms.ModelForm):

	class Meta:
		model=Article
		fields=('title','body' , 'pub_date')
		#2016-03-21 11:00:00 time format