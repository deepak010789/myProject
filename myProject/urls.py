from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    (r'^index/$','myProject.Premiere.views.search'),
    (r'^home/$','myProject.Premiere.views.home'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
