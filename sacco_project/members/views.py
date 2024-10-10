from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.db.models import Q 
from .models import Member
from .serializers import LoginSerializer, MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(full_name__icontains=search) |
                Q(email__icontains=search) |
                Q(username__icontains=search)
            )
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Member created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

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


class MemberLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({
            "message": "Login successful",
            "user_id": user.id
        }, status=status.HTTP_200_OK)
