from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password1', 'password2'
        ]
        labels = {
            'username' : 'Correo electrónico',
            'first_name' : 'Nombres',
            'Last_name' : 'Apellidos',    
        }
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': 'Ej: tucorreo@dominio.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ej: Juan Pedro'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ej: Pérez Machuca'}),
            'contraseña': forms.PasswordInput(attrs={'placeholder': 'Clave secreta'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repite la clave secreta'})
        }

        help_texts = {
            'username' : 'Debe contener letras, números y @.',
            'password1': 'Personaliza el texto de ayuda para la primera contraseña aquí.',
            'password2': 'Personaliza el texto de ayuda para la segunda contraseña aquí.',
        }
#         Su contraseña no puede asemejarse tanto a su otra información personal.
# Su contraseña debe contener al menos 8 caracteres.
# Su contraseña no puede ser una clave utilizada comúnmente.
# Su contraseña no puede ser completamente numérica.