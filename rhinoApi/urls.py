from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.all),
    path('search/',views.search),
    path('search/cat/',views.search_cat),

    path('signup/',views.signup),
    path('like/',views.like),
      path('dislike/',views.dislike),
     path('liked/',views.liked),
     path('orderplace/',views.orderPlace),
     path('ordered/',views.ordered),
    path('addrev/',views.addReview),
    path('showrev/',views.showReview),
    path('ranker/',views.ranker),
     path('news/',views.news),
     path('review/images/',views.reviewImage),
     path('userdata/',views.userdata),
     path('update/',views.user_update)


]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
