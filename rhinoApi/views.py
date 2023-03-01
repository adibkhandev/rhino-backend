from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Product,Review,Order,ReviewImages,News
from django.contrib.auth import get_user_model
import jwt

from .serializers import ProductSerializer,UserSerializer,UserOrderSerializer,OrderSerializer,ReviewSerializer,NewsSerializer,ReviewImagesSerializer
User = get_user_model()

@api_view(['GET'])
def all(request):
    products = Product.objects.all()
    ProductSerialized = ProductSerializer(products,many=True)
    return Response(ProductSerialized.data)

@api_view(['POST'])
def search(request):
    searched = request.data['searched']
    product = Product.objects.filter(name__contains=searched)
    ProductSerialized = ProductSerializer(product,many=True)
    return Response(ProductSerialized.data)

@api_view(['POST'])
def search_cat(request):
    category = request.data['category']
    product = Product.objects.filter(categories=category)
    ProductSerialized = ProductSerializer(product,many=True)
    return Response(ProductSerialized.data)


@api_view(['POST'])
def review(request):
    reviewKey = request.data['key']
    reviews = Review.objects.filter(product=reviewKey)
    reviewserialized = ReviewSerializer(reviews,many=true)
    return Response(reviewserialized.data) 


@api_view(['POST'])
def signup(request):
    sentdata = request.data['data']

  
    firstname = sentdata['firstname']
    lastname = sentdata['lastname']

    email = sentdata['email']
    phone_number =  sentdata['phonenumber']
    adress = sentdata['adress']
    password = sentdata['password']
    user = User.objects.create_user(email=email,first_name=firstname,last_name=lastname,password=password,adress=adress,phonenumber=phone_number)
    user.save() 
    return Response(user.first_name)

@api_view(['POST'])
def like(request):
    userID = request.data['userid']
    productID = request.data['productid']
    user = User.objects.get(id=userID)
    product = Product.objects.get(id=productID)
    print(userID)
    if user :
        user.liked.add(product)
        print(user.liked)
        serialized = UserSerializer(user,many=False)
        return Response(serialized.data)

@api_view(['POST'])
def dislike(request):
    userID = request.data['userid']
    productID = request.data['productid']
    user = User.objects.get(id=userID)
    product = Product.objects.get(id=productID)
    print(userID)
    if user :
        user.liked.remove(product)
        print(user.liked)
        serialized = UserSerializer(user,many=False)
        return Response(serialized.data)

@api_view(['POST'])
def liked(request):
    userid = request.data['id']
    user = User.objects.get(id=userid)
    product = UserSerializer(user,many=False)
    

    return Response(product.data)

# for placing orders
@api_view(['POST'])
def orderPlace(request):
    products = request.data['products']
    userid = request.data['userid']
    product_pk = products['id']
    product_count = products['count']
    user_instance = User.objects.get(id=userid)
    product_instance = Product.objects.get(id=product_pk)
    order_instance = Order.objects.create(user_id=userid,delicered=False,orderNumber=product_count)
    order_instance.save()
    order_instance.product.add(product_instance)
    order_instance.save()
    user_instance.ordered.add(order_instance)
    user_instance.save()
    serialized = UserSerializer(user_instance,many=False)
    return Response(serialized.data)

#for rendering orders

@api_view(['POST'])
def ordered(request):
    userid = request.data['userid']
    user = User.objects.get(id=userid)
    serialized = UserSerializer(user,many=False)


    return Response(serialized.data)

@api_view(['POST'])
def addReview(request):
  print(request.data)
  creater_id = request.data['userid']
  user_instance = User.objects.get(id=creater_id)
  user_name = user_instance.first_name +' '+ user_instance.last_name
  files = request.FILES
  image1 = files.get('image1')
  image2 = files.get('image2')
  image3 = files.get('image3')
  review = request.data['writing']
  rating = request.data['star']
  product_id = request.data['pk']
  product_instance = Product.objects.get(id=product_id)
  review_instance = Review.objects.create(creater_pfp=user_instance.profile_pic,creater_name=user_name,review=review,rating=rating)
  review_instance.save()
  if image1 is not None:
    image_instance = ReviewImages.objects.create(review=review_instance,image=image1)
    image_instance.save()
    files = request.FILES
    image = files.get('image')
    print(image)
    print('done')
    if image2 is not None:
      image_instance = ReviewImages.objects.create(review=review_instance,image=image2)
      image_instance.save() 
      if image3 is not None:
        image_instance = ReviewImages.objects.create(review=review_instance,image=image3)
        image_instance.save()

  
  else:
    print('serialize')
  product_instance.rev.add(review_instance)
  product_instance.save()
  product_serialized = ProductSerializer(product_instance,many=False)
  return Response(product_serialized.data)    
@api_view(['POST'])
def showReview(request):
    review_key = request.data['pk']
    review_instance = Review.objects.get(id=review_key)
    review = ReviewSerializer(review_instance,many=False)
    return Response(review.data)

@api_view(['POST'])
def reviewImage(request):
    print(request.data)
    Id = request.data['id']
    images = ReviewImages.objects.filter(review=Id)
    serialized = ReviewImagesSerializer(images,many=True)
    return Response(serialized.data)
@api_view(['GET'])
def ranker(request):
    all_products = Product.objects.order_by('-ordered')
    serialized = ProductSerializer(all_products,many=True)
    return Response(serialized.data)
@api_view(['GET'])
def news(request):
    news = News.objects.all()
    serialized = NewsSerializer(news,many=True)
    return Response(serialized.data)

@api_view(['POST'])
def userdata(request):
    Id = request.data['id']
    instance = User.objects.get(id=Id)
    serialized = UserSerializer(instance,many=False)
    
    return Response(serialized.data)

@api_view(['POST'])
def user_update(request):
    print(request.data)
    user_id = request.data['id']
    user_instance = User.objects.get(id=user_id)
    user_serialized = UserSerializer(user_instance,many=False)
    files = request.FILES
    pfp = files.get('pfp')
    # username = request.data['username']
    # number = request.data['number']
    # mail = request.data['mail']
    # adress = request.data['adress']
    if pfp:
       user_instance.profile_pic = pfp
       user_instance.save()
       return Response(user_serialized.data)
    if 'number' in request.data:
       number = request.data['number'] 
       user_instance.phonenumber = number
       user_instance.save()
       return Response(user_serialized.data)
    if 'mail' in request.data:
       mail = request.data['mail']
       user_instance.email = mail
       user_instance.save()
       return Response(user_serialized.data)
    if 'adress' in request.data:

       adress = request.data['adress']
       user_instance.adress = adress
       user_instance.save()
       return Response(user_serialized.data)
        
    else:
        print('nai')
        print(request.data,pfp)
        return Response(user_serialized.data)