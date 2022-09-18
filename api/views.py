import json
from threading import Thread
from unittest import result
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import BatchRunModel
from api.serializers import BatchRunSerializer

import requests

from api.utils import fetch_and_store_keywords

# Create your views here.




class BatchRunViewset(viewsets.ModelViewSet):

    queryset = BatchRunModel.objects.all().order_by("-created_at")
    serializer_class = BatchRunSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if(self.request.user.is_anonymous): return [];

        return BatchRunModel.objects.filter(owner=self.request.user)


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        # Adding results here   

        data['results'] = []
        # print("------------------------------" + request.user)
        if(request.user.id): data['owner'] = request.user

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        Thread(target=fetch_and_store_keywords, args=(json.loads(data['queries']), serializer.data["id"])).start();

        return Response(serializer.data, headers=headers)