
from rest_framework import viewsets
from .serializers import EmpresaSerializer, HistorialSerializer, EstadoSerializer, EvidenciaSerializer, TercerosSerializer, TipoServicioSerializer, Empresa, Historial, Estado, Evidencia, Terceros, TipoServicio
class EmpresaView(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class HistorialView(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
class EstadoView(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
class EvidenciaView(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
class TercerosView(viewsets.ModelViewSet):
    queryset = Terceros.objects.all()
    serializer_class = TercerosSerializer
class TipoServicioView(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
# Create your views here.

