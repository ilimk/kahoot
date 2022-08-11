from rest_framework import generics, viewsets
from .models import User, Group, Test, Question, Answer, UserAnswer
from .serializers import UserSerializer, GroupSerializer, TestSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from kahootApi.permissions import IsAdminReadOnly, IsOwnerOrReadOnly

class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

class UserAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminReadOnly, )