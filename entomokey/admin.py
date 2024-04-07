from django.contrib import admin
from .models import (
    Insect,
    Habitats,
    Region,
    WeightTypeInsect,
    SizeTypeInsect,
    GeoDistribution,
    State,
    Country,
)


admin.site.register(Insect)
admin.site.register(Habitats)
admin.site.register(Region)
admin.site.register(SizeTypeInsect)
admin.site.register(WeightTypeInsect)
admin.site.register(GeoDistribution)
admin.site.register(State)
admin.site.register(Country)

