from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def root(request):
    return JsonResponse({
        'message': 'AI Box Selection API',
        'routes': {
            'admin': '/admin/',
            'recommend_box': '/api/recommend-box/'
        }
    })


urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('api/', include('shipping.urls')),
]
