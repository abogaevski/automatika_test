from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied

from .serializers import StoreSerializer, VisitSerializer


class StoreListApiView(generics.ListAPIView):
    """ Store list authorize by employee phone """
    serializer_class = StoreSerializer

    def get_queryset(self):
        phone = self.kwargs['phone']
        return self.serializer_class.Meta.model.objects.filter(employee__phone=phone)


class VisitStoreApiView(generics.CreateAPIView):
    """ Visit store checked by employee phone """
    serializer_class = VisitSerializer

    def perform_create(self, serializer):
        phone = self.kwargs['phone']
        store = serializer.validated_data['store']

        if not store.employee.phone == phone:
            raise PermissionDenied('Вы не можете посетить данный магазин, так как он не привязан к вам')

        serializer.save()


