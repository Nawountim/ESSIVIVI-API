from rest_framework import serializers
from .models import Ville, Type_eau, Client, Profil, User, Info_livraison

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['nomprofil']
        
class Type_eauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_eau
        fields = ['libelle','pu','qte','qte_seuil']        

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ['nomville']
             
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nom','prenom','email','password','contact','idpro'] 
        
class Info_livr_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Info_livraison
        fields = ['qte_livr','montant','bonus','idcli','ideau','idcom']
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        #fields = '__all__'
        fields = ['nom','prenom','contact','adresse','longitude','latitude','sexe','created_by','statut','idVille'] 
        
