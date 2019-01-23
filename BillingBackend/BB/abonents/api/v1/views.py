from rest_framework.views import APIView, Response, status
from django.http import HttpResponseRedirect
from django.urls import reverse


from abonents.models import Abonents
from abonents.serializers import AbonentsSerializer


class AbonentsViews(APIView):

    def get(request, *args, **params):
        try:
            abonent = Abonents.objects.get(**params)
            serialized_abonent = AbonentsSerializer(abonent)
            return Response(serialized_abonent.data)
        except Abonents.MultipleObjectsReturned:
            return Response({'attentions': ['Multiple users on this selection']},
                            status=status.HTTP_300_MULTIPLE_CHOICES)
        except Abonents.DoesNotExist:
            return Response({'attentions': ['Abonent not found']},
                            status=status.HTTP_404_NOT_FOUND)

    def post(request, *args, **kwargs):
        abonent_info = request.POST.dict()
        try:
            abonent = Abonents(**abonent_info)
            abonent.save()
            return HttpResponseRedirect(reverse('abonents'))
        except Exception as reason:
            return Response({'errors': reason},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



