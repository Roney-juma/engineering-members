from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Member created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        member = self.get_object()
        serializer = self.get_serializer(member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Member updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        member = self.get_object()
        member.delete()
        return Response({
            "message": "Member deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
