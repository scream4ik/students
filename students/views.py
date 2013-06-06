# -*- coding: utf-8 -*-
from models import *
from forms import GroupAddForm, GroupEditForm, StudentsForm, LoginEmailForm

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


@login_required(login_url='/login/email/')
def index(request):
	
	groups = Group.objects.all()
	
	return TemplateResponse(request, 'index.html', {'groups': groups})


@login_required
def group_add(request):
	
	form = GroupAddForm(request.POST or None)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('students.views.index')
	
	return TemplateResponse(request, 'group_add.html', {'form': form})


@login_required
def group_edit(request, id):
	
	instance = get_object_or_404(Group, id=id)
	form = GroupEditForm(request.POST or None, instance=instance)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('students.views.index')
	
	return TemplateResponse(request, 'group_add.html', {'form': form})


@login_required
def group_del(request, id):
	
	try:
		Group.objects.get(id=id).delete()
	except Group.DoesNotExist:
		raise Http404
	
	return redirect('students.views.index')


@login_required
def group_list(request, id):
	
	group = get_object_or_404(Group, id=id)
	students = Students.objects.filter(group=group)
	
	return TemplateResponse(request, 'group_list.html', {'students': students, 'group': group})


@login_required
def student_add(request, group_id):
	
	group = get_object_or_404(Group, id=group_id)
	form = StudentsForm(request.POST or None)
	
	if request.method == 'POST':
		if form.is_valid():
			p = form.save(commit=False)
			p.group = group
			p.save()
			return redirect(reverse('group_list', args=[group.id]))
	
	return TemplateResponse(request, 'student_add.html', {'form': form, 'group': group})


@login_required
def student_edit(request, group_id, student_id):
	
	instance = get_object_or_404(Students, id=student_id, group=group_id)
	form = StudentsForm(request.POST or None, instance=instance)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(reverse('group_list', args=[instance.group.id]))
	
	return TemplateResponse(request, 'student_add.html', {'form': form, 'group': instance.group})


@login_required
def student_del(request, group_id, student_id):
	
	try:
		Students.objects.get(id=student_id, group=group_id).delete()
	except Students.DoesNotExist:
		raise Http404
	
	return redirect(reverse('group_list', args=[group_id]))