from django.forms import fields
from django import forms
from .models import Ville, Type_eau, Client, Profil, User, Info_livraison

       
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['nomprofil']


class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = '__all__'


class Type_eauForm(forms.ModelForm):
    
    class Meta:
        model = Type_eau
        fields = '__all__'
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class Info_livvraisonForm(forms.ModelForm):
    class Meta:
        model = Info_livraison
        fields = '__all__'                        