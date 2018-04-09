from django.contrib.gis import admin

from altonode.world.models import Place, Location, WorldBorder

admin.site.register(Location, admin.GeoModelAdmin)
admin.site.register(WorldBorder, admin.GeoModelAdmin)

class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


admin.site.register(Place, PlaceAdmin)
