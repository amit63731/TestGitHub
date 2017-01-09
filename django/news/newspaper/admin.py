from django.contrib import admin

# Register your models here.
from .models import Histograph, SignUp
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse



def export_csv(modeladmin, request, queryset):            # function defination
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
  writer = csv.writer(response, csv.excel)
  response.write(u'\ufeff'.encode('utf8'))
  # BOM (optional...Excel needs it to open UTF-8 file properly)
  writer.writerow([
    smart_str(u"First Name"),
    smart_str(u"Last Name"),
    smart_str(u"Email"),
  ])
  for obj in queryset:
    writer.writerow([
      smart_str(obj.first_name),
      smart_str(obj.last_name),
      smart_str(obj.email),
    ])
  return response
  export_csv.short_description = u"Export CSV"



class SignUpAdmin(admin.ModelAdmin):
    actions = [export_csv]                              # function call

admin.site.register(SignUp, SignUpAdmin)

admin.site.register(Histograph)
