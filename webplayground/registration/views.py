from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
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


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self, queryset=None):
        # Recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self, queryset=None):
        # Recuperar el objeto que se va a editar
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(EmailUpdate, self).get_context_data(**kwargs)
        # Modificar en tiempo real
        form = context['form']
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control , mt-2',
            'placeholder': 'Email'
        })
        return context
