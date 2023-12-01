from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Answers, Sertif

item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersView(ListView):
    model = Answers
    context_object_name = 'answers_list'
    success_url = reverse_lazy('testik:answers')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersCreate(CreateView):
    model = Answers
    template_name = 'testik/answers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:answers')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersUpdate(UpdateView):
    model = Answers
    template_name = 'testik/answers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:answers')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersDelete(DeleteView):
    model = Answers
    success_url = reverse_lazy('testik:answers')
	
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifView(ListView):
	model = Sertif
	context_object_name = 'sertif_list'
	success_url = reverse_lazy('testik:SertifView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SertifView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("users").verbose_name
		context['col3name'] = self.model._meta.get_field("blank").verbose_name
		context['col4name'] = self.model._meta.get_field("date").verbose_name
		context['col5name'] = self.model._meta.get_field("filled_sertif").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifUpdate(UpdateView):
	model = Sertif
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/testik/Sertif/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SertifUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','users', 'blank'}
		context['secslovar'] = {'date', 'filled_sertif'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDetail(DetailView):
	model = Sertif
	context_object_name = 'sertif_one'
	success_url = '/testik/Sertif/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SertifDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','users', 'blank'}
		context['secslovar'] = {'date', 'filled_sertif'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifCreate(CreateView):
	model = Sertif
	context_object_name = 'sertif_one'
	success_url = '/testik/Sertif/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SertifCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','users', 'blank'}
		context['secslovar'] = {'date', 'filled_sertif'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDelete(DeleteView):
	model = Sertif
	success_url = '/testik/Sertif/'
