#!/usr/bin/env python3
"""
Script de prueba para verificar que el bot funciona correctamente
"""
import os
import sys
import asyncio
from pathlib import Path

# Cargar variables de entorno desde .env
def load_env_file():
    """Cargar variables de entorno desde archivo .env"""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

# Cargar .env antes de importar la app
load_env_file()

# Agregar el directorio app al path
sys.path.insert(0, str(Path(__file__).parent / "app"))

async def test_bot():
    """Prueba básica del bot"""
    try:
        # Importar configuración
        from app.config.settings import settings
        print("✅ Configuración cargada correctamente")
        print(f"   Bot Token: {'*' * 20}...{settings.BOT_TOKEN[-10:]}")
        print(f"   Admin ID: {settings.ADMIN_USER_ID}")
        print(f"   Debug: {settings.DEBUG}")
        
        # Importar handlers
        from app.handlers.start import router
        print("✅ Handlers importados correctamente")
        
        # Importar main
        from app.main import main
        print("✅ Módulo principal importado correctamente")
        
        print("\n🎉 ¡Todas las importaciones funcionan correctamente!")
        print("🚀 El bot está listo para ejecutarse")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en la prueba: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Iniciando prueba del bot...")
    success = asyncio.run(test_bot())
    
    if success:
        print("\n✅ Prueba completada exitosamente")
        print("💡 Para ejecutar el bot: docker-compose up --build")
    else:
        print("\n❌ La prueba falló")
        sys.exit(1)
