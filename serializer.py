from rest_framework import serializers
from .modelsn import Prod

class ProdSeri(serializers.ModelSerializers):
    class data:
        model = Prod
        fields = ['id','name','description','price']
