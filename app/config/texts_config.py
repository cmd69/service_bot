"""
Configuración del sistema de textos
Todas las rutas y configuraciones se obtienen desde variables de entorno
"""
import os

# Configuración del sistema de textos desde variables de entorno
TEXTS_CONFIG = {
    # Rutas de archivos de textos
    "custom_texts_path": os.getenv("CUSTOM_TEXTS_PATH", "/app/texts/custom_texts.json"),
    "generic_texts_path": os.getenv("GENERIC_TEXTS_PATH", "/app/texts/generic_texts.json"),
    
    # Configuración del sistema
    "fallback_to_generic": os.getenv("TEXTS_FALLBACK_TO_GENERIC", "true").lower() == "true",
    "auto_reload": os.getenv("TEXTS_AUTO_RELOAD", "false").lower() == "true",
    "encoding": os.getenv("TEXTS_ENCODING", "utf-8"),
    
    # Configuración de logging
    "verbose_logging": os.getenv("TEXTS_VERBOSE_LOGGING", "true").lower() == "true"
}
