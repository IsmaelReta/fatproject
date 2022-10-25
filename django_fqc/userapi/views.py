from rest_framework import viewsets
from rest_framework import viewsets, status, mixins
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserFullSerializer
from rest_framework.response import Response

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user


    def update(self, request, *args, **kwargs):
        user = self.request.user
        user_object = self.get_object()
        if user == user_object:
            data = request.data


            user_object.username = data['username']   
            user_object.first_name = data['first_name']   
            user_object.last_name = data['last_name']      
            user_object.email = data['email']      
            user_object.password = data['password']      


            user_object.save()

            serializer = UserSerializer(user_object)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

    

#*Returns all user data, including patient data
class UserFullViewSet(mixins.RetrieveModelMixin, 
                   mixins.DestroyModelMixin, 
                   viewsets.GenericViewSet):
    serializer_class = UserFullSerializer
    
    
    def get_queryset(self):
        user = User.objects.all()
        return user



    def list(self, request):
        user_state = request.user.is_superuser
        if user_state == True:
            user = User.objects.all()
            serializer = UserFullSerializer(user, many = True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'Authorization Required'}, status=status.HTTP_401_UNAUTHORIZED)



    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        u_id = params['pk']
        user_state =self.request.user.is_superuser
        if user_state == False:
            current_user = self.request.user.id
            if int(current_user) == int(u_id):
                user = User.objects.filter(id=u_id)
                serializer = UserFullSerializer(user, many=True)
                return Response(serializer.data)
            else:
                return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user = User.objects.filter(id=u_id)
            serializer = UserFullSerializer(user, many=True)
            return Response(serializer.data)


#!en caso de usarse hacen falta todos los otros campos
    # def update(self, request, *args, **kwargs):
    #     user = self.request.user
    #     user_object = self.get_object()
    #     if user == user_object:
    #         data = request.data


    #         user_object.username = data['username']   
    #         user_object.first_name = data['first_name']   
    #         user_object.last_name = data['last_name']      
    #         user_object.email = data['email']      
    #         user_object.password = data['password']      


    #         user_object.save()

    #         serializer = UserFullSerializer(user_object)
    #         return Response(serializer.data)
    #     else:
    #         return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
