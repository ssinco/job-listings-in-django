from django.urls import path, include
from . import views # Import views to connect routes to view functions


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),   

    # Routes for profiles
    path('profiles/', views.profile_index, name ='profile-index'),
    path('profiles/<int:profile_id>', views.profile_detail, name ='profile-detail'),
    path('profiles/create/',views.ProfileCreate.as_view(), name ='profile-create'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name ='profile-update'),   
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name ='profile-delete'),   

    # Routes for job history
    path('job-history/create/',views.JobHistoryCreate.as_view(), name ='job-history-create'),
    path('job-history/<int:pk>/update/', views.JobHistoryUpdate.as_view(), name ='job-history-update'),   
    path('job-history/<int:pk>/delete/', views.JobHistoryDelete.as_view(), name ='job-history-delete'),   

    # Routes for education
    path('edu-history/create/',views.EduHistoryCreate.as_view(), name ='edu-history-create'),
    path('edu-history/<int:pk>/update/', views.EduHistoryUpdate.as_view(), name ='edu-history-update'),   
    path('edu-history/<int:pk>/delete/', views.EduHistoryDelete.as_view(), name ='edu-history-delete'),   

    # Routes for company
    path('companies/', views.company_index, name ='company-index'),
    path('company/create/',views.CompanyCreate.as_view(), name ='company-create'),

]