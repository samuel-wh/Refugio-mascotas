from django.shortcuts import render, redirect 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from forms import MascotaForm
from models import Mascota, Persona



# Create your views here.
def index(request):
    return render(request, 'mascota/index.html')

# Vistas basadas en funciones

# Definimos la funcion crear 
def mascota_create(request):
    # Si el request es un POST
    if request.method == 'POST':
        # Se reciben los datos que se estan mandado en el post del formulario
        form = MascotaForm(request.POST, request.FILES) 
        # Si se recibe el post, se validan los datos
        if form.is_valid():
            form.save()            
        # Nos redirige al index de mascota
        return redirect('mascota_listar_f')
    else:
        #Nos renderiza el formulario
        form = MascotaForm()
    return render(request, 'mascota/view_functions/mascota_form.html', {'form':form})

# Definimos la funcion de la listar mascota
def mascota_list(request):
    # Creamos el queryset para traer los datos del modelo mascota
    mascota = Mascota.objects.all().order_by('id')
    # Se manda el queryset al contexto
    contexto = {'mascotas':mascota}
    # Render con el nombre del template y el contexto
    return render(request, 'mascota/view_functions/mascota_list.html', contexto)

# Definimos la funcion editar mascota
def mascota_edit(request, id_mascota):
    # QuerySet para obtener el objeto que tiene el id que se esta enviando
    mascota = Mascota.objects.get(id=id_mascota)
    # Mandamos los que se obtuvo al formulario
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar_f')
    return render(request, 'mascota/view_functions/mascota_form.html', {'form':form})

# Definimos la funcion eliminar mascota
def mascota_delete(request, id_mascota):
    # QuerySet para obtener el objeto que tiene el id que se esta enviando
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar_f')
    return render(request, 'mascota/view_functions/mascota_delete.html', {'mascota':mascota})




# Vistas basadas en clases
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/view_class/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/view_class/mascota_form.html'
    success_url = reverse_lazy('mascota_listar_c')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/view_class/mascota_form.html'
    success_url = reverse_lazy('mascota_listar_c')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/view_class/mascota_delete.html'
    success_url = reverse_lazy('mascota_listar_c')


def persona_list(request):
    persona = Persona.objects.all().order_by('id')
    contexto = {'persona':persona}
    return render(request, 'mascota/view_functions/persona_list.html', contexto)

class PersonaList(ListView):
    model = Persona 
    template_name = 'mascota/view_class/persona_list.html'