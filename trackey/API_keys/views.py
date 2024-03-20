from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CoproprieteSerializer, CoproprieteListSerializer, CommonKeySerializer,CommonKeyListSerializer, PrivateKeySerializer,PrivateKeyListSerializer, TrackCommonSerializer, TrackPrivateSerializer, AgencySerializer, ChangePasswordSerializer, AgencyCreateSerialier, AccountSerializer
from .models import Copropriete, CommonKey, PrivateKey, TrackCommon, TrackPrivate, Agency
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, exceptions
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime




@api_view(['GET'])
def getRoutes(request):
    routes =[
        {
            'Endpoint':'/api/SuperUser/id/PUT/',
            'method':'PUT',
            'body': None,
            'description': 'SuperUser Can Modify SuperUser',
        },
        {
            'Endpoint':'/api/SuperUser/id/User/GET/',
            'method':'GET',
            'body': None,
            'description': 'SuperUser Can GET Users',
        },
        {
            'Endpoint':'/api/SuperUser/id/User/POST/',
            'method':'POST',
            'body': None,
            'description': 'SuperUser Can Create User',
        },
        {
            'Endpoint':'/api/SuperUser/id/User/id/DELETE/',
            'method':'DELETE',
            'body': None,
            'description': 'SuperUser Can DELETE User',
        },
        {
            'Endpoint':'/api/SuperUser/id/User/id/PUT/',
            'method':'PUT',
            'body': None,
            'description': 'SuperUser Can Modify User',
        },
        {
            'Endpoint':'/api/User/id/PUT/',
            'method':'PUT',
            'body': None,
            'description': 'User Can Modify User',
        },
        {
            'Endpoint':'/api/Copropriétés/',
            'method':'GET',
            'body': None,
            'description': 'Get all Copropriétés of agency',
        },
        {
            'Endpoint':'/api/Copropriétés/POST/',
            'method':'POST',
            'body': None,
            'description': 'Create Copropriété in agency',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PUT/',
            'method':'PUT',
            'body': None,
            'description': 'Modify one Copropriété of agency',
        },
        {
            'Endpoint':'/api/Copropriétés/id/DELETE/',
            'method':'DELETE',
            'body': None,
            'description': 'Remove one Copropriété of agency',
        },
        {
            'Endpoint':'/api/Copropriétés/id/',
            'method':'GET',
            'body': None,
            'description': 'GET all informations about one Copropriété in agency',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys',
            'method':'GET',
            'body': None,
            'description': 'GET a list of all common keys for one copropriete',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys',
            'method':'GET',
            'body': None,
            'description': 'GET a list of all private keys for one copropriete',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/',
            'method':'GET',
            'body': None,
            'description': 'GET all information about common keys',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/',
            'method':'POST',
            'body': None,
            'description': 'Create common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/',
            'method':'PUT',
            'body': None,
            'description': 'Modify common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/',
            'method':'DELETE',
            'body': None,
            'description': 'Remove common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/Track',
            'method':'Get',
            'body': None,
            'description': 'GET track about this common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/Track',
            'method':'POST',
            'body': None,
            'description': 'POST new track about this common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/CommonKeys/id/Track',
            'method':'PUT',
            'body': None,
            'description': 'Modify one track about this common key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/',
            'method':'POST',
            'body': None,
            'description': 'Create private key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/id/',
            'method':'PUT',
            'body': None,
            'description': 'Modify private key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/id/',
            'method':'DELETE',
            'body': None,
            'description': 'Remove private key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/id/Track',
            'method':'Get',
            'body': None,
            'description': 'GET track about this private key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/id/Track',
            'method':'POST',
            'body': None,
            'description': 'Create new track about this private key',
        },
        {
            'Endpoint':'/api/Copropriétés/id/PrivateKeys/id/Track',
            'method':'PUT',
            'body': None,
            'description': 'Modify one track about this private key',
        },
    ]
    return Response(routes)


class CoproprieteViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CoproprieteListSerializer
    detail_serializer_class = CoproprieteSerializer

    def get_queryset(self):
        return Copropriete.objects.filter(id_Agency = self.request.user)

    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()



class CommonKeyViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommonKeyListSerializer
    detail_serializer_class = CommonKeySerializer

    #Je pense que commonkey en listing pour toutes les copro ca me sert à rien par contre une listclés par copro ca me sert à quelque chose 
    def get_queryset(self):
        id_Copro = self.request.GET.get('id_Copro')
        queryset = CommonKey.objects.filter(id_Agency = self.request.user)
        if id_Copro is not None: 
            queryset = queryset.filter(id_Copro=id_Copro)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

class PrivateKeyViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PrivateKeyListSerializer
    detail_serializer_class = PrivateKeySerializer

    def get_queryset(self):
        id_Copro = self.request.GET.get('id_Copro')
        queryset = PrivateKey.objects.filter(id_Agency = self.request.user)
        if id_Copro is not None:
            queryset = queryset.filter(id_Copro=id_Copro)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class TrackCommonViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TrackCommonSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save(id_Agency = self.request.user)
        instance.disable()

    def perform_update(self, serializer):
        instance = serializer.save(id_Agency = self.request.user)
        instance.disable()

    def get_queryset(self):
        id_key = self.request.GET.get('id_key')
        queryset = TrackCommon.objects.filter(id_Agency = self.request.user)
        if id_key is not None:
            queryset = queryset.filter(id_key=id_key)
        return queryset
    
class TrackPrivateViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TrackPrivateSerializer

    def perform_create(self, serializer):
        instance = serializer.save(id_Agency = self.request.user)
        instance.disable()

    def perform_update(self, serializer):
        instance = serializer.save(id_Agency = self.request.user)
        instance.disable()

    def get_queryset(self):
        id_key = self.request.GET.get('id_key')
        queryset = TrackPrivate.objects.filter(id_Agency = self.request.user)
        if id_key is not None: 
            queryset = queryset.filter(id_key=id_key)
        return queryset

#user 
class AgencyUpdateView(generics.UpdateAPIView): 
    permission_classes = [IsAuthenticated]
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


    def get_object(self):
        serializer = AgencySerializer(data=request.data, context={'request': request})
        return self.request.user


class AgencyCreateView(generics.ListCreateAPIView):
    serializer_class = AgencyCreateSerialier

    def get_queryset(self): 
        user = self.request.user
        queryset=Agency.objects.filter(id = user.id)
        return queryset
    
    def post(self, request):
        serializer = AgencyCreateSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChangePasswordView(views.APIView): 
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAccount(request):
    Agency_id = request.GET.get('id')
    Agency = Agency.objects.filter(id=Agency_id)
    serializer = AgencySerializer(Agency, many=False)
    return Response(serializer.data)

#track key update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUpdateCommonTracKey(request, key_id):
    try:
        key = CommonKey.objects.filter(id=key_id, agency=request.user.agency).first()
        if key is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if key.available: 
            print('redirigé')
            return Response({'id_key': key.id},status=status.HTTP_307_TEMPORARY_REDIRECT)
        else: 
            tracks = key.trackcommon_set.all()
            print({tracks})
            for track in tracks:
                print({track.retour})
                if track.retour is None:
                    track.retour = datetime.now().astimezone()
                    track.save()
                    key.available = True
                    key.save()
                    print('available True')
                    break
            return Response(status=status.HTTP_202_ACCEPTED)
    except CommonKey.DoesNotExist:
        print('error')
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUpdatePrivateTracKey(request, key_id):
    try:
        key = PrivateKey.objects.filter(id=key_id, agency=request.user.agency).first()
        if key is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if key.available: 
            return Response({'id_key': key.id},status=status.HTTP_307_TEMPORARY_REDIRECT)
        else: 
            tracks = key.trackprivate_set.all()
            print({tracks})
            for track in tracks:
                print({track.retour})
                if track.retour is None:
                    track.retour = datetime.now().astimezone()
                    track.save()
                    key.available = True
                    key.save()
                    break
            return Response(status=status.HTTP_202_ACCEPTED)
    except PrivateKey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)