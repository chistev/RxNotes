from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)  # No auto update

    def save(self, *args, **kwargs):
        if self.pk:  # This ensures it's an update and not a new note
            self.updated_at = timezone.now()  # Manually set updated_at when saving an existing note
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
