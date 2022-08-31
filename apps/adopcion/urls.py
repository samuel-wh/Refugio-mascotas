from django.conf.urls import url, include
from views import SolicitudDelete, index, SolicitudList, SolicitudCreate, SolicitudUpdate, solicitud_create, solicitud_list, solicitud_edit, solicitud_delete

urlpatterns = [
    # URLS CLASS VIEW
    url(r'^$', index, name='index'),
    url(r'^solicitud/listar_cview$', SolicitudList.as_view(), name = 'solicitud_listar_c'),
    url(r'^solicitud/nueva_cview$', SolicitudCreate.as_view(), name = 'solicitud_crear_c'),
    url(r'^solicitud/editar_cview/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name = 'solicitud_editar_c'),
    url(r'^solicitud/eliminar_cview/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name = 'solicitud_eliminar_c'),

    

    # URLS FUNCTIONS VIEW
    url(r'^solicitud/nuevo_fview$', solicitud_create, name='solicitud_crear_f'),
    url(r'^solicitud/listar_fview$', solicitud_list, name='solicitud_listar_f'),
    url(r'^solicitud/editar_fview/(?P<id_solicitud>\d+)/$', solicitud_edit, name='solicitud_editar_f'),
    url(r'^solicitud/eliminar_fview/(?P<id_solicitud>\d+)/$', solicitud_delete, name='solicitud_eliminar_f'),
]
