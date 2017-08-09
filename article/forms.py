from django import forms

class Form(forms.Form):
	username=forms.CharField(label='Username')
	password=forms.CharField(label='Password')
	passwordcon=forms.CharField(label='Password')
