from django.conf.urls import patterns, include, url
from django.conf import settings

from students.forms import LoginEmailForm
#from backend import EmailBackend

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'students.views.index', name='index'),
    url(r'^group/add/$', 'students.views.group_add', name='group_add'),
    url(r'^group/edit/(?P<id>[\-\w]+)/$', 'students.views.group_edit', name='group_edit'),
    url(r'^group/delete/(?P<id>[\-\w]+)/$', 'students.views.group_del', name='group_del'),
    url(r'^group/list/(?P<id>[\-\w]+)/$', 'students.views.group_list', name='group_list'),
    
    url(r'^student/add/(?P<group_id>[\-\w]+)/$', 'students.views.student_add', name='student_add'),
    url(r'^student/edit/(?P<group_id>[\-\w]+)/(?P<student_id>[\-\w]+)/$', 'students.views.student_edit', name='student_edit'),
    url(r'^student/delete/(?P<group_id>[\-\w]+)/(?P<student_id>[\-\w]+)/$', 'students.views.student_del', name='student_del'),
    
    url(r'^login/email/$', 'django.contrib.auth.views.login', {'authentication_form': LoginEmailForm}),
    url('', include('registration.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)


# Do not forget to serve static files in production with something but django
if settings.DEBUG and settings.MEDIA_URL.startswith('/'):
    
    urlpatterns += patterns('',

        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'),
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT,
             'show_indexes': True}),
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,
             'show_indexes': True}),
    )