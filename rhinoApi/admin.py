from django.contrib import admin
from .models import Product
from .models import User
from .models import Order,Review,ReviewImages,News
from django.contrib import admin




admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(ReviewImages)
admin.site.register(News)