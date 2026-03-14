
# from django.urls import path
# from uploader import views

# urlpatterns = [
#     path('', views.upload_page, name='upload'),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from uploader import views

urlpatterns = [
    path('', views.upload_page, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)