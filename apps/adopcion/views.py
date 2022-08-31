import re
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from ..mascota.models import Mascota

from models import Persona, Solicitud
from forms import PersonaForm, SolicitudForm
# Create your views here.

# Vistas basadas en funciones
def index(request):
    return render(request, 'adopcion/index.html')

def solicitud_create(request):
    if request.method == 'POST':
        
        form = SolicitudForm(request.POST)
        second_form = PersonaForm(request.POST) 
        if form.is_valid() and second_form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = second_form.save()
            solicitud.save()
            form.save()            
        return redirect('solicitud_listar_f')
    else:
        form = SolicitudForm()
        second_form = PersonaForm()
    return render(request, 'adopcion/view_functions/solicitud_form.html', {'form':form, 'second_form':second_form})

def solicitud_list(request):
    solicitud = Solicitud.objects.all().order_by('id')
    contexto = {'solicitudes':solicitud}
    return render(request, 'adopcion/view_functions/solicitud_list.html', contexto)

def solicitud_edit(request, id_solicitud):
    
    solicitud = Solicitud.objects.get(id=id_solicitud)
    persona = Persona.objects.get(id=solicitud.persona_id)

    if request.method == 'GET':
        form = SolicitudForm(instance=solicitud)
        second_form = PersonaForm(instance=persona)
    else:
        form = SolicitudForm(request.POST, instance=solicitud)
        second_form = PersonaForm(request.POST, instance=persona)
        if form.is_valid() and second_form.is_valid():
            second_form.save()
            form.save()
            
        return redirect('solicitud_listar_f')
    return render(request, 'adopcion/view_functions/solicitud_form.html', {'form':form, 'second_form':second_form})

def solicitud_delete(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitud_listar_f')
    return render(request, 'adopcion/view_functions/solicitud_delete.html', {'solicitud':solicitud})


# Vistas basadas en clases
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/view_class/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/view_class/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar_c')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        # Recoge los valores que se ingresaron en los dos formularios
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        # Se validan
        if form.is_valid() and form2.is_valid():
            #Se guarda los valores del primer formulario
            solicitud = form.save(commit=False)
            # Se guarda los valores del segundo formulario
            solicitud.persona = form2.save()
            # Se guardan todos los valores en el objeto
            solicitud.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2= form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/view_class/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar_c')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        # Recoge los valores que se ingresaron en los dos formularios
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)

        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        # Se validan
        if form.is_valid() and form2.is_valid():
            #Se guarda los valores del primer formulario
            form.save()
            # Se guarda los valores del segundo formulario
            form2.save()
            # Se guardan todos los valores en el objeto
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/view_class/solicitud_delete.html'
    success_url = reverse_lazy('solicitud_listar_c')
