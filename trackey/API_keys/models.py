from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, Name, Adresse, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            Name = Name, 
            Adresse = Adresse,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, Name, Adresse, password=None):
        superuser = self.model(
            email=self.normalize_email(email),
            Name = Name, 
            Adresse = Adresse,
        )
        superuser.is_staff = True
        superuser.set_password(password)
        superuser.save(using = self._db)
        return superuser

class Agency(AbstractBaseUser): 
    Name = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    id = models.CharField(max_length=200, default=uuid.uuid4, unique=True, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)

    email_verif = models.BooleanField(default=False)
    #OTP
    otp = models.IntegerField(blank=True, null=True)
    otp_create = models.DateTimeField(blank=True, null=True)
    otp_valid_date = models.DateTimeField(blank=True, null=True)
    #MP oublié
    token = models.CharField(max_length=200, blank=True, null=True)
    date_token = models.DateTimeField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Adresse', 'Name']
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj = None):
        if self.is_staff:
            return True
    
    def has_module_perms(self, app_label):
        if self.is_staff:
            return True
        
    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name

class Copropriete(models.Model):
    Numero = models.IntegerField()
    name = models.TextField(max_length=20)
    adresse = models.TextField()
    id_Agency = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Numero) + '__/__' + self.name + '__/__:' + str(self.id_Agency)
    
    class Meta:
        ordering = ['id']

    
class CommonKey(models.Model): 
    name = models.TextField()
    acces = models.TextField(max_length=36)
    image = models.ImageField(upload_to = 'key_images/')
    qr_code = models.TextField(blank = True, null = True)
    available = models.BooleanField(default=True)
    id_Agency = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_Copro = models.ForeignKey(Copropriete, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '__/__' + str(self.id_Copro)
    
    class Meta:
        ordering = ['name']

class PrivateKey(models.Model): 
    name = models.TextField()
    acces = models.TextField(max_length=27)
    image = models.ImageField(upload_to = 'key_images/')
    qr_code = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    id_Agency = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_Copro = models.ForeignKey(Copropriete, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name + '__/__' + str(self.id_Copro)
    
    class Meta:
        ordering = ['name']

class TrackCommon(models.Model):
    id_key = models.ForeignKey(CommonKey, on_delete=models.CASCADE)
    id_Agency = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entreprise = models.TextField(max_length=30)
    tel = models.IntegerField()
    depart = models.DateTimeField(auto_now_add=True)
    retour = models.DateTimeField(blank=True, null=True) 
    notes = models.TextField(blank=True, null=True)

    @transaction.atomic
    def disable(self):
        if self.retour is not None:
            self.id_key.available=True
            self.id_key.save()
        elif self.retour is None:
            self.id_key.available=False
            self.id_key.save()

    def __str__(self):
        return self.entreprise + '__/__' + str(self.id_key)

    class Meta: 
        ordering = ['-depart']

class TrackPrivate(models.Model):
    id_key = models.ForeignKey(PrivateKey, on_delete=models.CASCADE)
    id_Agency = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entreprise = models.TextField(max_length=30)
    tel = models.IntegerField()
    depart = models.DateTimeField(auto_now_add=True)
    retour = models.DateTimeField(blank=True, null=True) 
    notes = models.TextField(blank=True, null=True)

    @transaction.atomic
    def disable(self):
        if self.retour is not None:
            self.id_key.available=True
            self.id_key.save()
        elif self.retour is None:
            self.id_key.available=False
            self.id_key.save()

    def __str__(self):
        return self.entreprise + '__/__' + str(self.id_key)
    
    class Meta: 
        ordering = ['-depart']

