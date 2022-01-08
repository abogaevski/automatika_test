from django.urls import path
from .views import StoreListApiView, VisitStoreApiView

urlpatterns = [
    path('list/<str:phone>', StoreListApiView.as_view(), name='store_list_url'),
    path('visit/<str:phone>', VisitStoreApiView.as_view(), name='store_visit_url')
]
