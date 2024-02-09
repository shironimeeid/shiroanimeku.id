
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks/', views.bookmark, name='bookmarks'),
    path('komikindo/', include('routers.web.komikindo')),
    path('otakudesu/', include('routers.web.otakudesu')),
    path('mangabat/', include('routers.web.mangabat')),
    path('komiku/', include('routers.web.komiku')),
    #path('bacakomik/', include('routers.web.bacakomik.urls')),
    path('api/komikindo/', include('routers.api.komikindo')),
    path('api/otakudesu/', include('routers.api.otakudesu')),
    path('api/mangabat/', include('routers.api.mangabat')),
    path('api/bacakomik/', include('routers.api.bacakomik')),
    path('api/komiku/', include('routers.api.komiku')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

handler404 = views.handle_not_found
handler400 = views.handle_bad_request
