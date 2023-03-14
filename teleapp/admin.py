from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Profile) #profile บุคคล
admin.site.register(Team) #ชื่อทีม
admin.site.register(Product) #ผลงาน
admin.site.register(expenses) #เบิก

