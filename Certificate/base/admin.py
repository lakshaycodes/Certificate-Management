from django.contrib import admin
from .models import Certificate
import random
import string


def generate_certificate_ids(modeladmin, request, queryset):
    for certificate in queryset:
        certificate.certificate_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        certificate.save()

generate_certificate_ids.short_description = "Generate Certificate IDs"

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'issued_date', 'certificate_id')
    actions = [generate_certificate_ids]
