from django.contrib import admin

from company.models import Person, Department

admin.site.register(Person)
admin.site.register(Department)
# Register your models here.
