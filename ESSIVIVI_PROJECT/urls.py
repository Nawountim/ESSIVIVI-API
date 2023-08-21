from django.urls import path
from django.contrib import admin
from ESSIVIVI_PROJECT import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .views import SearchClientView
from .views import ClientList


schema_view = get_schema_view(
   openapi.Info(
      title="ESSIVIVI API",
      default_version='v1',
      description="Everything you need to work with is here ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    
     
#GET
    path('', views.login),
    path('show_profil', views.show_profile),
    path('show_ville', views.show_ville),
    path('show_user', views.show_user),
    path('show_coms', views.show_coms),
    path('show_gerants', views.show_gerants),
    path('show_one_user/<int:id>', views.show_one_user),
    path('show_eau', views.show_eau),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('show_client', views.show_client),
    path('show_one_client/<int:id>', views.show_one_client),
    path('show_livr', views.show_livr),
    path('today_ca', views.today_ca),
    path('today_livr', views.today_livr),
    path('today_livr_per_com/<int:idcom>', views.today_livr_per_com),
    path('show_livrbycom/<int:idcom>', views.get_commercial_livraisons),
    path('show_eau_per_qte', views.show_livr_grouped_by_water_type),
    path('show_com_ca', views.show_com_ca),
    path('show_months_ca', views.chiffre_affaire_par_mois),
    path('search/client/', SearchClientView.as_view()),
    path('show_client_by_com/<int:created_by>', views.clients_par_commercial),
    path('show_five_client_by_com/<int:created_by>', views.clients_par_commercial_five),
    path('api/token/', views.MyTokenObtainPairSerializer, name='token_obtain_pair'),



    
#POST    
    path('new_eau', views.Create_eau),
    path('new_profil', views.Create_profile),
    path('new_ville', views.Create_Ville),
    path('new_user', views.Create_user),  
    path('new_client', views.Create_client), 
    path('new_livr', views.Create_livr), 
    
    path('envoyer_sms', views.envoyer_sms), 
    
    
#Update    
    path('update_ville/<int:idVille>', views.update_ville),
    path('update_client/<int:id>', views.update_client),


#Delete
    path('delete_profil/<int:id>', views.delete_profil),
    path('delete_ville/<int:id>', views.delete_ville),
    path('delete_eau/<int:id>', views.delete_user),
    path('delete_client/<int:id>', views.delete_client),
    path('delete_user/<int:id>', views.delete_user),
    

#Swagger    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
#Login

    path('angularlogin', views.angularlogin),    
    path('flutterlogin', views.flutterlogin),    

    
    

]