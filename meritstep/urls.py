from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from meritapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('courses/', views.courses),
    path('course_details/<int:id>', views.course_details),
    path('corporate/', views.corporate),
    path('instructor/', views.instructor),
    path('support/', views.support),
    path('staffing/', views.staffing),
    path('blog/', views.blog),
    path('blog_detail/', views.blog_detail),
    path('contact/', views.contact),
    path('send', views.send),
    path('send1', views.send1),
    path('contact1', views.contact1),
    path('modal', views.modal),
    path('homecontact', views.homecontact),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
