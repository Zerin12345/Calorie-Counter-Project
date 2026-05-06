from django.contrib import admin
from Counter_app.models import*

# Register your models here.
admin.site.register(User)
admin.site.register(BasicInfoModel)
admin.site.register(ConsumedCalories)

