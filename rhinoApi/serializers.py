from rest_framework import serializers
from .models import Product,Review,Order,Review,ReviewImages,News
from django.contrib.auth import get_user_model
User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Review
		fields = '__all__'
class ReviewImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReviewImages
		fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
	rev = ReviewSerializer(many=True)
	class Meta:
		model = Product
		fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
	product = ProductSerializer(required=True)
	class Meta:
		model = News
		fields = ('news_title','news_header','product')

class OrderSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True)
	class Meta:
		model = Order
		fields = ('delicered','orderNumber','product')

class UserSerializer(serializers.ModelSerializer):
	liked = ProductSerializer(many=True)
	ordered = OrderSerializer(many=True)
	class Meta:
		model = User
		fields = '__all__'
class UserOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['ordered','id']

	

class ReviewSerializer(serializers.ModelSerializer):
	images = ReviewImagesSerializer(many=True)
	class Meta:
		model = Review
		fields = ('creater_name','review','rating','images')
