from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("home.urls")),
    path("", include("core.urls")),

    path("auth/", include("accounts.urls")),
    path("fanlar/", include("education.urls")),
    path("kurslar/", include("courses.urls")),
    path("ota-onalar/", include("parents_content.urls")),
    path("vakansiyalar/", include("vacancies.urls")),
    path("aloqa/", include("contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
