from django.forms import ModelForm
from .models import User,Carro,Moto

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nome','idade','cpf']

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['tituloCarro','precoCarro','anoCarro','tituloCarro','marcaCarro','combustivelCarro','tipoCarro']

class MotoForm(ModelForm):
    class Meta:
        model = Moto
        fields = ['tituloMoto','precoMoto','anoMoto','marcaMoto','combustivelMoto','tipoMoto']
