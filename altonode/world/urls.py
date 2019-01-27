from django.views.generic import TemplateView
from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from altonode.world.models import Location


urlpatterns = [
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Location), name='data')
]