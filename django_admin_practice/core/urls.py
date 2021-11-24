"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog.admin import blog_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# admin.site.index_title = "초기화면"                  # 초기화면 title, default=null
# admin.site.site_header = 'Greeners 관리자 페이지'    # html header 이름, default=Django 관리
# admin.site.site_title = "Greeners 관리자 페이지"     # tab 이름 , default=Django 관리
# admin.site.site_url = '/hi'                         # 오른쪽 위에서 사이트보기 누리면 이동하는 url, default='/'