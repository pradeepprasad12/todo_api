from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    