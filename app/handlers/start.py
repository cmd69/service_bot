"""
Handler para el comando /start
"""
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from app.keyboards.main import get_main_menu_keyboard
from app.config.texts import text_manager

# Router para los handlers
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Comando /start - Mensaje de bienvenida"""
    
    bot_name = text_manager.get("bot.name")
    title = text_manager.get("welcome.title", bot_name=bot_name)
    description = text_manager.get("welcome.description")
    features = text_manager.get_list("welcome.features")
    instructions = text_manager.get("welcome.instructions")
    
    features_text = "\n".join(f"• {feature}" for feature in features)
    
    welcome_text = f"""
        {title}

        {description}

        **¿Qué puedo hacer por ti?**

        {features_text}

        **{instructions}**
    """
    
    await message.answer(
        welcome_text,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="Markdown"
    )

@router.callback_query(lambda c: c.data == "back_to_main")
async def cmd_back_to_main(callback: types.CallbackQuery):
    """Volver al menú principal"""
    
    bot_name = text_manager.get("bot.name")
    title = text_manager.get("welcome.title", bot_name=bot_name)
    description = text_manager.get("welcome.description")
    features = text_manager.get_list("welcome.features")
    instructions = text_manager.get("welcome.instructions")
    
    features_text = "\n".join(f"• {feature}" for feature in features)
    
    welcome_text = f"""
        {title}

        {description}

        **¿Qué puedo hacer por ti?**
        {features_text}

        **{instructions}**
    """
    
    await callback.message.edit_text(
        welcome_text,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()