from django.urls import path
from Myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('add_donor/', views.AddDonorView.as_view(), name='add-donor'),
    path('', views.DonorListView.as_view(), name='donor-list'),
    #path('filter/', views.FilterDonorView.as_view(), name='donor-filter'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search_donor/', views.SearchDonor, name='search-donor'),
    path('update/<int:id>/', views.DonorUpdate.as_view(), name='donor-update'),
    path('<int:id>/', views.DonorDelete.as_view(), name="delete-donor"),

]