from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
		user = models.OneToOneField(User,on_delete=models.CASCADE)#การใช้ .OneToOneField คือ การอ้างอิงถึง field ของ tadateble อื่น ในที่นี้ อ้างอิงถึง data table User หากมีการลบให้ลบตรงนี้ด้วย
		photo = models.ImageField(upload_to = 'photo_profile',null=True,blank=True,default='default.png')
		usertype = models.CharField(max_length = 100,default='Telesale')
		def __str__ (self):
			return str(self.user)