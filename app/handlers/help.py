"""
Handlers para ayuda y soporte
"""
from aiogram import Router, types
# No need for Text filter, using lambda functions

from app.keyboards.main import get_help_keyboard
from app.config.texts import text_manager

# Router para handlers de ayuda
router = Router()

@router.callback_query(lambda c: c.data == "help")
async def cmd_help(callback: types.CallbackQuery):
    """Mostrar ayuda detallada"""
    
    bot_name = text_manager.get("bot.name")
    title = text_manager.get("help.title", bot_name=bot_name)
    description = text_manager.get("help.description", bot_name=bot_name)
    commands = text_manager.get_list("help.commands")
    process = text_manager.get_list("help.process")
    networks = text_manager.get_list("help.networks")
    
    # Obtener información de planes
    basic_plan = text_manager.get("plans.basic.name")
    premium_plan = text_manager.get("plans.premium.name")
    vip_plan = text_manager.get("plans.vip.name")
    
    commands_text = "\n".join(f"• {cmd}" for cmd in commands)
    process_text = "\n".join(f"{i+1}. {step}" for i, step in enumerate(process))
    networks_text = "\n".join(f"• **{network}**" for network in networks)
    
    text = f"""
        {title}

        **🤖 ¿Qué es {bot_name}?**
        {description}

        **📋 Comandos Principales:**
        {commands_text}

        **💳 Proceso de Suscripción:**
        {process_text}

        **🔐 Redes Soportadas:**
        {networks_text}

        **📊 Planes Disponibles:**
        • **{basic_plan}** - Acceso básico a servicios
        • **{premium_plan}** - Servicios + análisis técnico
        • **{vip_plan}** - Todo incluido + soporte prioritario

        **🆘 ¿Necesitas más ayuda?**
        Contacta con el administrador del bot.

        **📱 Estado del Bot:** MVP - En desarrollo activo
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_help_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

# TODO Prompts user for a message and sends it to the admin's telgram using its chat_id
@router.callback_query(lambda c: c.data == "contact_support")
async def cmd_contact_support(callback: types.CallbackQuery):
    """Contactar soporte"""
    
    title = text_manager.get("help.contact_title")
    description = text_manager.get("help.contact_description")
    
    text = f"""
        {title}

        {description}
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_help_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "tutorial")
async def cmd_tutorial(callback: types.CallbackQuery):
    """Mostrar tutorial"""
    
    bot_name = text_manager.get("bot.name")
    title = text_manager.get("help.tutorial_title", bot_name=bot_name)
    steps = text_manager.get_list("help.tutorial_steps")
    
    steps_text = "\n".join(steps)
    
    text = f"""
        {title}

        {steps_text}
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_help_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "faq")
async def cmd_faq(callback: types.CallbackQuery):
    """Mostrar FAQ"""
    
    title = text_manager.get("help.faq_title")
    faq_items = text_manager.texts["help"]["faq_items"]
    
    newline = "\n"
    faq_text = "\n".join(f"**{item['question']}**{newline}{item['answer']}" for item in faq_items)
    
    text = f"""
        {title}

        {faq_text}
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_help_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()
