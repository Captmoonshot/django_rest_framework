# api/views.py

from django.shortcuts import render

# Create your views here.
# Django REST Framework's built-in generic class views...deliberately mimic traditional 
# Django's generic class-based views in format, but they are
# NOT the same thing

from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	