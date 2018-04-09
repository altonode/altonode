from datetime import date

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny

from altonode.aceapp.models import Service, Project, Squad
from .serializers import SubscriberSerializer
from .viewmixins import AjaxFormMixin

class HomeView(AjaxFormMixin, APIView):
	template_name = 'aceapp/index.html'
	renderer_classes = [TemplateHTMLRenderer]
	permission_classes = (AllowAny, )
	lookup_field = 'uuid'
	
	def post(self, request, *args, **kwargs):
		# Retrieve list of available services/projects
		service_list = Service.objects.all()
		project_list = Project.objects.all()[:3]

		# Retrieve three team members
		squad_list = Squad.objects.all()[:3]

		# Fetch subscriber data
		serializer = SubscriberSerializer(data=request.data)
		
		if not serializer.is_valid():
			if request.is_ajax():
				return JsonResponse(serializer.errors,
					status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response({
					'serializer': serializer,
					'services': service_list,
					'portfolios': project_list,
					'team': squad_list,
					},
					status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		if request.is_ajax():
			data = {
			'message': "Success!"
			}
			return JsonResponse(data)
		else:
			serializer = SubscriberSerializer()
			return Response({
				'serializer': serializer,
				'services': service_list,
				'portfolios': project_list, 
				'team': squad_list,
				}, 
			status=status.HTTP_201_CREATED)
		
	def get(self, request, *args, **kwargs):
		
		# Retreive list of available services/projects
		service_list = Service.objects.all()
		project_list = Project.objects.all()[:3]	
		
		# Retreive three team members
		squad_list = Squad.objects.all()[:3]
		
		# Initiate empty form
		serializer = SubscriberSerializer()
		
		# Establish the year
		this_day = date.today()
		this_year = this_day.year
		return Response({
			'serializer': serializer,
			'services': service_list,
			'portfolios': project_list,
			'team': squad_list,
			'year': this_year,
		})
