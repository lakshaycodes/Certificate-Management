from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

def generate_certificate_pdf(name, course, certificate_id):
    file_path = f"certificates/{certificate_id}.pdf"
    c = canvas.Canvas(file_path, pagesize=landscape(A4))
    
    width, height = landscape(A4)
    
    # Background
    c.setFillColor(colors.lightgrey)
    c.rect(30, 30, width-60, height-60, stroke=1, fill=0)
    
    # Title
    c.setFillColor(colors.black)
    c.setFont("Times-Bold", 36)
    c.drawCentredString(width/2, height-100, "Certificate of Completion")
    
    # Name
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(width/2, height-200, name)
    
    # Course Details
    c.setFont("Helvetica", 20)
    c.drawCentredString(width/2, height-250, f"Has successfully completed the course:")
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(width/2, height-280, course)
    
    # Certificate ID & Date
    c.setFont("Helvetica", 16)
    c.drawCentredString(width/2, height-350, f"Certificate ID: {certificate_id}")
    
    # Signature Line
    c.line(100, 100, 300, 100)
    c.setFont("Helvetica", 14)
    c.drawString(100, 80, "Authorized Signature")
    
    # Save PDF
    c.save()
    return file_path
