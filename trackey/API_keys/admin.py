from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Create new agency only by admin access
from .models import Agency,Copropriete,CommonKey,PrivateKey,TrackCommon,TrackPrivate
admin.site.register(Agency)
admin.site.register(Copropriete)
admin.site.register(CommonKey)
admin.site.register(PrivateKey)
admin.site.register(TrackCommon)
admin.site.register(TrackPrivate)