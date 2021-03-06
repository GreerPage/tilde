"""tilde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as homeviews
from gallery import views as gallery
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from post import views as postviews
from . import views as rootviews

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', homeviews.index),
    path('gallery', gallery.index),
    path('gallery/', gallery.index),
    path('post', postviews.index),
    path('p/<str:postname>', gallery.postPage),
    path('p', gallery.p),
    path('post/', postviews.index),
    path('p/<str:postname>/', gallery.postPage),
    path('p/', gallery.p),
    path('e/<str:errornum>/<str:error>', rootviews.error)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
handler404 = rootviews.error_404
handler500 = rootviews.error_500
handler403 = rootviews.error_403
handler400 = rootviews.error_400

