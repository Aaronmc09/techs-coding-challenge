from rest_framework import serializers
from .models import Record


from rest_framework import serializers, response, status


class ResponseMixin(serializers.BaseSerializer):

    def create(self, validated_data):
        super().create(validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

    def to_representation(self, instance):
        super().to_representation(instance)

    def to_internal_value(self, data):
        super().to_internal_value(data)

    @staticmethod
    def error_response(message: str, data: dict, status_code: int = 400,
                       developer_message: str = None) -> response.Response:
        """Generates a DRF Response object.

        Response body will contain:
            {
                'message': 'The message of the error',
                'errors': {}  # Any errors that should be returned
                'developer_message': 'A message that is more suited to developers',
            }
        """

        if 'detail' in data and data['detail'] == message:
            data.pop('detail')

        new_data: dict = {
            'message': message,
            'errors': data
        }

        if developer_message:
            new_data['developer_message'] = developer_message

        return response.Response(new_data, status=status_code)

    def as_response(self, success_status_code: int = status.HTTP_200_OK,
                    error_status_code: int = status.HTTP_400_BAD_REQUEST, error_message: str = 'Bad request'):

        if hasattr(self, '_errors') and self.errors:
            return self.error_response(error_message, self.errors, status_code=error_status_code)

        print("here")
        return response.Response(self.data, status=success_status_code)


class WriteRecord(serializers.ModelSerializer, ResponseMixin):
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id',)


class ReadRecord(WriteRecord):
    class Meta:
        model = Record
        fields = '__all__'
        read_only = True
