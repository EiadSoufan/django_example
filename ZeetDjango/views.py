from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse,FileResponse


def index(request):
    return HttpResponse('index')
	
	
def detail(request, category_id):
    return HttpResponse('detail')
	

def pdffile(request, category_id,fid):
    return HttpResponse('pdffile')
