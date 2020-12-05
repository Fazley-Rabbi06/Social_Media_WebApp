from App_Login import views
from django.urls import path

app_name = "app_login"

urlpatterns = [
path('signup/',views.sign_up,name="signup"),
path('login/',views.login_page,name="login"),
path('edit_profile/',views.edit_profile,name="edit_profile"),
path('logout/',views.logout_user,name='logout'),
path('profile',views.profile,name='profile'),
path('other_user/<username>/',views.other_user,name="other_user"),
path('follow/<username>/',views.follow,name='follow'),
path('unfollow/<username>/',views.unfollow,name='unfollow'),
]