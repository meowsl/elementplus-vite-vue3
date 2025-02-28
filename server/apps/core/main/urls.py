from django.urls import include, path, re_path

from .views import MainRedirectView

urlpatterns = [
    path("", MainRedirectView.as_view()),
    re_path(r"^ckeditor5/", include("django_ckeditor_5.urls")),
    path("api/", include("apps.core.api.urls"), name="api"),
]
