from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class Profile(models.Model):
		user = models.OneToOneField(User,on_delete=models.CASCADE)#การใช้ .OneToOneField คือ การอ้างอิงถึง field ของ tadateble อื่น ในที่นี้ อ้างอิงถึง data table User หากมีการลบให้ลบตรงนี้ด้วย
		photo = models.ImageField(upload_to = 'photo_profile',null=True,blank=True,default='default.png')
		usertype = models.CharField(max_length = 100,default='Telesale')
		def __str__ (self):
			return str(self.user)
		

class TeamStat(models.Model):

	telesale_team = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	commu_team1 = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	commu_team2 = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	online_team = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	mynmar_team = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	duckbet = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	mughauy = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	slak_thai = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	phone_number = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	quality = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	interest = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	inwork = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	absent = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	employee = models.IntegerField(max_length=10,null=True,blank=True,default=0)
	stamp = models.DateField(auto_now_add=True,null=True,blank=True)
	
	def __str__ (self):
			return str(f'รายงานประจำวันที่ ')+str(self.stamp)




		