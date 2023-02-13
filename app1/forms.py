from .models import Profile

from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['profile_photo','cover_photo','intro','education','hometown','work']