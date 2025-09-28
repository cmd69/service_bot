#!/usr/bin/env python3
"""
Script para probar las importaciones de aiogram
"""
import os
import sys
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

def test_imports():
    """Probar importaciones de aiogram"""
    try:
        print("🧪 Probando importaciones de aiogram...")
        
        # Probar importaciones básicas
        from aiogram import Router, types
        print("✅ aiogram.Router y types importados correctamente")
        
        from aiogram.filters import Command, Text
        print("✅ aiogram.filters.Command y Text importados correctamente")
        
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        print("✅ aiogram.types.InlineKeyboard importados correctamente")
        
        # Probar importación de la app
        from app.config.settings import settings
        print("✅ Configuración de la app importada correctamente")
        
        from app.keyboards.main import get_main_menu_keyboard
        print("✅ Keyboards importados correctamente")
        
        from app.handlers.start import router as start_router
        print("✅ Handler start importado correctamente")
        
        from app.handlers.subscription import router as subscription_router
        print("✅ Handler subscription importado correctamente")
        
        from app.handlers.subscribe import router as subscribe_router
        print("✅ Handler subscribe importado correctamente")
        
        from app.handlers.help import router as help_router
        print("✅ Handler help importado correctamente")
        
        from app.handlers.plans import router as plans_router
        print("✅ Handler plans importado correctamente")
        
        print("\n🎉 ¡Todas las importaciones funcionan correctamente!")
        print("🚀 El bot está listo para ejecutarse")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en las importaciones: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Iniciando prueba de importaciones...")
    success = test_imports()
    
    if success:
        print("\n✅ Prueba completada exitosamente")
        print("💡 Para ejecutar el bot: docker compose up --build")
    else:
        print("\n❌ La prueba falló")
        sys.exit(1)
