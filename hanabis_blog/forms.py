from django import forms
from .models import Reviews, Post
from bootstrap_datepicker.widgets import DatePicker
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class ReviewForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'date_pub', 'recaptcha')
        widgets = {
            'name':forms.TextInput(attrs={"class":"form-field full-width", "placeholder":"Your Name", "id":"cNmae", "name":"name", }),
            'email':forms.EmailInput(attrs={"class":"form-field full-width","placeholder":"Your Email", "id":"cEmail", "name":"email"}),
            'text':forms.Textarea(attrs={"class":"form-field full-width", "placeholder":"Your Message", "id":"cMessage", "name":"message"}),

        }
