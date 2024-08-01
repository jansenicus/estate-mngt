"""
users.forms
"""

from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import get_user_model

User = get_user_model()


class UserChangeForm(BaseUserChangeForm):
    """
    customization of BaseUserChangeForm
    """

    class Meta(BaseUserChangeForm.Meta):
        """BaseUserChangeForm.Meta"""

        model = User
        fields = ["first_name", "last_name", "username", "email"]


class UserCreationForm(BaseUserCreationForm):
    """
    user creation form customization
    """

    class Meta(BaseUserCreationForm.Meta):
        """UserCreationForm.Meta"""

        model = User
        fields = ["first_name", "last_name", "username", "email"]

    error_messages = {
        "duplicate_username": "A user with that usernama already exists.",
        "duplicate_email": "A user with that email already exists.",
    }

    def clean_email(self) -> str:
        """
        to ensure that we have clean unique email
        """
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages["duplicate_email"])

        return email

    def clean_username(self) -> str:
        """
        to ensure that we have clean unique username
        """
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(self.error_messages["duplicate_username"])
        return username
