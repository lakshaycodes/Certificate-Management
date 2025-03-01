import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.conf import settings

def generate_certificate_pdf(certificate):
    # Define the directory path for storing certificates
    cert_dir = os.path.join(settings.MEDIA_ROOT, "certificates")
    
    # Ensure the directory exists
    if not os.path.exists(cert_dir):
        os.makedirs(cert_dir)

    # Define file path
    file_path = os.path.join(cert_dir, f"{certificate.user.username}_{certificate.certificate_id}.pdf")

    # Generate PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 20)

    # Certificate Title
    c.drawString(200, 700, "Certificate of Achievement")

    # Recipient Name
    c.setFont("Helvetica", 16)
    c.drawString(200, 650, f"Awarded to: {certificate.user.get_full_name()}")

    # Course Title
    c.drawString(200, 600, f"For completing: {certificate.title}")

    # Issued Date & ID
    c.drawString(200, 550, f"Issued on: {certificate.issued_date}")
    c.drawString(200, 500, f"Certificate ID: {certificate.certificate_id}")

    # Save PDF
    c.save()
    return file_path
