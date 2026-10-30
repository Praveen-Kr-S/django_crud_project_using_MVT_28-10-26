from .models import StudentData
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model=StudentData
        fields = "__all__"