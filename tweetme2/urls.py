"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include # url()
from django.views.generic import TemplateView

# from accounts.views import RegisterAPI
# from knox import views as knox_views
# from accounts.views import LoginAPI
# from django.urls import path



from Baseball.views import (
    Baseballhome_view,
    Baseballtweets_list_view,
    Baseballtweets_detail_view,
)

from Europa.views import (
    Europahome_view,
    Europatweets_list_view,
    Europatweets_detail_view,
)
from Formula1.views import (
    Formula1home_view,
    Formula1tweets_list_view,
    Formula1tweets_detail_view,
)






urlpatterns = [
    #path('api/', include('accounts.urls')),
    
    #path('', home_view),
    path('Baseball/', Baseballhome_view),
    path('Europa/', Europahome_view),
    path('Formula1/', Formula1home_view),
    path('admin/', admin.site.urls),
    path('react/', TemplateView.as_view(template_name='react.html')),
    #path('global/', tweets_list_view),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    # path('login/', login_view),
    # path('logout/', logout_view),
    # path('register/', register_view),

    path('Baseball/<int:tweet_id>/', Baseballtweets_detail_view),
    path('Europa/<int:tweet_id>/', Europatweets_detail_view),
    path('Formula1/<int:tweet_id>/', Formula1tweets_detail_view),
    #path('<int:tweet_id>', tweets_detail_view),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/Baseball/', include('Baseball.api.urls')),
    path('api/Europa/', include('Europa.api.urls')),
    path('api/Formula1/', include('Formula1.api.urls')),

    re_path(r'api/profiles?/', include('profiles.api.urls')),
    # path('tweets/', include('tweets.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                document_root=settings.MEDIA_ROOT)