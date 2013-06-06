# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from models import Group, Students


class GroupAddForm(forms.ModelForm):
	
	class Meta:
		model = Group
		exclude = ('elder',)


class GroupEditForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super (GroupEditForm, self).__init__(*args, **kwargs)
		instance = self.instance
		self.fields['elder'].queryset = Students.objects.filter(group=instance)
	
	class Meta:
		model = Group


class StudentsForm(forms.ModelForm):
	
	birthday = forms.DateField(widget=SelectDateWidget(years=range(1960, 2006)[::-1]))
	
	class Meta:
		model = Students
		exclude = ('group',)


class LoginEmailForm(AuthenticationForm):
	
	username = forms.EmailField(label="E-mail")