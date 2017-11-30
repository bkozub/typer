from django.contrib import admin

from typer_app.models import Competition, Competition_Location, Ski_Jumper, Result

admin.site.register(Competition)
admin.site.register(Competition_Location)
admin.site.register(Ski_Jumper)
admin.site.register(Result)
# Register your models here.
