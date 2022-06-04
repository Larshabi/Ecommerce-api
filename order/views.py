from django.shortcuts import render
from django.conf import Settings
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import  authentication, permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Order, OrderItem
from .serializers import OrderSerializer