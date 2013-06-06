# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


ACTION = (
	('add', 'Add'),
	('edit', 'Edit'),
	('delete', 'Delete'),
)


class Group(models.Model):
	
	name = models.CharField(max_length=100, verbose_name=u'Название')
	elder = models.ForeignKey('Students', verbose_name=u'Староста', related_name='elder', blank=True, null=True, unique=True)
	
	def get_students(self):
		return Students.objects.filter(group=self)
	
	def __unicode__(self):
		return self.name


class Students(models.Model):
	
	fio = models.CharField(max_length=200, verbose_name=u'ФИО')
	birthday = models.DateField(verbose_name=u'Дата рождения')
	student_card = models.IntegerField(verbose_name=u'No студ. билета', unique=True)
	group = models.ForeignKey(Group, verbose_name=u'Группа', related_name='group')
	
	def __unicode__(self):
		return self.fio


class Log(models.Model):
	
	action = models.CharField(max_length=10, choices=ACTION)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	
	def __unicode__(self):
		return str(self.id)


@receiver(post_save, sender=Group)
@receiver(post_save, sender=Students)
def add_or_edit(sender, instance, created, **kwargs):
	if created:
		p = Log(content_object=instance, action='add')
	else:
		p = Log(content_object=instance, action='edit')
	p.save()


@receiver(post_delete, sender=Group)
@receiver(post_delete, sender=Students)
def delete(sender, instance, **kwargs):
	p = Log(content_object=instance, action='delete')
	p.save()