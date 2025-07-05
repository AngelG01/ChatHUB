from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ChatHUB.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'username', 'profile_picture', 'bio', 'date_of_birth')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
