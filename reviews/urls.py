from django.urls import path
from reviews.apps import ReviewsConfig
from reviews.views import ReviewListAPIView, ReviewCreateAPIView, ReviewDetailAPIView, ReviewUpdateAPIView, \
    ReviewDeleteAPIView

app_name = ReviewsConfig.name


urlpatterns = [
    path('', ReviewListAPIView.as_view(), name='review-list'),
    path('create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('update/<int:pk>/', ReviewUpdateAPIView.as_view(), name='review-update'),
    path('delete/<int:pk>/', ReviewDeleteAPIView.as_view(), name='review-delete'),

]
