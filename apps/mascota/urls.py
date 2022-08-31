from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from views import index, mascota_create, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, PersonaList,persona_list

urlpatterns = [

    # URLS CLASS VIEW
    url(r'^$', index, name='index'),
    # URL mascota_view
    url(r'^mascota/nuevo_cview$', MascotaCreate.as_view(), name='mascota_crear_c'),
    # URL mascota_list
    url(r'^mascota/listar_cview$', MascotaList.as_view(), name='mascota_listar_c'),
    # URL mascota_list
    url(r'^mascota/editar_cview/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar_c'),
    # URL mascota_delete
    url(r'^mascota/eliminar_cview/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar_c'),

    # URLS FUNCTIONS VIEW
    url(r'^mascota/nuevo_fview$', mascota_create, name='mascota_crear_f'),
    url(r'^mascota/listar_fview$', mascota_list, name='mascota_listar_f'),
    url(r'^mascota/editar_fview/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar_f'),
    url(r'^mascota/eliminar_fview/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar_f'),



    url(r'^mascota/listar_persona_cview$', PersonaList.as_view(), name='persona_listar_c'),
    url(r'^mascota/listar_persona_fview$', persona_list, name='persona_listar_f'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)