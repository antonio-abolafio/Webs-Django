from .forms import UserCretionFormWithEmail
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCretionFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar widgets
        form.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Nombre de usuario',
            'class': 'form-control',
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Dirección de email',
            'class': 'form-control',
        })

        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control',
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Repite la contraseña',
            'class': 'form-control',
        })
        return form
