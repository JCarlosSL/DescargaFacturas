from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
from .listar import ListarFacturas
from .models import Factura

path = 'static/facturas'


def CargarData():
    for vector in ListarFacturas():
        factura = str(vector[2])+"-"+str(vector[3])
        result=Factura.objects.filter(Q(nroFac1=factura))
        if not result:
            Factura.objects.create(nroFac1=factura,
                fecha=vector[4],RUC=vector[5],extra=vector[1],
                rucEmpresa=vector[0])

@login_required
def search(request):
    template='home/mostrar_facturas.html'
    if (request.GET.get('q') ):
        query=request.GET.get('q')
        result=Factura.objects.filter(Q(fecha__icontains=query) | Q(RUC__icontains=query) | Q(nroFac1__icontains=query))
        #context={ 'posts':result 
        #}
        paginator = Paginator(result, 6) # Show 25 contacts per page.
        is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page') or 1
        try:
        	current_page = paginator.page(page)
        except InvalidPage as e:
        	raise Http404(str(e))
        context={ 'is_paginated':is_paginated,
        		'current_page':current_page,
        		'posts':result}
        return render(request,template,context)
    else:
        return redirect('home')
   

def filtroanho(request,ango):
    template='home/mostrar_facturas.html'
    result = Factura.objects.filter(Q(fecha__icontains=ango))
    paginate_by=6
    context= {
            'posts':result,
            'anho':ango}
    return render(request,template,context)

def filtromes(request,ango,mes):
    template='home/mostrar_facturas.html'
    result = Factura.objects.filter(Q(fecha__icontains=str(ango)+"-"+mes))
    paginate_by=6
    context = {
            'posts':result,
            'anho':ango}
    return render(request,template,context)


class PostListView(ListView):
    model = Factura
    template_name = 'home/mostrar_facturas.html'  # <app>/<model>_<viewtype>.html

    context_object_name = 'posts'
    ordering = ['-fecha']
    paginate_by = 6
    
    CargarData()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)
