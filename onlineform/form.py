from django import forms  
from .models import ClientDetails  
  
class ClientForm(forms.ModelForm):  
    class Meta:  
        model = ClientDetails  
        fields = "__all__"  