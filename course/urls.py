from django.urls import path
from . import views 
urlpatterns = [
    path('registercourse/',views.register_course,name="register_course"),
    path("list/",views.course_list,name="course_list"),
    path("profile/<int:id>",views.course_profile,name="course_profile"),
    path("edit/<int:id>",views.edit_course,name="edit_course"),

]
