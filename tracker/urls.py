from django.urls import path
from .views import EntryListCreateView, EntryDeleteView, register_user

urlpatterns = [
    path('entries/', EntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', EntryDeleteView.as_view(), name='entry-delete'),
    path('register/', register_user, name='register'),
]
