from django import template
from altonode.aceapp.models import Project, Service

register = template.Library()

@register.inclusion_tag('pages/subscribers.html')
def get_subscriber_list(projo=None):
	return {'subscribers': Service.subscriber_set.all(),
			'active_project': projo}