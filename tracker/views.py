from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Entry
from .serializers import EntrySerializer
# Create your views here.

class EntryListCreateView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print("Saving entry for:", self.request.user)
        serializer.save(user=self.request.user)

class EntryDeleteView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
