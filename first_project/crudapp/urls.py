from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
    path("view/", views.view, name="view"),
    path("update_user/<int:id>/", views.update_user, name="update_user")
]