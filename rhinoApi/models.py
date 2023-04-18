from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class Review(models.Model):
	creater_id = models.IntegerField(null=True)
	creater_pfp = models.ImageField(upload_to="images",null=True)
	creater_name = models.CharField(max_length=20)
	review = models.TextField()
	rating = models.IntegerField()
class Product(models.Model):
	name = models.CharField(max_length=40)
	price = models.IntegerField()
	image = models.ImageField(upload_to='images')
	ordered = models.IntegerField()
	story = models.TextField()
	categories = models.CharField(max_length=20)
	rev = models.ManyToManyField(Review,  blank=True)
class News(models.Model):
	news_title = models.CharField(max_length=30)
	news_header = models.CharField(max_length=40)
	product = models.OneToOneField(Product,on_delete=models.CASCADE)
    
class ReviewImages(models.Model):
	review = models.ForeignKey(Review,null=True,on_delete=models.CASCADE,related_name='images')
	image = models.ImageField(upload_to='images')


class Order(models.Model):
	user_id = models.IntegerField()
	product = models.ManyToManyField(Product)
	delicered = models.BooleanField(default=False)
	orderNumber = models.IntegerField()

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Users require an email field')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
	username = None
	profile_pic = models.ImageField(null=True,upload_to='images')
	email = models.EmailField(unique=True)
	phonenumber = models.IntegerField(null=True)
	adress = models.TextField(null=True)
	objects = UserManager()
	liked = models.ManyToManyField(Product)
	ordered = models.ManyToManyField(Order)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
