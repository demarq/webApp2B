from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField


class Abonents(models.Model):
    login = models.TextField(unique=True)
    password = models.TextField(default='', null=True)
    ip = models.TextField(blank=True)
    mac = models.TextField(blank=True)
    tariff = models.ForeignKey('Tariffs', on_delete=models.SET_NULL, unique=False, blank=True, null=True)
    network = models.ForeignKey('Networks', on_delete=models.SET_NULL, unique=False, blank=True, null=True)
    money = models.IntegerField(default=0)
    state = models.ForeignKey('States', on_delete=models.SET_NULL, unique=False, blank=True, null=True)
    first_name = models.TextField(blank=True)
    second_name = models.TextField(blank=True)
    third_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    links = ArrayField(base_field=models.IntegerField(), blank=True, null=True)
    is_online = models.BooleanField()

    class Meta:
        db_table = 'abonents'

    def __str__(self):
        return '%s %s %s %s %s' % (self.login, self.first_name, self.second_name, self.third_name, self.ip)


class Tariffs(models.Model):
    name = models.TextField(unique=True)
    payment = models.IntegerField()
    speed = models.ForeignKey('Speed', on_delete=models.SET_NULL, unique=False, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.payment, self.speed)


class Speed(models.Model):
    name = models.TextField()
    local_in = models.IntegerField()
    local_out = models.IntegerField()
    world_in = models.IntegerField()
    world_out = models.IntegerField()

    def __str__(self):
        return '%s %s/%s' % (self.name, self.world_in, self.world_out)


class Networks(models.Model):
    gateway = models.TextField()
    netmask = models.TextField()
    ip = models.TextField()
    description = models.TextField()
    name = models.TextField()

    def __str__(self):
        return '%s %s/%s' % (self.name, self.ip, self.netmask)


class States(models.Model):
    name = models.TextField()
    status = models.TextField()
    description = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.status)
