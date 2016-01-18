from django.shortcuts import render

from cadastrocloud.models import cadastro
from cadastrocloud.serializers import CadastroCloudSerializer
from rest_framework import mixins
from rest_framework import generics
from django.views.generic import TemplateView

# Create your views here.
    
def post_list(request):
        return render(request, 'cadastrocloud/post_list.html', {})
        
class CadastroList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = cadastro.objects.all()
    serializer_class = CadastroCloudSerializer
 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
 
    
class CadastroDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = cadastro.objects.all()
    serializer_class = CadastroCloudSerializer
 
    def get(self, request, *args, **kwargs):
        print "teste"
        return self.retrieve(request, *args, **kwargs)
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CadastroView(TemplateView):
   	template_name = "post_list.html"

    

