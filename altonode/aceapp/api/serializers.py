from altonode.aceapp.models import Service, Project, Squad, Subscriber

from rest_framework import serializers

class SubscriberSerializer(serializers.ModelSerializer):

		
	class Meta:
		model = Subscriber
		fields = ['name', 'email', 'organization', 'phone', 'message', 
				  'interest', 'uuid']
		extra_kwargs = {
			'name': {'style': {'placeholder': 'Your Name*',
								'hide_label': True,
								}
						},
			'email': {'style': {'placeholder': 'Valid Email Address*',
								'hide_label': True,
								}
						},
			'organization': {'style': {'placeholder': 'Your Company:',
										'hide_label': True,
										}
						},
			'phone': {'style': {'placeholder': 'Reachable Contacts:',
								'hide_label': True,
								}
						},
			'message': {'style': {
								'placeholder': 'Project Needs Described*',
								'base_template': 'textarea.html',
								'hide_label': True,
								}
						},
			'interest': {'style': {
									'placeholder': 'Area of Interest (Optional):',
									'base_template': 'checkbox_multiple.html',
									'hide_label': True,
								}
						},
		}

		
class SquadSerializer(serializers.ModelSerializer):


	class Meta:
		model = Squad
		fields = ('user', 'designation', 'bio', 'avatar', 'profile')
		
		
class ProjectSerializer(serializers.ModelSerializer):


	class Meta:
		model = Project
		fields = ('type', 'name', 'description', 'snapshot', 'platform', 
			'created')
			

class ServiceSerializer(serializers.ModelSerializer):


	class Meta:
		model = Service
		fields = ('type', 'details', 'fa_icon')
