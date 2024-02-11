from django.db import models

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	register_date = models.DateField(auto_now_add=True)

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.IntegerField()
	add_date = models.DateField(auto_now_add=True)

class Order(models.Model):
	customer = models.ForeignKey(Client, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	order_date = models.DateField(auto_now_add=True)