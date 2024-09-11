from rest_framework import viewsets
from .models import Prod
from .serializers import ProdSeri

class ProdView(viewsets.ModelViewset):
    queryset = prod.objects.all()
    serializers_class = ProdSeri