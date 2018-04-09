from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from altonode.aceapp.models import Subscriber
from altonode.aceapp.models import Project
from altonode.aceapp.models import Service


class SubscriberTests(APITestCase):
    
	def create_subscriber(self, name, email, message):
	    url = reverse('aceapp:home_rest_api')
	    data = {
		    'name': name,
            'email': email,
			'message': message}
	    response = self.client.post(url, data, format='json')
	    return response
		
	def test_create_and_retrieve_subscriber(self):
	    """
	    Ensure we can create a new Subscriber and then retrieve it
	    """
	    name = 'New Game Category'
	    email = 'subscriber@example.com'
	    message = 'Message from new subcriber'
	    response = self.create_subscriber(name, email, message)
	    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	    self.assertEqual(Subscriber.objects.count(), 1)
	    self.assertEqual(Subscriber.objects.get().email, email)
	    print("PK {0}".format(Subscriber.objects.get().pk))
		
	def test_create_duplicated_subscriber_email(self):
	    """
	    Ensure we can't create a new Subscriber with an existing email address
	    """
	    url = reverse('aceapp:home_rest_api')
	    name = 'Copycat'
	    email = 'copycat@example.com'
	    message = 'The name is cat, copy cat!'
	    response_1 = self.create_subscriber(name, email, message)
	    self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
	    response_2 = self.create_subscriber(name, email, message)
	    self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)
		

class ProjectTests(APITestCase):
    
	def create_service(self, service_type, details, icon):
	    service = Service.objects.get_or_create(
		    type=service_type, 
			details=details,
			fa_icon=icon)[0]
	    service.save()
	    return service
		
	def create_project(self, name, description):
	    service_type = 'Web Services'
	    details = 'Web service delivery.'
	    icon = 'cloud'
	    type = self.create_service(service_type, details, icon)
	    project = Project.objects.get_or_create(
		    type=type,
			name=name,
			description=description)[0]
	    project.save()
	    return project
		
	def test_create_and_retrieve_project(self):
	    """
	    Ensure we can create a new Project and then retrieve it
	    """
	    name = 'Web Services'
	    description = 'Web service delivery'
	    project = self.create_project(name, description)
	    project.save()
	    self.assertEqual(Project.objects.count(), 1)
	    self.assertEqual(Project.objects.get().name, name)
			
	def test_slug_line_creation(self):
	    """
	    Ensure an appropriate slug line is created when we save a new project
	    """
	    name = 'Slug Test Project'
	    description = 'A test to evaluate the slug field'
	    project = self.create_project(name, description)
	    project.save()
	    self.assertEqual(Project.objects.get().slug, 'slug-test-project')

		
class HomeViewTests(APITestCase):

	def test_index_view_template_with_no_model_data(self):
	    """
	    If there is no model data, an appropriate message should be displayed
	    """
	    response = self.client.get(reverse('home'))
	    self.assertEqual(response.status_code, 200)
	    self.assertContains(response, "Cloud Networks")
	    self.assertQuerysetEqual(response.context['services'], [])
	    self.assertContains(response, "Django Web Apps")
	    self.assertQuerysetEqual(response.context['portfolios'], [])
	    self.assertContains(response, "Altonode Networks Team")
	    self.assertQuerysetEqual(response.context['team'], [])
		