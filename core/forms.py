from django import forms
from django.core.validators import RegexValidator
from .models import UserProfile

class UploadHwForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

class RegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Your Name',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'
        })
    )
    
    mobile_no = forms.CharField(
        max_length=11,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^01\d{9}$',
                message="Invalid Mobile No"
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': '01XXXXXXXXX',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'
        })
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'
        })
    )

class LoginForm(forms.Form):
    mobile_no = forms.CharField(
            max_length=11,
            required=True,
            validators=[
                RegexValidator(
                    regex=r'^01\d{9}$',
                    message="Invalid Mobile No"
            )],
            widget = forms.TextInput(attrs={
                'placeholder' : '01XXXXXXXXX',
                'class' : 'shadow-sm rounded-md w-full px-3 py-2 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
    }))

    password = forms.CharField(
            required=True, 
            widget = forms.PasswordInput(attrs={
                'class' : 'shadow-sm rounded-md w-full px-3 py-2 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
    }))  

class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )

class ExamForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

    start_time = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    duration = forms.DurationField(
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'in minutes',
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

    student = forms.ChoiceField(
        choices=[('', 'Select')] + [(d.id, f'{d.name} {d.user}') for d in UserProfile.objects.filter(role='user').all()],
        required=True,
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md min-h-10 border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'id': 'division'
        })
    )

class ExamEditForm(forms.Form):
    start_time = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    duration = forms.DurationField(
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'in minutes',
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

    student = forms.ChoiceField(
        choices=[('', 'Select')] + [(d.id, f'{d.name} {d.user}') for d in UserProfile.objects.filter(role='user').all()],
        required=True,
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md min-h-10 border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'id': 'division'
        })
    )

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('okay', 'Okay'),
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

    delete_existing_file = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mt-1 mr-2'
        }),
        label="Delete existing file?"
    )

    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50'
        })
    )

