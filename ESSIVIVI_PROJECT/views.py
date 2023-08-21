from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ClientForm, UserForm, Type_eauForm, Info_livvraisonForm, ProfilForm, VilleForm
from .models import Client, User, Type_eau, Info_livraison, Profil, Ville
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .serializers import ProfilSerializer, VilleSerializer,Type_eauSerializer,UserSerializer,ClientSerializer,Info_livr_Serializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import ClientSerializer
from django.utils import timezone
from django.views import View
from django.db.models import Sum
from datetime import datetime
import calendar
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer





# Create your views here.


### Methode de la Table Profil ###

#Creation d'un profil un formulaire propre a django
@csrf_exempt
def createprofil(request):   
    if request.method=="POST":
        form = ProfilForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()    
            except:
                pass
        else:
            return form.errors   
    else:
        return redirect("/show_pro")      
            
# Même chose via un serializer(C'est ce que nous utiliseront)

@csrf_exempt
def Create_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = ProfilSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Profil créé"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({"Info":"Profil non créé"})
    return redirect("/show_pro")

        
 
####################

            
#Liste des profiles
def show_profile(request):
    data = { "profiles": [] }
    profiles = Profil.objects.all()
    for profil in profiles:
        data["profiles"].append({
            "id": profil.idpro,
            "nomprofil": profil.nomprofil
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)            

#Modification d'un profil
@csrf_exempt
def update_profil(request, id):
    profil = get_object_or_404(Profil, id=id)
    if request.method == 'POST':
        serializer = ProfilSerializer(profil, data=request.data)
        if serializer.is_valid():
            serializer.update(profil, request.data)
            return JsonResponse({"info": "Profil modifié"})
        return JsonResponse({"error": serializer.errors})
            


#Suppression d'un profil
@csrf_exempt
def delete_profil(request, id):
    profil = Profil.objects.get(id=id)
    profil.delete()
    
    
                                         ### Methode de la Table Ville ###    
                                         
#Creation d'une Ville via un formulaire propre a django
def Create_ville_form(request):
    if request.method=="POST":
        form =VilleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
            except:
                pass
           
# Même chose via un serializer(C'est ce que nous utiliseront)


@csrf_exempt
def Create_Ville(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = VilleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Ville créée"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({"Info":"Ville non créée"})
    return redirect("/show_ville")            
            
#Liste des Villes
def show_ville(request):
    data = { "villes": [] }
    villes = Ville.objects.all()
    for ville in villes:
        data["villes"].append({
            "id": ville.idVille,
            "nomville": ville.nomville
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)            

#Modification d'une Ville
@csrf_exempt
def update_ville(request, idVille):
    ville = get_object_or_404(Ville, idVille=idVille)
    data = json.loads(request.body)
    serializer = VilleSerializer(ville, data=data)
    if serializer.is_valid():
            serializer.update(ville, data)
            return JsonResponse({"info": "Ville modifiéé"})
    return JsonResponse({"error": serializer.errors})            


#Suppression d'une Ville
@csrf_exempt
def delete_ville(request, id):
    ville = Ville.objects.get(id=id)
    ville.delete()                                         
    
    
                                               ### Methode de la Table Type_eau ###   
                                               
#Creation d'un type d'eau via un formulaire propre a django
@csrf_exempt
def Create_eau_form(request):
    if request.method=="POST":
        form =Type_eauForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
            except:
                pass
            
# Même chose via un serializer(C'est ce que nous utiliseront)

      
@csrf_exempt
def Create_eau(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = Type_eauSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Type d'eau créé"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({"Info":"Type d'eau non créé"})
    return redirect("/show_eau")              
            
#Liste des types d'eaux
def show_eau(request):
    data = { "eaux": [] }
    eaux = Type_eau.objects.all()
    for eau in eaux:
        data["eaux"].append({
            "id": eau.id,
            "libelle": eau.libelle,
            "prix_unitaire": eau.pu,
            "Quantite": eau.qte,
            "Quantite_seuil": eau.qte_seuil
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)            

#Modification d'un type d'eau
@csrf_exempt
def update_eau(request, id):
    eau = get_object_or_404(Type_eau, id=id)
    if request.method == 'POST':
        serializer = Type_eauSerializer(eau, data=request.data)
        if serializer.is_valid():
            serializer.update(eau, request.data)
            return JsonResponse({"info": "Type d'eau modifiéé"})
        return JsonResponse({"error": serializer.errors})                  


#Suppression d'un type d'eau
@csrf_exempt
def delete_eau(request, id):
    eau = Type_eau.objects.get(id=id)
    eau.delete()                                                   
    
    
    
                                    ### Methode de la Table User ### 
                                     
#Creation d'un User
@csrf_exempt
def Create_user_form(request):
    if request.method=="POST":
        form =UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
            except:
                pass
            
# Même chose via un serializer(C'est ce que nous utiliseront)
  
    
@csrf_exempt
def Create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Utilisateur créé"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({"Info":"Utilisateur non créé"})
    return redirect("/show_user")              
            
            
#Liste des Users
def show_user(request):  
    data = { "users": [] }
    users = User.objects.all()     
    for user in users:
        
        data["users"].append({
            "id": user.id,
            "nom": user.nom,
            "prenom": user.prenom,
            "email": user.email,
            "contact":user.contact,
            "id_profil": user.idpro.idpro,
            "nom_profil": user.idpro.nomprofil
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data) 

#Liste des comerciaux
def show_coms(request):  
    data = { "commerciaux": [] }
    total_coms = User.objects.filter(idpro=3).count()
    commerciaux = User.objects.filter(idpro=3)      
    for commercial in commerciaux:
        
        data["commerciaux"].append({
            "id": commercial.id,
            "nom": commercial.nom,
            "prenom": commercial.prenom,
            "email": commercial.email,
            "contact":commercial.contact,
            "id_profil": commercial.idpro.idpro,
            "nom_profil": commercial.idpro.nomprofil,
            "nb_commerciaux_total": total_coms
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)  

#Liste des gerants
def show_gerants(request):  
    data = { "gerants": [] }
    total_gerants = User.objects.filter(idpro=2).count()
    commerciaux = User.objects.filter(idpro=2)      
    for commercial in commerciaux:
        
        data["gerants"].append({
            "id": commercial.id,
            "nom": commercial.nom,
            "prenom": commercial.prenom,
            "email": commercial.email,
            "contact":commercial.contact,
            "id_profil": commercial.idpro.idpro,
            "nom_profil": commercial.idpro.nomprofil,
            "nb_gerants_total": total_gerants
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)  

#Avoir un utilisateur via son id
def show_one_user(request, id):  
    data = { "users": [] }
    users = User.objects.filter(id=id)    
    for user in users:
        
        data["users"].append({
            "id": user.id,
            "nom": user.nom,
            "prenom": user.prenom,
            "email": user.email,
            "contact":user.contact,
            "id_profil": user.idpro.idpro,
            "nom_profil": user.idpro.nomprofil
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)     

#Avoir un Client via son id

def show_one_client(request, id):  
    data = { "client": [] }
    clients = Client.objects.filter(id=id)    
    for client in clients:
        
        data["client"].append({
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "adresse": client.adresse,
            "ville": client.idVille.nomville,
            "sexe": client.sexe,
            "contact":client.contact,
            
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)         

#Modification d'un User
@csrf_exempt
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.update(user, request.data)
            return JsonResponse({"info": "Utilisateur modifié"})
        return JsonResponse({"error": serializer.errors})             


#Suppression d'un User
@csrf_exempt
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    
    
                                             ### Methode de la Table Info Livraison ### 
                                             
#J'ai un trigger "reduction_de_la_qte" qui fait la mise à jour automatique de la quantité àpres vente

"""
Contenu du trigger:

CREATE TRIGGER reduction_de_la_qte 
AFTER INSERT ON info_livraison 
FOR EACH ROW 
BEGIN 
    UPDATE type_eau SET qte = qte - NEW.qte_livr WHERE id = NEW.id; 
END

"""
                                             
                                             
#Creation d'une livraison
@csrf_exempt
def Create_livr_form(request):
    if request.method=="POST":
        form =UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
            except:
                pass
            
# Même chose via un serializer(C'est ce que nous utiliseront)
            
@csrf_exempt
def Create_livr(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = Info_livr_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Livraison effectuée"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({"Info":"Livraison non effectuée"})
    return redirect("/show_livr")              
            
#Liste des Livraisons
def show_livr(request):
    
    livraisons = Info_livraison.objects.all()
    livraisons_list = []
    for livraison in livraisons:
        livraisons_list.append({
        'id': livraison.id,
        'qte_livr': livraison.qte_livr,
        'montant': livraison.montant,
        'bonus': livraison.bonus,
        'date_livr': livraison.date_livr,
        'idcli': livraison.idcli.id,
        'nomcli': livraison.idcli.nom,
        'ideau': livraison.ideau.id,
        'libelle_eau':livraison.ideau.libelle,
        'idcom': livraison.idcom.id,
        'nomcom':livraison.idcom.nom
        })
    return JsonResponse({'livraisons': livraisons_list})

#Livraison par commercial(id à passer)

def get_commercial_livraisons(request, idcom):
    data = { "livraisons": [] }
    livraisons = Info_livraison.objects.filter(idcom=idcom)
    for livraison in livraisons:
        data["livraisons"].append({
            "id": livraison.id,
            "Quantite_livree": livraison.qte_livr,
            "montant": livraison.montant,
            "bonus": livraison.bonus,
            "date_livraison": livraison.date_livr,
            "Client": livraison.idcli,
            "Type_eau": livraison.ideau,
            "Commercial": livraison.idcom
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)       

"""
   PARTIE A REVOIR 
   
#Modification d'un livraison
def update_livr(request, id):
    user = User.objects.get(id=id)
    form = Type_eauForm(request.POST, instance = user)
    if form.is_valid():
        form.save()            


#Suppression d'une livraison
def delete_livr(request, id):
    user = User.objects.get(id=id)
    user.delete() 
                                                
"""


                                    ### Methode de la Table Client ### 
                                     
#Creation d'un client
@csrf_exempt
def Create_client_form(request):
    if request.method=="POST":
        form =ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
            except:
                pass
            
# Même chose via un serializer(C'est ce que nous utiliseront)
  
    
@csrf_exempt
def Create_client(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info": "Client créé"})
        else:
         #return JsonResponse({"error": serializer.errors})
         return JsonResponse({'status': 200,"success": True,"Info":"Client non créé"})
    return redirect("/show_client")              
            
            
#Liste des client
def show_client(request):  
    data = { "clients": [],  }
    clients = Client.objects.all()
    total_clients = Client.objects.count()
    for client in clients:
        
        data["clients"].append({
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "adresse": client.adresse,
            "contact": client.contact,
            "longitude": client.longitude,
            "latitude": client.latitude,
            "sexe":client.sexe,
            "created_by": client.created_by.nom,
            "date_created": client.date_created,
            "date_update":client.date_update,
            "statut": client.statut,
            "ville": client.idVille.nomville,
            "nb_client_total": total_clients
            
            
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data,  safe= False)        

class ClientList(generics.ListCreateAPIView):
    data = { "clients": [] }  
    queryset = Client.objects.all()
    serializer_class = ClientSerializer 

#Modification d'un client
import json

@csrf_exempt
def update_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'PATCH':
        data = json.loads(request.body)
        serializer = ClientSerializer(client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"info": "Client modifié"})
        return JsonResponse({"error": serializer.errors})


#Suppression d'un client
@csrf_exempt
def delete_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return JsonResponse({"status": 200})
    
    
    
#Generer un token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajoutez des champs personnalisés au payload du token
        token['user_id'] = user.id
        token['user_email'] = user.email
        # Ajoutez d'autres champs personnalisés si nécessaire

        return token
  
    
""" #LoginWeb
@csrf_exempt
def angularlogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)   
        email = data['email']
        password = data['password']  
                   
        try:
                user = User.objects.get(email=email, password=password)
                
                if user is not None and user.idpro.idpro == 1 :                    
                    return JsonResponse({'status': 200,'success': True, 'message': 'Connecté en tant qu Administrateur', 'id':user.idpro.idpro, 'isLogged': 1 })
                if user is not None and user.idpro.idpro == 2 :
                    return JsonResponse({'status': 200,"success": True, 'message': 'Connecté en tant que Gerant', 'id':user.idpro.idpro, 'isLogged': 1})
                if user is not None and user.idpro.idpro == 3  :
                    return JsonResponse({'status': 200,"success": True, 'message': 'Connecté en tant que Commercial' ,'id':user.idpro.idpro, 'isLogged': 1 })
        except:
                return JsonResponse({'status': 400,"success": False, 'message': 'Options de connexion invalides'})
           """      
from rest_framework_simplejwt.tokens import RefreshToken
@csrf_exempt
def angularlogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email, password=password)

            if user is not None:
                serializer = UserSerializer(user)
                token = RefreshToken.for_user(user)

                return JsonResponse({
                    'status': 200,
                    'success': True,
                    'message': 'Connecté avec succès',
                    'user': serializer.data,
                    'id':user.idpro.idpro,
                    'token': {
                        'access': str(token.access_token),
                        'refresh': str(token),
                    }
                })
        except User.DoesNotExist:
            return JsonResponse({
                'status': 400,
                'success': False,
                'message': 'Options de connexion invalides'
            })

#LoginMobile
@csrf_exempt
def flutterlogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)   
        contact = data['contact']
        password = data['password']  
                   
        try:
                user = User.objects.get(contact=contact, password=password)
                
                if user is not None and user.idpro.idpro == 3  :
                    return JsonResponse({'status': 200,"success": True, 'message': 'Connecté en tant que Commercial', 'id':user.id, 'nom':user.nom })
        except:
                return JsonResponse({'status': 400,"success": False, 'message': 'Options de connexion invalides'})
                            
                
###Livraison journaliere
""" def livraisons_aujourdhui_json(request):
    livraisons = Info_livraison.objects.filter(date_livr__date=timezone.now().date())
    livraisons_list = list(livraisons.values('id', 'qte_livr', 'montant', 'bonus', 'date_livr', 'idcli', 'ideau', 'idcom'))
    return JsonResponse({'livraisons': livraisons_list})  """   
""" def livraisons_aujourdhui_json(request):
    livraisons = Info_livraison.objects.filter(date_livr__date=timezone.now().date())
    livraisons_list = []
    for livraison in livraisons:
        client = Client.objects.get(id=livraison.idcli)
        commercial = User.objects.get(id=livraison.idcom)
        type_eau = Type_eau.objects.get(id=livraison.ideau)
        livraisons_list.append({
        'id': livraison.id,
        'qte_livr': livraison.qte_livr,
        'montant': livraison.montant,
        'bonus': livraison.bonus,
        'date_livr': livraison.date_livr,
        'client_name': client.id,
        'commercial_name': commercial.nom,
        'type_eau_name': type_eau.libelle
        })
    return JsonResponse({'livraisons': livraisons_list})  """    
    
def today_livr(request):
    livraisons = Info_livraison.objects.filter(date_livr__date=timezone.now().date())
    livraisons_list = []
    for livraison in livraisons:
        livraisons_list.append({
        'id': livraison.id,
        'qte_livr': livraison.qte_livr,
        'montant': livraison.montant,
        'bonus': livraison.bonus,
        'date_livr': livraison.date_livr,
        'idcli': livraison.idcli.id,
        'nomcli': livraison.idcli.nom,
        'ideau': livraison.ideau.id,
        'libelle_eau':livraison.ideau.libelle,
        'idcom': livraison.idcom.id,
        'nomcom':livraison.idcom.nom
        })
    return JsonResponse({'livraisons': livraisons_list})

#Livraison par commercial
def today_livr_per_com(request, idcom):
    livraisons = Info_livraison.objects.filter(date_livr__date=timezone.now().date(), idcom= idcom)
    livraisons_list = []
    for livraison in livraisons:
        livraisons_list.append({
        'id': livraison.id,
        'qte_livr': livraison.qte_livr,
        'montant': livraison.montant,
        'bonus': livraison.bonus,
        'date_livr': livraison.date_livr,
        'idcli': livraison.idcli.id,
        'nomcli': livraison.idcli.nom,
        'ideau': livraison.ideau.id,
        'libelle_eau':livraison.ideau.libelle,
        'idcom': livraison.idcom.id,
        'nomcom':livraison.idcom.nom
        })
    return JsonResponse({'livraisons': livraisons_list})               


###Quantité Total de Type d'eau vendu
def show_livr_grouped_by_water_type(request):
    data = {"types_d_eau": []}
    livrs = Info_livraison.objects.values("ideau__libelle").annotate(total_qte=Sum("qte_livr"))
    for livr in livrs:
        data["types_d_eau"].append({
            "type_d_eau": livr["ideau__libelle"],
            "total_qte": livr["total_qte"],
        })
    return JsonResponse(data)

###Commercial le plus rentable
def show_com_ca(request):
    data = {"commercials": []}
    livrs = Info_livraison.objects.values("idcom__nom").annotate(total_ca=Sum("montant"))
    for livr in livrs:
        data["commercials"].append({
            "commercial": livr["idcom__nom"],
            "total_ca": livr["total_ca"],
        })
    return JsonResponse(data)


###Recherche client
class SearchClientView(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search', '')
        clients = Client.objects.filter(nom__icontains=search_term)
        serialized_clients = ClientSerializer(clients, many=True)
        return JsonResponse(serialized_clients.data, safe=False)
    
    
###CA de la journéé
def today_ca(request):
    ventes_aujourdhui = Info_livraison.objects.filter(date_livr__date=timezone.now().date())
    chiffre_affaires = ventes_aujourdhui.aggregate(Sum('montant'))
    return JsonResponse({'chiffre_affaires': chiffre_affaires['montant__sum']}) 
   
#Créer par
def clients_par_commercial(request, created_by):
    data = { "clients": [] }
    clients = Client.objects.filter(created_by=created_by)
    for client in clients:
        data["clients"].append({
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "adresse": client.adresse,
            "longitude": client.longitude,
            "latitude": client.latitude,
            "sexe": client.sexe,
            "date_created": client.date_created,
            "date_update": client.date_update,
            "statut": client.statut,
            "ville": client.idVille.nomville,
            #"nb_client_total": total_users
        })
    """ Envoyer sous forme de Json: API """
    return JsonResponse(data, safe=False)

def clients_par_commercial_five(request, created_by):
    data = { "clients": [] }
    clients = Client.objects.filter(created_by=created_by).order_by('-id')[:5]
    for client in clients:
        data["clients"].append({
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "adresse": client.adresse,
            "longitude": client.longitude,
            "latitude": client.latitude,
            "sexe": client.sexe,
            "date_created": client.date_created,
            "date_update": client.date_update,
            "statut": client.statut,
            "ville": client.idVille.nomville,
            #"nb_client_total": total_users
        })
    """ Envoyer sous forme de Json: API """
    return JsonResponse(data, safe=False)



def get_commercial_livraisons(request, idcom):
    data = { "livraisons": [] }
    livraisons = Info_livraison.objects.filter(idcom=idcom)
    for livraison in livraisons:
        data["livraisons"].append({
            "id": livraison.id,
            "Quantite_livree": livraison.qte_livr,
            "montant": livraison.montant,
            "bonus": livraison.bonus,
            "date_livraison": livraison.date_livr,
            "Client": livraison.idcli,
            "Type_eau": livraison.ideau,
            "Commercial": livraison.idcom
                                  })
        """ Envoyer sous forme de Json: API """
    return JsonResponse(data)       


#CA par mois

import datetime

def chiffre_affaire_par_mois(request):
    current_year = datetime.datetime.now().year
    chiffres_affaires = {}
    for month in range(1, 13):
        chiffre_affaire = Info_livraison.objects.filter(date_livr__year=current_year, date_livr__month=month).aggregate(Sum('montant'))['montant__sum']
        month_name = calendar.month_name[month]
        chiffres_affaires[month_name] = chiffre_affaire or 0
    return JsonResponse({"Chiffre_d_affaire": chiffres_affaires})

from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings

@csrf_exempt
def envoyer_sms(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to='+22890303046',  # Remplacez par le numéro de téléphone de destination
        from_=settings.TWILIO_PHONE_NUMBER,
        body='Ceci est un exemple de SMS envoyé depuis Django avec Twilio! par Arnaud'
    )
    return HttpResponse(f'SMS envoyé, SID : {message.sid}')