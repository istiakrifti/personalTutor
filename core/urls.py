from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('auto-submit/', views.auto_submit_view, name='auto_submit'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('live-class/', views.live_class_view, name='live_class'),
    path('upload-hw/', views.upload_hw_view, name='upload_hw'),
    path('check-hw/', views.upload_checked_hw_view, name='check_hw'),
    path('check-script/', views.upload_checked_scripts_view, name='check_script'),
    path('show-unchecked-hw/', views.show_unchecked_hw_view, name='show_unchecked_hw'),
    path('show-unchecked-scripts/', views.show_unchecked_scripts_view, name='show_unchecked_scripts'),
    path('show-checked-hw/', views.show_checked_hw_view, name='show_checked_hw'),
    path('show-checked-script/', views.show_checked_scripts_view, name='show_checked_script'),
    path('add-files/', views.add_files_view, name='add_files'),
    path('show-files/', views.show_files_view, name='show_files'),
    path('show-files/<int:folder_id>/', views.show_files_view, name='show_files'),
    path('add-files/<int:folder_id>/', views.add_files_view, name='add_files'),
    path('create-folder/<int:folder_id>/', views.create_folder, name='create_folder'),
    path('upload-file/<int:folder_id>/', views.upload_file, name='upload_file'),
    path('edit_file/<int:file_id>/', views.edit_file, name='edit_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete-folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('take-exam/', views.exam_form_view, name='take_exam'),
    path('attend-exam/', views.attend_exam_view, name='attend_exam'),
    path('exam-list/', views.exam_list_view, name='exam_list'),
    path('edit-exam/<int:exam_id>/', views.edit_exam_view, name='edit_exam'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)