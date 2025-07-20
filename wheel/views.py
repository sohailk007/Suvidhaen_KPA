
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification, BogieChecksheet
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer
from django.utils.dateparse import parse_date
from django.db import IntegrityError


class WheelSpecificationListCreateView(APIView):
    def get(self, request):
        form_number = request.query_params.get('formNumber')
        submitted_by = request.query_params.get('submittedBy')
        submitted_date = request.query_params.get('submittedDate')

        filters = {}
        if form_number:
            filters['formNumber'] = form_number  # Filter by form number if provided
        if submitted_by:
            filters['submittedBy'] = submitted_by  # Filter by submitter if provided
        if submitted_date:
            filters['submittedDate'] = parse_date(submitted_date)  # Parse and filter by date

        queryset = WheelSpecification.objects.filter(**filters)
        if not queryset.exists():
            return Response({
                'success': False,
                'message': 'No data found for the given filters.',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            'success': True,
            'message': 'Filtered wheel specification forms fetched successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                instance = serializer.save()
            except IntegrityError:
                form_number = request.data.get('formNumber')
                return Response({
                    'success': False,
                    'message': f'A form with this formNumber ({form_number}) already exists.',
                    'errors': {'formNumber': [f'This formNumber ({form_number}) already exists.']}
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'success': True,
                'message': 'Wheel specification submitted successfully.',
                'data': {
                    'formNumber': instance.formNumber,
                    'submittedBy': instance.submittedBy,
                    'submittedDate': str(instance.submittedDate),
                    'status': 'Saved'
                }
            }, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': 'Validation failed.', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BogieChecksheetListCreateView(APIView):
    def get(self, request):
        form_number = request.query_params.get('formNumber')
        inspection_by = request.query_params.get('inspectionBy')
        inspection_date = request.query_params.get('inspectionDate')

        filters = {}
        if form_number:
            filters['formNumber'] = form_number  # Filter by form number if provided
        if inspection_by:
            filters['inspectionBy'] = inspection_by  # Filter by inspector if provided
        if inspection_date:
            filters['inspectionDate'] = parse_date(inspection_date)  # Parse and filter by date

        queryset = BogieChecksheet.objects.filter(**filters)
        if not queryset.exists():
            return Response({
                'success': False,
                'message': 'No data found for the given filters.',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = BogieChecksheetSerializer(queryset, many=True)
        return Response({
            'success': True,
            'message': 'Filtered bogie checksheet forms fetched successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            try:
                instance = serializer.save()
            except IntegrityError:
                form_number = request.data.get('formNumber')
                return Response({
                    'success': False,
                    'message': f'A form with this formNumber ({form_number}) already exists.',
                    'errors': {'formNumber': [f'This formNumber ({form_number}) already exists.']}
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'success': True,
                'message': 'Bogie checksheet submitted successfully.',
                'data': {
                    'formNumber': instance.formNumber,
                    'inspectionBy': instance.inspectionBy,
                    'inspectionDate': str(instance.inspectionDate),
                    'status': 'Saved'
                }
            }, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': 'Validation failed.', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
