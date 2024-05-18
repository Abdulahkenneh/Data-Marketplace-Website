from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.homepage, name='homepage'),
    path('education/',views.education_view,name='education'),
    path('research/',views.research_view,name='research'),
    path('innovations/',views.innovations_view,name='innovation'),
    path('admission/',views.admission_view,name='admission'),
    path('campuslife/',views.campuslife_view,name='campus'),
    path('news/',views.news_view,name='news'),
    path('alumini/',views.alumni_view,name='alumni')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

app_name='university'