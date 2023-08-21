from django.db import models
from django.utils import timezone

current_date = timezone.now().date()

# Create your models here.


  ### Table Ville ###  

class Ville(models.Model):
    idVille = models.AutoField(primary_key=True)
    nomville = models.CharField(max_length= 150, null= False)

    def __str__(self):
        return f"{self.nomville}"
    
    class Meta:
        db_table = "ville"
        
  ### Table Type d'eau ###  

class Type_eau(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length= 100, null= False)
    pu = models.IntegerField( null= False)
    qte = models.IntegerField(null= False)
    qte_seuil = models.IntegerField( null= False)

    def __str__(self):
        return f"{self.libelle} {self.pu}"
    
    class Meta:
        db_table = "type_eau"

 
        
  ### Table Profil ###  
        
class Profil(models.Model):
    idpro = models.AutoField(primary_key=True)
    nomprofil = models.CharField(max_length= 20, null= False, blank=False)
    
    def __str__(self):
        return f"{self.nomprofil}"
    
    class Meta:
        db_table = "profil"
 
   ### Table User ###  
        
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20, null= False)
    prenom = models.CharField(max_length=30, null= False)
    email = models.EmailField(unique=True, null= False)
    password = models.CharField(max_length=15, null= False)
    contact = models.CharField(max_length=20, null= False)
    idpro = models.ForeignKey(Profil,null= False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    class Meta:
        db_table = "user"

 ### Table Client ###  

class Client(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20, null= False)
    prenom = models.CharField(max_length=30, null= True)
    contact = models.CharField(max_length=20, null= False)
    adresse = models.TextField(max_length=100, null= False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    sexe = models.CharField(max_length=1, choices=SEX_CHOICES)  
    created_by = models.ForeignKey(User, null= False, on_delete=models.DO_NOTHING,)
    updated_by = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= False)
    date_update = models.DateTimeField(auto_now=True,null= True)
    statut = models.CharField(max_length=10)
    idVille = models.ForeignKey(Ville,null= False, on_delete=models.DO_NOTHING)

    

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    class Meta:
        db_table = "client"
        
     
  ### Table Livraison ###  
  
class Info_livraison(models.Model):
    id = models.AutoField(primary_key=True)
    qte_livr = models.IntegerField(null= False)
    montant = models.IntegerField(null= False)
    bonus = models.IntegerField(null= True, default=0)
    date_livr = models.DateTimeField(auto_now_add=True)
    idcli = models.ForeignKey(Client, null= False, on_delete=models.DO_NOTHING,)
    ideau = models.ForeignKey(Type_eau, null= False, on_delete=models.DO_NOTHING,)
    idcom = models.ForeignKey(User, null= False, on_delete=models.DO_NOTHING,)
    
    def __str__(self):
        return f"{self.montant} {self.idcli} {self.ideau} {self.idcom}"
    
    class Meta:
        db_table = "info_livraison"
    
    
    
        