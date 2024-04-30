from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Copropriete, CommonKey, PrivateKey, TrackCommon, TrackPrivate, Agency
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

#List
class CommonKeyListSerializer(ModelSerializer):
    class Meta:
        model = CommonKey
        fields = ['name','acces','image','qr_code','id_Copro','id_Agency','id', 'available']
        validators = [
            UniqueTogetherValidator(
                queryset =CommonKey.objects.all(),
                fields =['name','id_Copro','id_Agency'],
                message = "Ce trousseau existe déjà"
            )
        ]
    def validate(self, attrs):
        id_agency_key = attrs.get('id_Agency')
        id_copro_key = attrs.get('id_Copro')

        if id_copro_key.id_Agency != id_agency_key:
            raise serializers.ValidationError("la copropriété choisie n'appartient pas à la même agence que la clé")
        return attrs
    
    def create(self, validated_data):
        instance = CommonKey.objects.create(**validated_data)
        instance.qr_code = f'https://trackey.fr/Copropriete/CommonKey/track/{instance.id}/'
        instance.save()
        return instance

class PrivateKeyListSerializer(ModelSerializer):
    class Meta:
        model = PrivateKey
        fields = ['name','acces','image','qr_code','id_Copro','id_Agency', 'id', 'available']
        validators = [
            UniqueTogetherValidator(
                queryset =PrivateKey.objects.all(),
                fields =['name','id_Copro','id_Agency'],
                message = "Ce trousseau existe déjà"
            )
        ]
    def validate(self, attrs):
        id_agency_key = attrs.get('id_Agency')
        id_copro_key = attrs.get('id_Copro')

        if id_copro_key.id_Agency != id_agency_key:
            raise serializers.ValidationError("la copropriété choisie n'appartient pas à la même agence que la clé")
        return attrs
    
    def create(self, validated_data):
        instance = PrivateKey.objects.create(**validated_data)
        instance.qr_code = f'https://trackey.fr/Copropriete/PrivateKey/track/{instance.id}/'
        instance.save()
        return instance

class CoproprieteListSerializer(ModelSerializer):
    class Meta: 
        model = Copropriete
        fields = ['Numero','name','adresse','id_Agency', 'id']
        validators = [
            UniqueTogetherValidator(
                queryset=Copropriete.objects.all(),
                fields = ["Numero", 'id_Agency'],
                message = "Ce numéro de copropriété existe déjà"
            )
        ]


#Detail 
class TrackCommonSerializer(ModelSerializer):
    class Meta:
        model = TrackCommon
        fields = ['id_key','entreprise','tel','depart','retour', 'notes','id']

class TrackPrivateSerializer(ModelSerializer):
    class Meta:
        model = TrackPrivate
        fields = ['id_key','entreprise','tel','depart','retour','notes','id']

class CommonKeySerializer(ModelSerializer):
    trackcommon_set = TrackCommonSerializer(many=True)
    class Meta:
        model = CommonKey
        fields = ['name','acces','image','qr_code','id_Copro','trackcommon_set','id', 'available']
    

class PrivateKeySerializer(ModelSerializer):
    trackprivate_set = TrackPrivateSerializer(many=True)
    class Meta:
        model = PrivateKey
        fields = ['name','acces','image','qr_code','id_Copro','trackprivate_set','id', 'available']

class CoproprieteSerializer(ModelSerializer):
    commonkey_set = CommonKeySerializer(many=True)
    privatekey_set = PrivateKeySerializer(many=True)
    class Meta:
        model = Copropriete
        fields = ['Numero','name','adresse','id_Agency','commonkey_set', 'privatekey_set','id']

#Account
class AgencySerializer(ModelSerializer):
    class Meta:
        model = Agency
        fields = ['Name', 'Adresse', 'email', 'email_verif']
        extra_kwargs = {'password': {'write_only':True}}

    
class AgencyCreateSerialier(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Agency 
        fields = ['Name', 'Adresse', 'password','email', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value): 
            raise serializers.ValidationError("Ancien Mot de passe incorrect")
        return value
    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Mauvais MP de confirmation")
        return attrs
    

class MPOubliePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Mauvais MP de confirmation")
        return attrs


