from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

# Import all the models/classes what we have created.
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
