from rest_framework import serializers
from cadastrocloud.models import cadastro
 
class CadastroCloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = cadastro
        fields = ('id', 'codigo','cpu', 'memoria','disco','sistemaoperacional')