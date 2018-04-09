from django.urls import reverse

from altonode.world.models import Location

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class LocationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Location
        geo_field = 'geom'
        id_field = 'slug'
        fields = ('slug', 'name', 'objects')