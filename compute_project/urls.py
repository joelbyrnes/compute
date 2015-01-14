from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compute_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^compute/', include('compute.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
