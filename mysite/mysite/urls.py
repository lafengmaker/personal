from django.conf.urls import patterns, include, url
from settings import STATICFILES_DIRS
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.index'),
    (r'^css/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':STATICFILES_DIRS[0]+'/css'}),
    (r'^js/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':STATICFILES_DIRS[0]+'/js'}),
     (r'^images/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':STATICFILES_DIRS[0]+'/images'}),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
