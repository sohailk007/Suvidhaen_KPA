from django.contrib import admin
from wheel.models import WheelSpecification, BogieChecksheet

# Register your models here.

@admin.register(WheelSpecification)
class wheeladmin(admin.ModelAdmin):
    list_display = ['formNumber','submittedBy','submittedDate']

@admin.register(BogieChecksheet)
class BogieAdmin(admin.ModelAdmin):
    list_display = ['formNumber','inspectionBy','inspectionDate']

