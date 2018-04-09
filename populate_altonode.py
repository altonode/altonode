import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'config.settings.local')
import django
django.setup()
from altonode.aceapp.models import Service, Project

def populate():
# First, we will create lists of dictionaries containing the projects
# we want to add into each service type.
# Then we will create a dictionary of dictionaries for our service types.
# This allows us to iterate through each data structure, 
# and add the data to our models.
	
	custom_apps = [
		{
			"name": "Rango",
			"description": "Categories application deployed on pythonanywhere PaaS. It registers and authenticates users enabling access to additional features of the web application.",
			"platform":	"https://tonyops.pythonanywhere.com"
		},
	]
		
	web_apis = [
		{
			"name": "Online Signing",
			"description": "E-signature application for online document signing. The email app sends documents signed by authorized users to concerned parties while the storage app saves a copy of the transaction in the cloud.",
			"platform":	"https://altonodemo.pythonanywhere.com"
		},
		{
			"name": "drf_demo",
			"description": "Django Rest Framework app for handling blog posts.",
			"platform":	"https://github.com"
		},
	]
		
	online_education = [
		{
			"name": "Open edX Platform",
			"description": "Learning management and course authoring applications",
			"platform":	""
		},
	]
		
	services = {
				"Cloud Migration": {"type": custom_apps,
									"details":"Customized web apps that facilitate data storage in a managed cloud environment", 
									"fa-icon":"cubes" },		
				"RESTful Services": {"type": web_apis,
									 "details":"Lightweight, scalable & secure applications that interact with RESTful web services or APIs",
									 "fa-icon":"cogs" },
				"Open edX Integration": {"type": online_education,
										 "details":"Web-based system for creating, delivering, and analyzing online courses",
										 "fa-icon":"graduation-cap" },
			}
		
	# add them to the dictionaries above.

	# The code below goes through the services dictionary, then adds each service,
	# and then adds all the associated projects for that service.

	for service, service_type in services.items():
		s = add_service(service, service_type["details"], service_type["fa-icon"])
		for p in service_type["type"]:
			add_project(s, p["name"], p["description"], p["platform"])
	
	# Print out the services we have added.
	for s in Service.objects.all():
		for p in Project.objects.filter(type=s):
			print("- {0} - {1}".format(str(s), str(p)))
		
def add_project(service, name, description, platform):
	p = Project.objects.get_or_create(type=service, name=name)[0]
	p.description=description
	p.platform=platform
	p.save()
	return p
	
def add_service(type, details, icon):
	s = Service.objects.get_or_create(type=type)[0]
	s.details = details
	s.fa_icon = icon
	s.save()
	return s
	
# Start execution here!
if __name__ == '__main__':
	print("Starting Altonode population script...")
	populate()
