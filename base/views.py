import datetime
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from . serializer import MemberSerializer
from . models import Member

# Create your views here.
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):         
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
          
class HomeView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)

# list  members
class Members(generics.GenericAPIView):
    serializers_class = MemberSerializer
    queryset = Member.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"member": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# member single
class MemberDetail(generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = Member

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        member = self.get_member(pk=pk)
        if member == None:
            return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(member)
        return Response({"status": "success", "data": {"Member": serializer.data}})
    
    def patch(self, request, pk):
        member = self.get_member(pk)
        if member == None:
            return Response({"status": "fail", "message": f"member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validate_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status":"success", "data":{"member": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        member = self.get_member(pk)
        if member == None:
            return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)