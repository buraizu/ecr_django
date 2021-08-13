from django.forms import ModelForm
from .models import Run

class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = ['course', 'review', 'rating', 'distance', 'time']