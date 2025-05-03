from django.urls import path
from .views import EntryListCreateView, EntryDeleteView

urlpatterns = [
    path('entries/', EntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', EntryDeleteView.as_view(), name='entry-delete'),
]
