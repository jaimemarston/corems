from django.contrib import admin
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from django.apps import apps

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()


for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        #if 'django.contrib.sessions.models.Session' == model:
        #print (model)
        admin.site.register(model, admin_class)
        
    except admin.sites.AlreadyRegistered:
        pass



admin.site.unregister(Session)
admin.site.unregister(ContentType)
admin.site.unregister(LogEntry)
