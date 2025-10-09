"""
Punto de entrada principal del bot para MVP
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config.settings import settings
from app.handlers.start import router as start_router
from app.handlers.subscription import router as subscription_router
from app.handlers.subscribe import router as subscribe_router
from app.handlers.help import router as help_router
from app.handlers.plans import router as plans_router
from app.database.init_db import initialize_database

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Función principal del bot"""
    
    # Crear bot y dispatcher
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Registrar routers
    dp.include_router(start_router)
    dp.include_router(subscription_router)
    dp.include_router(subscribe_router)
    dp.include_router(help_router)
    dp.include_router(plans_router)
    
    try:
        logger.info("🚀 Iniciando JellyBot MVP...")
        
        # Inicializar base de datos
        logger.info("🗄️ Inicializando base de datos...")
        initialize_database()
        logger.info("✅ Base de datos inicializada correctamente")
        
        # Obtener información del bot
        bot_info = await bot.get_me()
        logger.info(f"🤖 Bot configurado: @{bot_info.username}")
        logger.info(f"👤 Admin: {settings.ADMIN_USER_ID}")
        
        # Iniciar polling
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Error al iniciar el bot: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot detenido por el usuario")
    except Exception as e:
        logger.error(f"❌ Error fatal: {e}")