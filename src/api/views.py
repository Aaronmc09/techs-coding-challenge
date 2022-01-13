from rest_framework import viewsets, mixins
from .models import Record
from . import serializers


class Records(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):

    lookup_field = 'id'

    def get_queryset(self):
        return Record.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return serializers.WriteRecord

        return serializers.ReadRecord

    def create(self, request, *args, **kwargs):
        serializer: serializers.WriteRecord = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)

        return serializer.as_response(error_message='Unable to create record.')
