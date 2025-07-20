from django.urls import path
from .views import WheelSpecificationListCreateView, BogieChecksheetListCreateView

urlpatterns = [
    path('forms/wheel-specification/', WheelSpecificationListCreateView.as_view(), name='wheel-specification-list-create'),
    path('forms/bogie-checksheet/', BogieChecksheetListCreateView.as_view(), name='bogie-checksheet-list-create'),
] 