from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
import courserec.views



urlpatterns = [
    path("", courserec.views.index, name="index"),
    path('predict',courserec.views.predict,name="predict"),
    path('recommend/',courserec.views.recommends,name="recommends"),
    path("about/", courserec.views.about, name="about"),
    path("db/", courserec.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("recommendations/", courserec.views.recommend, name="recommend")
    
]
