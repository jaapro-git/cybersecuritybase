from django.urls import path
from csb_app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.timesheet, name="timesheet"),
    path("newentry/", views.newentry, name="newentry"),
    path("newpw/", views.newpw, name="newpw"),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(next_page='/'))
]