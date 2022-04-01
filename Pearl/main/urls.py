from django.urls import path
from .views import GetUsersView, GetUserView

urlpatterns = [
    path('', GetUsersView.as_view()),
    path('<int:id>', GetUserView)
]