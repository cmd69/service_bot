"""
Handlers para proceso de suscripción
"""
from aiogram import Router, types
# No need for Text filter, using lambda functions

from app.keyboards.main import get_back_to_main_keyboard
from app.config.texts import text_manager

# Router para handlers de suscripción
router = Router()

@router.callback_query(lambda c: c.data == "subscribe")
async def cmd_subscribe(callback: types.CallbackQuery):
    """Iniciar proceso de suscripción"""
    
    title = text_manager.get("subscribe.title")
    coming_soon = text_manager.get("subscribe.coming_soon")
    description = text_manager.get("subscribe.description")
    process = text_manager.get_list("subscribe.process")
    stay_tuned = text_manager.get("subscribe.stay_tuned")
    
    process_text = "\n".join(process)
    
    text = f"""
        {title}

        **{coming_soon}**

        {description}

        {process_text}

        **{stay_tuned}**
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_main_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()
