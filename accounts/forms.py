from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustonUserCreationForm(UserCreationForm):
    """Extends the UserCreationForm and create new forms,
    the password field is implicitly included by default
    """
    class Meta:
        model = get_user_model()  # looks into AUTH_USER_MODEL cofig in settings
        fields = ("email", "username",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username",)