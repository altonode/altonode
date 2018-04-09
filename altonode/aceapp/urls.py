from django.conf.urls import url
from django.views.generic import TemplateView

from .api import views

urlpatterns = [
	url(
		regex=r'^home/$',
		view=views.HomeView.as_view(),
		name='home_rest_api'
	),
	url(
		regex=r'^privacy/$', 
		view=TemplateView.as_view(template_name='aceapp/privacy.html'), 
		name='privacy_policy'
	),
	url(
		regex=r'^terms/$', 
		view=TemplateView.as_view(template_name='aceapp/terms.html'), 
		name='usage_terms'
	),	
]