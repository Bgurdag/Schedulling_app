from django import forms
from.models import Event
#creating form for homepage to input events
class ScheduleFrom(forms.ModelForm):
    # eventname = forms.CharField(max_length=200)
    # start_date_time = forms.DateTimeField()
    # end_date_time = forms.DateTimeField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date_time'].widget = forms.widgets.DateInput(attrs= {
            'type': 'date' , 'placeholder' : 'yyyy-mm-dd',
            'class' : 'form-control'
        })

    class Meta:
        model = Event
        fields = '__all__'


