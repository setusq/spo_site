from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView
from mysite.anketa.models import Professions, Skills, Questions, Model_prof, Blank, Human

item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionsView(ListView):
	model = Professions
	context_object_name = 'professions_list'
	success_url = reverse_lazy('anketa:ProfessionsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionUpdate(UpdateView):
	model = Professions
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/professions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionDetail(DetailView):
	model = Professions
	context_object_name = 'profession_one'
	success_url = '/anketa/professions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionCreate(CreateView):
	model = Professions
	context_object_name = 'profession_one'
	success_url = '/anketa/professions/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionDelete(DeleteView):
	model = Professions
	success_url = '/anketa/professions/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsView(ListView):
	model = Skills
	context_object_name = 'skills_list'
	success_url = reverse_lazy('anketa:SkillsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsUpdate(UpdateView):
	model = Skills
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/skills/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsDetail(DetailView):
	model = Skills
	context_object_name = 'skills_one'
	success_url = '/anketa/skills/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsCreate(CreateView):
	model = Skills
	context_object_name = 'skills_one'
	success_url = '/anketa/skills/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsDelete(DeleteView):
	model = Skills
	success_url = '/anketa/skills/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsView(ListView):
	model = Questions
	context_object_name = 'questions_list'
	success_url = reverse_lazy('anketa:QuestionsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("score").verbose_name
		context['col3name'] = self.model._meta.get_field("skills").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsUpdate(UpdateView):
	model = Questions
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/questions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsDetail(DetailView):
	model = Questions
	context_object_name = 'questions_one'
	success_url = '/anketa/questions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsCreate(CreateView):
	model = Questions
	context_object_name = 'questions_one'
	success_url = '/anketa/questions/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsDelete(DeleteView):
	model = Questions
	success_url = '/anketa/questions/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profView(ListView):
	model = Model_prof
	context_object_name = 'modelprof_list'
	success_url = reverse_lazy('anketa:Model_profView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("professions").verbose_name
		context['col3name'] = self.model._meta.get_field("skills").verbose_name
		context['col4name'] = self.model._meta.get_field("score").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profUpdate(UpdateView):
	model = Model_prof
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/model_prof/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','professions'}
		context['secslovar'] = {'skills',"score"}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profDetail(DetailView):
	model = Model_prof
	context_object_name = 'modelprof_one'
	success_url = '/anketa/model_prof/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','professions'}
		context['secslovar'] = {'skills',"score"}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profCreate(CreateView):
	model = Model_prof
	context_object_name = 'modelprof_one'
	success_url = '/anketa/model_prof/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title','professions'}
		context['secslovar'] = {'skills',"score"}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profDelete(DeleteView):
	model = Model_prof
	success_url = '/anketa/model_prof/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankView(ListView):
	model = Blank
	context_object_name = 'blank_list'
	success_url = reverse_lazy('anketa:BlankView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(BlankView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("image_full").verbose_name
		context['col3name'] = self.model._meta.get_field("image_one").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankUpdate(UpdateView):
	model = Blank
	fields = '__all__'
	success_url = '/anketa/blank/'
	template_name_suffix = '_update_form'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(BlankUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {'image_full','image_one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankDetail(DetailView):
	model = Blank
	context_object_name = 'blank_one'
	success_url = '/anketa/blank/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(BlankDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {'image_full','image_one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankCreate(CreateView):
	model = Blank
	context_object_name = 'blank_one'
	success_url = '/anketa/blank/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(BlankCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['secslovar'] = {'image_full','image_one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankDelete(DeleteView):
	model = Blank
	success_url = '/anketa/blank/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanView(ListView):
	model = Human
	context_object_name = 'human_list'
	success_url = reverse_lazy('anketa:HumanView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(HumanView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("avatar").verbose_name
		context['col3name'] = self.model._meta.get_field("phone").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanUpdate(UpdateView):
	model = Human
	fields = '__all__'
	success_url = '/anketa/human/'
	template_name_suffix = '_update_form'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(HumanUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {'avatar','phone'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanDetail(DetailView):
	model = Human
	context_object_name = 'human_one'
	success_url = '/anketa/human/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(HumanDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {'avatar','phone'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanCreate(CreateView):
	model = Human
	context_object_name = 'human_one'
	success_url = '/anketa/human/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(HumanCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['secslovar'] = {'avatar','phone'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanDelete(DeleteView):
	model = Human
	success_url = '/anketa/human/'
