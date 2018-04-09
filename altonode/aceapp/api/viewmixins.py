from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response

from .serializers import SubscriberSerializer


class AjaxFormMixin(object):

	def post(self, request, *args, **kwargs):
		# Retrieve list of available services/projects
		service_list = Service.objects.all()
		project_list = Project.objects.all()	
		# Retrieve three team members
		squad_list = Squad.objects.all()[:3]
		# Fetch subscriber data
		serializer = SubscriberSerializer(data=request.data)
		if not serializer.is_valid():
			if self.request.is_ajax():
				return JsonResponse(serializer.errors,
					status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response({
					'serializer': serializer,
					'services': service_list,
					'portfolios': project_list, 
					'team': squad_list,},
					status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		if request.is_ajax():
			data = {
			'message': "Success!"
			}
			return JsonResponse(data, status=status.HTTP_201_CREATED)
		else:
			serializer = SubscriberSerializer()
			return Response({
				'serializer': serializer,
				'services': service_list,
				'portfolios': project_list, 
				'team': squad_list,}, status=status.HTTP_201_CREATED) 
