from django.contrib import admin
from abonents.models import Abonents, Networks, Tariffs, States, Speed


admin.site.register((Abonents, Networks, Tariffs, States, Speed))

