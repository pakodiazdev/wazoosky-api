import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------
# 🔧 Directorio base del proyecto
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# 🌍 Entorno actual: dev, test, prod...
# ---------------------------
env_name = os.getenv("DJANGO_ENV", "dev").lower()
env_file = f".env.{env_name}"

# 🔄 Cargar archivo .env.{env_name} si existe, si no usar .env
dotenv_path = BASE_DIR / env_file
if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)
else:
    load_dotenv(dotenv_path=BASE_DIR / ".env")

# ---------------------------
# 🔐 Seguridad y entorno
# ---------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
USE_CUSTOM_SWAGGER_UI = os.getenv("USE_CUSTOM_SWAGGER_UI", "true").lower() == "true"
FAKE_REGISTER_PASSWORD = os.getenv("FAKE_REGISTER_PASSWORD", "Test1234!")
ALLOWED_HOSTS = (
    os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else []
)

# ---------------------------
# 🗄️ Configuración de base de datos
# ---------------------------
APP_PREFIX = os.getenv("APP_PREFIX", "wazoosky")
DB_NAME = os.getenv("DB_NAME", f"{APP_PREFIX}_db")
DB_USER = os.getenv("DB_USER", os.getenv("POSTGRES_USER", "admin"))
DB_PASSWORD = os.getenv("DB_PASSWORD", os.getenv("POSTGRES_PASSWORD", "Wazoosky!123"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# ---------------------------
# ⚙️ Configuración de aplicaciones
# ---------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ---------------------------
# 🎨 Templates
# ---------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------
# 🔒 Validaciones de contraseña
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.",
            "UserAttributeSimilarityValidator",
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------
# 🌐 Internacionalización
# ---------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---------------------------
# 📁 Archivos estáticos
# ---------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ---------------------------
# 🧩 Configuración de DRF
# ---------------------------
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# ---------------------------
# 📚 Swagger UI
# ---------------------------
SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": None if USE_CUSTOM_SWAGGER_UI else "SIDECAR",
    "REDOC_DIST": None,
}

# ---------------------------
# 🔐 Configuración de JWT
# ---------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ---------------------------
# 👤 Modelo de usuario personalizado
# ---------------------------
AUTH_USER_MODEL = "users.User"

# ---------------------------
# 🆔 Campo por defecto para primary key
# ---------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
