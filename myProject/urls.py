from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    (r'^index/$','myProject.Premiere.views.search'),
    (r'^home/$','myProject.Premiere.views.home'),
#    (r'^home/(?P<url>(?:.*?://)[\w\-\_\.\@\:\/\?\#\=]*)','myProject.Premiere.views.func'),
#    (r'^home/(?P<url>[/]?[\w]+[/]?([\w]+)?)$','myProject.Premiere.views.func'),
#    (r'^home/(?P<url>([/][\w]+)+([/][\w]+[:]?[\w|\d]+)+)$','myProject.Premiere.views.func'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # url(r'^myProject/', include('myProject.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
