from todofield import models
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker

class TodoFieldForm(ModelForm):
    class Meta:
        model = models.TodoField
        fields = ['text', 'deadline']
        widgets = {
                'deadline': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                    "pickseconds": False})
        }
