# mywebsite/mainapp/forms.py
from django import forms
from .models import QuizSubmission

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizSubmission
        fields = '__all__'
        exclude = ['ai_report', 'created_at'] # Exclude fields not in the form

    # You can customize widgets here for a better front-end appearance
    # This example assumes you have Tailwind CSS classes for styling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['energy_level', 'stress_level']:
                field.widget.attrs.update({'class': 'mt-2 w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-purple-600'})

                # mywebsite/mainapp/forms.py
from django import forms
from .models import QuizSubmission

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizSubmission
        fields = '__all__'
        exclude = ['ai_report', 'created_at']

    # Customize widgets for a better front-end appearance
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['energy_level', 'stress_level', 'work_schedule']:
                field.widget.attrs.update({'class': 'mt-2 w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-purple-600'})
            if field_name in ['dietary_habits', 'medication']:
                field.widget.attrs.update({'rows': 3})
        
        # Add choices for new fields
        self.fields['work_schedule'].widget = forms.RadioSelect(choices=[
            ('regular', 'Regular (9-5)'),
            ('shift', 'Shift work'),
            ('irregular', 'Irregular hours'),
            ('wfh', 'Work from home')
        ])
        
        self.fields['energy_level'].widget = forms.RadioSelect(choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ])
        
        self.fields['stress_level'].widget = forms.RadioSelect(choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ])

        # mywebsite/mainapp/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-2 w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-purple-600'
            })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-2 w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-purple-600'
            })