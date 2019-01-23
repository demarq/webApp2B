from rest_framework.serializers import ModelSerializer
from .models import Abonents


class AbonentsSerializer(ModelSerializer):
    class Meta:
        model = Abonents
        fields = '__all__'
