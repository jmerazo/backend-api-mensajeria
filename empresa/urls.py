from django.urls import path
from .views import EmpresaView, HistorialView, EstadoView, EvidenciaView, TercerosView, TipoServicioView


urlpatterns = [
    path('empresa/',EmpresaView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),
    path('empresa/<int:pk>', EmpresaView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })),

    path('historial/',HistorialView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),

     path('historial/<int:pk>', HistorialView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })),
    path('estado/',EstadoView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),
    path('estado/<int:pk>', EstadoView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })),
    path('evidencia/', EvidenciaView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),
    path('evidencia/<int:pk>', EvidenciaView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })),
    path('terceros/',TercerosView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),
    path('terceros/<int:pk>', TercerosView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })), 
    path('tiposervicio/',TipoServicioView.as_view({
        'get' : 'list',
        'post' : 'create',
        

    })),
    path('tiposervicio/<int:pk>', TipoServicioView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',


    })),       
]