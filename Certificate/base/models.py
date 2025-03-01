from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Certificate(models.Model):
    certificate_id = models.CharField(max_length=20, unique=True, blank=True)  # Unique ID
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    issued_date = models.DateField(auto_now_add=True)
    pdf_file = models.FileField(upload_to="certificates/", blank =True)

    def save(self, *args, **kwargs):
        if not self.certificate_id:  # Generate only if not set
            self.certificate_id = str(uuid.uuid4().hex[:10]).upper()  # Unique 10-char ID
        super().save(*args, **kwargs)