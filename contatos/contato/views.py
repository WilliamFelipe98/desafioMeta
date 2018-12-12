from django.shortcuts import render

from rest_framework import generics
from .models import Contato
from .serializer import ContatoSerializer
from rest_framework.permissions import IsAuthenticated

class ContatoList(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = (IsAuthenticated,)

class ContatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = (IsAuthenticated,)
