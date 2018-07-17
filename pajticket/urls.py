from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # accounts
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # tickets
    url(r'', include('tickets.urls', namespace='tickets')),
    
    # news
    url(r'', include('news.urls', namespace='news')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
