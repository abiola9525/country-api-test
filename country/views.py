from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import status
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from country.models import Country
from django.http import Http404, HttpResponseForbidden
from .serializers import CountrySerializer

@swagger_auto_schema(method='POST', request_body=CountrySerializer)
@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        country_list = Country.objects.all()
        serializer = CountrySerializer(country_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='PUT', request_body=CountrySerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, pk):
    try:
        country_detail = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
