from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class viewapi(APIView):

    def get(self, request)

        return "hoi"
