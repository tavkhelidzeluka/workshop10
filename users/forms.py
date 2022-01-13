from django import forms
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=255, validators=[validate_password], widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def is_valid(self) -> bool:
        
        if self.data['password2'] != self.data['password']:
            self.errors['password'] = ('Passwords do not match!', )
            self.errors['password2'] = ('Passwords do not match!', )

        return super().is_valid()
    
    def save(self, commit: bool = ...):
        user = super().save(False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user
