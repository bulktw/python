from django.conf.urls import include, url

from youtube import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^list/$', views.list, name='list'),
	url(r'^list/(?P<employee_id>\d+)/$', views.detail, name='detail'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^edit/(?P<employee_id>\d+)/$', views.edit, name='edit'),
	url(r'^remove/(?P<employee_id>\d+)/$', views.remove, name='remove'),
	#url(r'^(?P<employee_id>\d+)/list/$', views.list, name='list'),
]