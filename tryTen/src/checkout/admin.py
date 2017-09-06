from django.contrib import admin
from .models import profile, userStripe

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, ProfileAdmin)

class UserStripeAdmin(admin.ModelAdmin):
    class meta:
        model = userStripe

admin.site.register(userStripe, UserStripeAdmin)