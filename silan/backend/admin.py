from django.contrib import admin

from .models import ModelsMachine, ModelsEngine, ModelsTransmission, ModelsDriveAxle, ModelsSteeringBridge, \
    Machine, TypeMaintenance, Maintenance, RecoveryMethod, FailureNode, Claims, User

admin.site.register(ModelsMachine)
admin.site.register(ModelsEngine)
admin.site.register(ModelsTransmission)
admin.site.register(ModelsDriveAxle)
admin.site.register(ModelsSteeringBridge)
# admin.site.register(ServiceCompany)
admin.site.register(Machine)
admin.site.register(TypeMaintenance)
admin.site.register(Maintenance)
admin.site.register(RecoveryMethod)
admin.site.register(FailureNode)
admin.site.register(Claims)


# admin.site.register(User)


@admin.register(User)
class User(admin.ModelAdmin):
    fields = ('username', 'email', 'password',
              'role',
              'name', 'description',)


from django.contrib import admin

# Register your models here.
