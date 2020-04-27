from allauth.socialaccount.models import SocialAccount
from django import forms
from .models import Reviews, Post
from bootstrap_datepicker.widgets import DatePicker
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):


    recaptcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ('text', 'email', 'name', 'recaptcha', 'username')
        widgets = {

            'text':forms.Textarea(attrs={"class":"form-control", "placeholder":"Your Message", "id":"message", "name":"text", 'cols':"30", 'rows':"10"}),
        }
