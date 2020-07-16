from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from django.conf.urls.static import static
urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('accounts/', include('accounts.urls')),
    path('board/', include('board.urls')),
    path('support/', include('support.urls')),
    # path('notice/', include('notice.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

from . import settings
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)