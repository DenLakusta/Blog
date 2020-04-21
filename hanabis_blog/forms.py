from django import forms
from .models import Reviews, Post
from bootstrap_datepicker.widgets import DatePicker




class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'date_pub')

