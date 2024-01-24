from django.urls import path
from inventory.views import BookAPIView,AuthorAPIView,ComplementryItemAPIView,BrandAPIView


urlpatterns = [
    path('books/',BookAPIView.as_view({'get':'list','post':'create'}),name='books'),
    path('authors/',AuthorAPIView.as_view({'get':'list','post':'create'}),name='authors'),
    path('complemetry-items/',ComplementryItemAPIView.as_view({'get':'list','post':'create'}),name='complementry-items'),
    path('brands&publications/',BrandAPIView.as_view({'get':'list','post':'create'}), name='brand-or-publications'),
]
