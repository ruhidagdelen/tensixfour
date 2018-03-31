from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.coming_soon, name='coming_soon'),
    url(r'^thechemist$', views.coming_soon, name='coming_soon'),
    url(r'^thechemist/$', views.coming_soon, name='coming_soon'),
    url(r'^google16ce05cfac0fd7b4\.html$', views.confirmation, name='confirmation'),
    url(r'^.*$', views.not_found, name='not_found'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)