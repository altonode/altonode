import uuid as uuid_lib

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.template.defaultfilters import slugify

from location_field.models.spatial import LocationField


class WorldBorder(models.Model):
	# Regular Django fields corresponding to the attributes in the
	# world borders shapefile.
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField('Population 2005')
	fips = models.CharField('FIPS Code', max_length=2)
	iso2 = models.CharField('2 Digit ISO', max_length=2)
	iso3 = models.CharField('3 Digit ISO', max_length=3)
	un = models.IntegerField('United Nations Code')
	region = models.IntegerField('Region Code')
	subregion = models.IntegerField('Sub-Region Code')
	lon = models.FloatField()
	lat = models.FloatField()	
	# GeoDjango-specific: a geometry field (MultiPolygonField)
	mpoly = models.MultiPolygonField()
	
	# Returns the string representation of the model.	
	def __str__(self):
		return self.name


class Place(models.Model):
    parent_place = models.ForeignKey('self', null=True, blank=True)
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=13, 
		default=Point(1.0, 1.0))
    objects = models.GeoManager()

    def __str__(self):
        return self.city
	

class Location(models.Model):
	name = models.CharField(max_length=255)
	geom = models.PointField()
	objects = models.GeoManager()	
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
		super(Location, self).save(*args, **kwargs)

	def __str__(self):
	    return self.name
	
