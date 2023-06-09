from allauth.account.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets

from .filters import MachineFilter, AuthMachineFilter, AuthMaintenanceFilter, AuthClaimFilter
from .forms import MachineForm, MaintenanceForm, ClaimForm, ModelsMachineForm, ModelsEngineForm, ModelsTransmissionForm, \
    ModelsDriveAxleForm, ModelsSteeringBridgeForm, TypeMaintenanceForm, RecoveryMethodForm, FailureNodeForm
from .models import Machine, Maintenance, Claims, ModelsMachine, ModelsEngine, ModelsTransmission, ModelsDriveAxle, \
    ModelsSteeringBridge, TypeMaintenance, RecoveryMethod, FailureNode
from .serializers import MachineSerializer, MaintenanceSerializer, ClaimsSerializer


class Index(ListView):
    model = Machine
    template_name = 'first_page.html'
    context_object_name = 'machine'

    def get_queryset(self):
        if self.request.GET.get('factory_number_machine'):
            return self.queryset
        return Machine.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user.role == 'MN':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.all())
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.all())
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.all())
                return context
            elif self.request.user.role == 'CL':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.filter(
                                                                       client=self.request.user
                                                                   ))
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.filter(
                                                                               machine__client=self.request.user
                                                                           ))
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.filter(
                                                                   machine__client=self.request.user
                                                               ))
                return context
            elif self.request.user.role == 'SC':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.filter(
                                                                       service_company=self.request.user
                                                                   ))
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.filter(
                                                                               service_company=self.request.user
                                                                           ))
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.filter(
                                                                   machine__service_company=self.request.user
                                                               ))
                return context
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ModelsMachineListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_modelsmachine',)
    model = ModelsMachine
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsMachineUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_modelsmachine',)
    model = ModelsMachine
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsMachineForm
    success_url = reverse_lazy('models_machine')


class ModelsMachineCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_modelsmachine',)
    model = ModelsMachine
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsMachineForm
    success_url = reverse_lazy('models_machine')


class ModelsEngineListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_modelsengine',)
    model = ModelsEngine
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsEngineUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_modelsengine',)
    model = ModelsEngine
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsEngineForm
    success_url = reverse_lazy('models_engine')


class ModelsEngineCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_modelsengine',)
    model = ModelsEngine
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsEngineForm
    success_url = reverse_lazy('models_engine')


class ModelsTransmissionListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_modelstransmission',)
    model = ModelsTransmission
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsTransmissionUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_modelstransmission',)
    model = ModelsTransmission
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsTransmissionForm
    success_url = reverse_lazy('models_transmission')


class ModelsTransmissionCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_modelstransmission',)
    model = ModelsTransmission
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsTransmissionForm
    success_url = reverse_lazy('models_transmission')


class ModelsDriveAxleListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_modelsdriveaxle',)
    model = ModelsDriveAxle
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsDriveAxleUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_modelsdriveaxle',)
    model = ModelsDriveAxle
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsDriveAxleForm
    success_url = reverse_lazy('models_driveaxle')


class ModelsDriveAxleCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_modelsdriveaxle',)
    model = ModelsDriveAxle
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsDriveAxleForm
    success_url = reverse_lazy('models_driveaxle')


class ModelsSteeringBridgeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_modelssteeringbridge',)
    model = ModelsSteeringBridge
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsSteeringBridgeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_modelssteeringbridge',)
    model = ModelsSteeringBridge
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsSteeringBridgeForm
    success_url = reverse_lazy('models_steeringbridge')


class ModelsSteeringBridgeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_modelssteeringbridge',)
    model = ModelsSteeringBridge
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = ModelsSteeringBridgeForm
    success_url = reverse_lazy('models_steeringbridge')


class TypeMaintenanceListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_typemaintenance',)
    model = TypeMaintenance
    template_name = 'directory.html'
    context_object_name = 'models'


class TypeMaintenanceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_typemaintenance',)
    model = TypeMaintenance
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = TypeMaintenanceForm
    success_url = reverse_lazy('models_typemaintenance')


class TypeMaintenanceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_typemaintenance',)
    model = TypeMaintenance
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = TypeMaintenanceForm
    success_url = reverse_lazy('models_typemaintenance')


class RecoveryMethodListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_recoverymethod',)
    model = RecoveryMethod
    template_name = 'directory.html'
    context_object_name = 'models'


class RecoveryMethodUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_recoverymethod',)
    model = RecoveryMethod
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = RecoveryMethodForm
    success_url = reverse_lazy('models_recoverymethod')


class RecoveryMethodCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_recoverymethod',)
    model = RecoveryMethod
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = RecoveryMethodForm
    success_url = reverse_lazy('models_recoverymethod')


class FailureNodeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('Backend.change_failurenode',)
    model = FailureNode
    template_name = 'directory.html'
    context_object_name = 'models'


class FailureNodeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('Backend.change_failurenode',)
    model = FailureNode
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = FailureNodeForm
    success_url = reverse_lazy('models_failurenode')


class FailureNodeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_failurenode',)
    model = FailureNode
    template_name = 'update_models.html'
    context_object_name = 'models'
    form_class = FailureNodeForm
    success_url = reverse_lazy('models_failurenode')


class MyLogin(LoginView):
    template_name = 'account/login.html'


class MachineDetail(DetailView):
    model = Machine
    template_name = 'machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machine_maintenance'] = Maintenance.objects.filter(machine=self.kwargs.get('pk'))
        context['machine_claim'] = Claims.objects.filter(machine=self.kwargs.get('pk'))
        return context


class CreateMachineView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_machine',)
    template_name = 'create.html'
    form_class = MachineForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        User = get_user_model()
        form.instance.client = User.objects.get(id=self.request.user.id)
        return super(CreateMachineView, self).form_valid(form)


class CreateMaintenanceView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_maintenance',)
    template_name = 'create.html'
    form_class = MaintenanceForm
    success_url = reverse_lazy('index')


class CreateClaimView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_claims',)
    template_name = 'create.html'
    form_class = ClaimForm
    success_url = reverse_lazy('index')


class MachineApiView(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MaintenanceApiView(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ClaimsApiView(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer


from django.shortcuts import render

# Create your views here.
