import uuid as uuid_lib

from django.db import models
from django.conf import settings
from django.core.validators import phone_number_validator
from django.template.defaultfilters import slugify


class Service(models.Model):
	type = models.CharField(max_length=128, unique=True)
	details = models.CharField(max_length=128)
	fa_icon = models.CharField(max_length=128)
	
	def __str__(self):
		return self.type
	

class Project(models.Model):
	type = models.ForeignKey(Service)
	name = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=500)
	snapshot = models.ImageField(upload_to='project_snips', blank=True)
	screenshot = models.ImageField(upload_to='project_snips', blank=True)
	platform = models.URLField(blank=True)
	created = models.DateField(auto_now_add=True)
	slug = models.SlugField()	
	
	# update record
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Project, self).save(*args, **kwargs)
		
	def __str__(self):
		return self.name
		

class Squad(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	designation = models.CharField(max_length=128)
	bio = models.CharField(max_length=250)
	avatar = models.ImageField(upload_to='squad_pics')
	profile = models.URLField()
	
	
	class Meta:
		verbose_name_plural = 'Squad'
		
		
class Subscriber(models.Model):
	name = models.CharField(max_length=128, 
						help_text='Please enter your name.')
	email = models.EmailField(unique=True, 
							help_text='Please enter your email address.')
	organization = models.CharField(max_length=128, blank=True,
								help_text='Please enter name of institution.')
	phone = models.CharField(validators=[phone_number_validator], 
							max_length=15, blank=True,
							help_text='please enter phone number.')
	interest = models.ManyToManyField(Service, blank=True, 
				help_text='Please select service of interest.')
	message = models.TextField(max_length=250, 
							help_text='Please describe your project requirements.')
	created = models.DateTimeField(auto_now_add=True)
	# web api record identifier
	uuid = models.UUIDField(
		db_index=True,
		default=uuid_lib.uuid4,
		editable=False)	
	# web api url slug
	slug = models.SlugField(unique=True)	
	# update record
	def save(self, *args, **kwargs):
		self.slug = slugify(self.uuid)
		super(Subscriber, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ('created',)
		
	def __str__(self):
		return self.organization
		
	def get_absolute_url(self):
		return reverse('', kwargs={'slug': self.slug})

