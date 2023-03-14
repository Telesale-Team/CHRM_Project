from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)#การใช้ .OneToOneField คือ การอ้างอิงถึง field ของ tadateble อื่น ในที่นี้ อ้างอิงถึง data table User หากมีการลบให้ลบตรงนี้ด้วย
	photo = models.ImageField(upload_to = 'photo_profile',null=True,blank=True,default='default.png')
	usertype = models.CharField(max_length = 100,default='member')
	salary = models.IntegerField(default=1)

	def __str__ (self):
		return str(f'Profile พนักงาน :')+str(self.user)
		
class Team(models.Model):

	team = models.CharField(max_length=255,unique=True) # ชื่อทีม
	members = models.IntegerField(default=1) # จำนวนคน

	def __str__(self):
		return  str(self.team)


class Product(models.Model): #สินค้า
	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	
	duckbet = models.IntegerField(default=0) #เว็บดั๊กเบ็ท
	mughauy = models.IntegerField(default=0) #เว็บมักหวย
	thailotto = models.IntegerField(default=0) #เว็บสลากไท
	member = models.IntegerField(default=0) #จำนวนสมาชิก

	#-----------------------------------#

	room_fee = models.IntegerField(default=0) #ค่าห้องพนักพนักงาน
	income = models.IntegerField(default=0) # รายได้
	expenses = models.IntegerField(default=0) #รายจ่าย
	total = models.IntegerField(default=0) # รายรับรวม
	create = models.DateTimeField(auto_now_add=True,null=True,blank=True)



	def __str__(self):
		return str(self.team,)
	

class expenses(models.Model): #"ค่าใช้จ่ายบุคคล"
	user = models.ForeignKey(Team,on_delete=models.CASCADE) # ผู้เบิก

	room_fee = models.IntegerField(default=0) #เอกสาร
	income = models.IntegerField(default=0) # จำนวนเงินที่เบิก
	expenses = models.IntegerField(default=0) #ธนาคาร
	account_bank = models.IntegerField()

	create = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	total = models.IntegerField(default=0) #จำนวนเงินรวม


	def __str__(self):
		return str(self.user)	

	



	
