from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def descargar_pdf(request):
    # Ruta completa del archivo PDF
    pdf_path = os.path.join(settings.BASE_DIR, 'core/static/core/files/BernyVGResume.pdf')

    # Devolver el archivo como respuesta
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename='BernyVGResume.pdf')
