"""
Sistema de gestión de textos para el bot
Permite cargar textos personalizados desde archivos externos o usar textos genéricos
"""
import os
import json
from typing import Dict, Any, Optional
from pathlib import Path
from .texts_config import TEXTS_CONFIG

class TextManager:
    """Gestor de textos del bot"""
    
    def __init__(self, custom_texts_path: Optional[str] = None):
        """
        Inicializa el gestor de textos
        
        Args:
            custom_texts_path: Ruta al archivo de textos personalizados (opcional)
        """
        self.custom_texts_path = custom_texts_path or TEXTS_CONFIG["custom_texts_path"]
        self.encoding = TEXTS_CONFIG["encoding"]
        self.fallback_to_generic = TEXTS_CONFIG["fallback_to_generic"]
        self.texts = self._load_texts()
    
    def _load_texts(self) -> Dict[str, Any]:
        """Carga los textos desde archivos personalizados o usa los genéricos"""
        # Intentar cargar textos personalizados
        if os.path.exists(self.custom_texts_path):
            try:
                with open(self.custom_texts_path, 'r', encoding=self.encoding) as f:
                    custom_texts = json.load(f)
                    if TEXTS_CONFIG["verbose_logging"]:
                        print(f"✅ Textos personalizados cargados desde {self.custom_texts_path}")
                    return custom_texts
            except Exception as e:
                if TEXTS_CONFIG["verbose_logging"]:
                    print(f"⚠️ Error cargando textos personalizados: {e}")
                if self.fallback_to_generic:
                    if TEXTS_CONFIG["verbose_logging"]:
                        print("📝 Usando textos genéricos como fallback")
                else:
                    raise e
        
        # Usar textos genéricos como fallback
        if self.fallback_to_generic:
            if TEXTS_CONFIG["verbose_logging"]:
                print("📝 Usando textos genéricos (no se encontraron textos personalizados)")
            return self._get_generic_texts()
        else:
            raise FileNotFoundError(f"No se encontraron textos personalizados en {self.custom_texts_path}")
    
    def _get_generic_texts(self) -> Dict[str, Any]:
        """Carga textos genéricos desde archivo configurado"""
        generic_texts_path = TEXTS_CONFIG["generic_texts_path"]
        
        try:
            with open(generic_texts_path, 'r', encoding=self.encoding) as f:
                generic_texts = json.load(f)
                if TEXTS_CONFIG["verbose_logging"]:
                    print(f"✅ Textos genéricos cargados desde {generic_texts_path}")
                return generic_texts
        except Exception as e:
            if TEXTS_CONFIG["verbose_logging"]:
                print(f"⚠️ Error cargando textos genéricos: {e}")
            # Fallback a textos hardcoded mínimos si falla la carga del archivo
            return {
                "bot": {"name": "JellyBot"},
                "welcome": {"title": "🤖 ¡Hola! Soy {bot_name}", "description": "Bot de servicios premium"},
                "buttons": {"back_to_main": "Volver al Menú Principal ⬅️"}
            }
    
    def get(self, key_path: str, **kwargs) -> str:
        """
        Obtiene un texto por su ruta de claves
        
        Args:
            key_path: Ruta del texto (ej: "welcome.title")
            **kwargs: Variables para formatear el texto
            
        Returns:
            Texto formateado
        """
        try:
            # Navegar por la estructura de claves
            keys = key_path.split('.')
            value = self.texts
            
            for key in keys:
                value = value[key]
            
            # Formatear el texto si es string
            if isinstance(value, str):
                return value.format(**kwargs)
            return str(value)
            
        except (KeyError, TypeError):
            return f"[Texto no encontrado: {key_path}]"
    
    def get_list(self, key_path: str, **kwargs) -> list:
        """
        Obtiene una lista de textos
        
        Args:
            key_path: Ruta del texto (ej: "welcome.features")
            **kwargs: Variables para formatear los textos
            
        Returns:
            Lista de textos formateados
        """
        try:
            keys = key_path.split('.')
            value = self.texts
            
            for key in keys:
                value = value[key]
            
            if isinstance(value, list):
                return [item.format(**kwargs) if isinstance(item, str) else str(item) for item in value]
            return []
            
        except (KeyError, TypeError):
            return [f"[Lista no encontrada: {key_path}]"]

# Instancia global del gestor de textos
text_manager = TextManager()
