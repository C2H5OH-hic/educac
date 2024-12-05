from django import forms
from .models import Usuario

class RegistroUsuarioAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super(RegistroUsuarioAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
