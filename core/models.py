from django.db import models
import os
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db.models.signals import post_save
from django import forms

class HWFiles(models.Model):
    hw_title = models.CharField(max_length=255)
    file = models.FileField(upload_to='hw_files/')
    
    STATUS_CHOICES = [
        ('checked', 'Checked'),
        ('unchecked', 'Unchecked'),
        ('okay', 'Okay'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unchecked')

    def __str__(self):
        return self.hw_title

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')

    class Meta:
        unique_together = ('name', 'parent_folder')

    def __str__(self):
        return self.name

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='')

    def save(self, *args, **kwargs):
        if self.folder:
            # Build the full folder path by traversing the folder hierarchy
            folder_path = self.folder.name
            parent_folder = self.folder.parent_folder

            # Traverse up the folder hierarchy to get the full path
            while parent_folder:
                folder_path = os.path.join(parent_folder.name, folder_path)
                parent_folder = parent_folder.parent_folder

            # Join the 'files' directory with the constructed folder path
            self.file.name = os.path.join('files', folder_path, self.file.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    mobile_no = models.CharField(max_length=11, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    picture = models.ImageField(upload_to='users/', null=True, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Hash the password before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.role}"

@receiver(post_save, sender=UserProfile)
def create_user_for_users(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(username=instance.mobile_no)
        user.password = instance.password
        user.save()

        instance.user = user
        instance.save()

class Exam(models.Model):
    title = models.CharField(max_length=255)
    question = models.FileField(upload_to='')
    start_time = models.DateTimeField()
    duration = models.DurationField()
    student = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('okay', 'Okay'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.title:
            self.question.name = os.path.join('questions', self.title, self.question.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class AnswerScript(models.Model):
    answer = models.FileField(upload_to='')
    question = models.ForeignKey(Exam, on_delete=models.CASCADE,  null=True, blank=True)

    STATUS_CHOICES = [
        ('checked', 'Checked'),
        ('unchecked', 'Unchecked'),
        ('okay', 'Okay'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unchecked')

    def save(self, *args, **kwargs):
        if self.question.title:
            self.answer.name = os.path.join('answers', self.question.title, self.answer.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question.title