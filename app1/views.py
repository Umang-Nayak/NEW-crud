import logging
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializers
from django_filters.rest_framework import DjangoFilterBackend
from .utils import success_false_response, success_true_response


# Configure logging
logger = logging.getLogger("app1.views")


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['e_name', 'e_post', 'e_contact', 'e_email', 'e_salary', 'e_address', 'e_city']
    filterset_fields = ['e_post', 'e_salary', 'e_city']

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(success_true_response(
                    message='Employee Details Retrieved Successfully',
                    data=serializer.data
                ))

            serializer = self.get_serializer(queryset, many=True)
            return Response(success_true_response(
                message='Employee Details Retrieved Successfully',
                data=serializer.data
            ))
        except Exception as e:
            logger.error(f"An error occurred during listing: {e}")  # Log error message
            return Response(success_false_response(
                message='Failed To Retrieve Employee Details',
                data={'error': str(e)}
            ), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            logger.info('Employee Details Added Successfully')  # Log info message
            return Response(success_true_response(message='Employee Details Added Successfully',
                                                  data={"Success": serializer.data},))
        except Exception as e:
            logger.error(f"An error occurred during creation: {e}")  # Log error message
            return Response(success_false_response(message='Failed To Add Employee Details',
                                                   data={'error': str(e)}), status=400)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            logger.info('Employee Details Updated Successfully')  # Log info message
            return Response(success_true_response(message='Employee Details Updated Successfully',
                                                  data={"Success": serializer.data}))
        except Exception as e:
            logger.error(f"An error occurred during update: {e}")  # Log error message
            return Response(success_false_response(message='Failed To Update Employee Details',
                                                   data={'error': str(e)}), status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            logger.info('Employee Details Deleted Successfully')  # Log info message
            return Response(success_true_response(message='Employee Details Deleted Successfully'))
        except Exception as e:
            logger.error(f"An error occurred during deletion: {e}")  # Log error message
            return Response(success_false_response(message='Failed To Delete Employee Details',
                                                   data={'error': str(e)}), status=400)
