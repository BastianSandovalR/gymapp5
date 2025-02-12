"""
WSGI config for Crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Determina la ruta base del proyecto. En este caso, partimos del directorio actual (donde está wsgi.py),
# subimos dos niveles para llegar a la carpeta que contiene manage.py y la carpeta gymapp.
BASE_DIR = Path(__file__).resolve().parent.parent
# Agrega BASE_DIR al principio del sys.path para que Python encuentre la carpeta gymapp.
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crud.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
