from rest_framework import serializers
from .models import WheelSpecification, BogieChecksheet

class WheelSpecificationSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(required=True)
    submittedBy = serializers.CharField(required=True)
    submittedDate = serializers.DateField(required=True)
    fields = serializers.JSONField(required=True)

    class Meta:
        model = WheelSpecification
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields']

    def validate_fields(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError('fields must be a dictionary.')
        if not value:
            raise serializers.ValidationError('fields cannot be empty.')
        return value

class BogieChecksheetSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(required=True)
    inspectionBy = serializers.CharField(required=True)
    inspectionDate = serializers.DateField(required=True)
    bogieDetails = serializers.JSONField(required=True)
    bogieChecksheet = serializers.JSONField(required=True)
    bmbcChecksheet = serializers.JSONField(required=True)

    class Meta:
        model = BogieChecksheet
        fields = [
            'formNumber', 'inspectionBy', 'inspectionDate',
            'bogieDetails', 'bogieChecksheet', 'bmbcChecksheet'
        ]

    def validate_bogieDetails(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError('bogieDetails must be a dictionary.')
        if not value:
            raise serializers.ValidationError('bogieDetails cannot be empty.')
        return value

    def validate_bogieChecksheet(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError('bogieChecksheet must be a dictionary.')
        if not value:
            raise serializers.ValidationError('bogieChecksheet cannot be empty.')
        return value

    def validate_bmbcChecksheet(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError('bmbcChecksheet must be a dictionary.')
        if not value:
            raise serializers.ValidationError('bmbcChecksheet cannot be empty.')
        return value 