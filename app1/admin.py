from django.contrib import admin
from app1.models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'e_name', 'e_post', 'e_contact', 'e_email', 'e_salary', 'e_address', 'e_city']
