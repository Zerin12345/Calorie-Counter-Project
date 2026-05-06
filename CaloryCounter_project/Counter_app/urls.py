from django.urls import path
from .views import*

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('dashboard/',dashboard, name='dashboard'),
    path('logout/', logout_page, name='logout_page'),
    path('profile/', profile_page, name='profile_page'),
    path('update/', update_page, name='update_page'),
    path('consumed_calorie/', consumed_calories, name='consumed_calories'),
    path('add_calorie/', add_calorie, name='add_calorie'),
    path('edit_calorie/<str:id>/', edit_calorie, name='edit_calorie'),
    path('delete_calorie/<str:id>/', delete_calorie, name='delete_calorie'),
]
