from django.conf.urls import patterns, url

from compute import views

urlpatterns = patterns('',
       url(r'^$', views.index, name='index'),

       url(r'^test$', views.test, name='test'),

       url(r'^tasks/?$', views.tasks, name='tasks'),

       url(r'^task/(?P<task_id>\d+)/$', views.task, name='task'),

       url(r'^new_task$', views.new_task, name='new_task'),
       url(r'^save_task$', views.save_task, name='save_task'),
)