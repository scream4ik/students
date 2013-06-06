# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def edit_link(object):
	url = reverse('admin:%s_%s_change' %(object._meta.app_label,  object._meta.module_name),  args=[object.id] )
	return u'<a href="%s">Редактировать в админке</a>' % url