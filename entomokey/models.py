from django.db import models


class Habitats(models.Model):
	name = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=100)

class State(models.Model):
    name = models.CharField(max_length=100)

class GeoDistribution(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=100)

class SizeTypeInsect(models.Model):
    type_size = models.CharField(max_length=8)

class WeightTypeInsect(models.Model):
    type_size = models.CharField(max_length=8)


class Insect(models.Model):
    name_sci = models.CharField(max_length=200)
    name_commom = models.CharField(max_length=200)
    size = models.PositiveSmallIntegerField()
    size_type = models.ForeignKey(SizeTypeInsect, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    weight_type = models.ForeignKey(WeightTypeInsect, on_delete=models.CASCADE)
    properties = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    habitats = models.ForeignKey(Habitats, on_delete=models.CASCADE)
    geo_distribution = models.ForeignKey(GeoDistribution, on_delete=models.CASCADE)