"""
Configuración básica del bot para MVP
"""
import os

class Settings:
    """Configuración del bot"""
    
    def __init__(self):
        # Bot Configuration
        self.BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
        
        # Admin ID
        admin_id_str = os.getenv("ADMIN_USER_ID", "")
        if admin_id_str:
            self.ADMIN_USER_ID: int = int(admin_id_str.strip())
        else:
            self.ADMIN_USER_ID: int = 0
        
        # Basic Configuration
        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
        
        # Validar configuración
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN no está configurado en las variables de entorno")
    
    def is_admin(self, user_id: int) -> bool:
        """Verifica si un usuario es administrador"""
        return user_id == self.ADMIN_USER_ID

# Instancia global de configuración
settings = Settings()