from django.template.response import TemplateResponse
from django.http import HttpResponse
from .forms import DataframeForm
from .models import DataframeNode
from django.db.models.signals import post_save
from django.dispatch import receiver
 
def index(request):
 if request.method == 'POST':
	 form = DataframeForm(request.POST,request.FILES)
	 if form.is_valid():
	  form.save()
	  return TemplateResponse(request, 'success.html')
	 else:
	 	return HttpResponse("помилка")
 else:
     form = DataframeForm()
 return TemplateResponse(request, 'dataform.html', {
     'form': form
 })

@receiver(post_save, sender=DataframeNode)
def predict(sender, instance, **kwargs):
	print("dor")


