from django.shortcuts import get_object_or_404, render, redirect
from django.http import FileResponse
from .models import Certificate
from .utils import generate_certificate_pdf
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def download_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id)

    # Generate the PDF dynamically
    file_path = generate_certificate_pdf(certificate)

    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def verify_certificate(request):
    certificate = None
    error_message = None

    if request.method == "POST":
        certificate_id = request.POST.get("certificate_id")
        try:
            certificate = Certificate.objects.get(certificate_id=certificate_id)
        except Certificate.DoesNotExist:
            error_message = "Invalid Certificate ID. Please check and try again."

    return render(request, "verify_certificate.html", {"certificate": certificate, "error_message": error_message})

@login_required
def my_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, "my_certificates.html", {"certificates": certificates})

def user_login(request):
    if request.user.is_authenticated:  
        return redirect("my_certificates")  # Redirect logged-in users to their certificates page

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("my_certificates")  # Redirect to certificates page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})

'''def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")'''