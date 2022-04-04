from django.db import models

# Create your models here.
class user_type(models.Model):
	u_type = models.CharField(max_length=20)

	def __str__(self):
		return self.u_type

	class Meta:
		verbose_name_plural = "User Type"

class req_user(models.Model):
	user_id = models.IntegerField()
	email = models.CharField(max_length=50)
	passwrd = models.CharField(max_length=20)
	c_name = models.CharField(max_length=30)
	uname = models.CharField(max_length=40)
	phno = models.BigIntegerField()

	def __str__(self):
		return self.email

	class Meta:
		verbose_name_plural = "Users"

class tender_type(models.Model):
	t_type = models.CharField(max_length=10)

	def __str__(self):
		return self.t_type

	class Meta:
		verbose_name_plural = "Tender Type"

class category_type(models.Model):
	t_type_id = models.IntegerField()
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = "Category Type"

class t_request(models.Model):
	u_id = models.IntegerField()
	prj_name = models.CharField(max_length=50)
	t_type = models.IntegerField()
	category =models.IntegerField()
	prj_desc = models.TextField()
	reg_price = models.IntegerField()

	def __str__(self):
		return self.prj_name

	class Meta:
		verbose_name_plural = "Requested Tenders"

class bid_request(models.Model):
	whos_tender = models.IntegerField()
	tender_id = models.IntegerField()
	org_name = models.CharField(max_length=50)
	org_file = models.FileField(upload_to='C:/Python/Webtechlab/wtech_tender/tendermanagement/static/company_docx/')
	time = models.IntegerField()
	cost = models.IntegerField()
	who_bid_for_it = models.IntegerField()

	def __str__(self):
		return self.org_name

	class Meta:
		verbose_name_plural = "Tender Bids"

class card_details(models.Model):
	user_id = models.IntegerField()
	card_owner = models.CharField(max_length=50)
	card_number = models.CharField(max_length=20)
	exp_month = models.CharField(max_length=50)
	exp_year = models.IntegerField()

	def __str__(self):
		return self.card_owner

	class Meta:
		verbose_name_plural = "Card Details"

class feedback(models.Model):
	uname = models.CharField(max_length=40)
	email = models.CharField(max_length=50)
	subject = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.subject

	class Meta:
		verbose_name_plural = "Feedback"

class admin_users(models.Model):
	name = models.CharField(max_length=40)
	pwrd = models.CharField(max_length=40)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Admin"