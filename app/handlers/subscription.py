"""
Handlers para gestión de suscripciones
"""
from aiogram import Router, types
# No need for Text filter, using lambda functions

from app.keyboards.main import get_subscription_menu_keyboard, get_back_to_main_keyboard
from app.config.texts import text_manager

# Router para handlers de suscripción
router = Router()

@router.callback_query(lambda c: c.data == "my_subscription")
async def cmd_my_subscription(callback: types.CallbackQuery):
    """Mostrar menú de suscripción"""
    
    title = text_manager.get("subscription.menu_title")
    description = text_manager.get("subscription.menu_description")
    options = text_manager.get_list("subscription.options")
    
    options_text = "\n".join(f"• {option}" for option in options)
    
    text = f"""
        {title}

        {description}

        **Opciones disponibles:**
        {options_text}

        Selecciona una opción:
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_subscription_menu_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "check_subscription")
async def cmd_check_subscription(callback: types.CallbackQuery):
    """Consultar estado de suscripción"""
    
    # TODO: Implementar consulta real a la base de datos
    title = text_manager.get("subscription.check_title")
    no_subscription = text_manager.get("subscription.no_subscription")
    
    text = f"""
        {title}

        **Estado:** {no_subscription}
        **Plan:** Ninguno
        **Fecha de expiración:** -
        **Días restantes:** -

        **Para suscribirte:**
        1. Selecciona "Suscribirse" en el menú principal
        2. Elige un plan
        3. Realiza el pago
        4. Verifica tu transacción

        *Esta funcionalidad estará disponible próximamente.*
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_main_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "view_credentials")
async def cmd_view_credentials(callback: types.CallbackQuery):
    """Mostrar credenciales de acceso"""
    
    # TODO: Implementar generación de credenciales
    title = text_manager.get("subscription.credentials_title")
    
    text = f"""
        {title}

        **Usuario:** `usuario_ejemplo`
        **Contraseña:** `password_ejemplo`
        **Servidor:** `servidor.ejemplo.com`
        **Puerto:** `8080`

        **⚠️ Importante:**
        • Estas credenciales son temporales
        • Cámbialas después del primer acceso
        • No las compartas con nadie

        *Esta funcionalidad estará disponible próximamente.*
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_main_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "group_access")
async def cmd_group_access(callback: types.CallbackQuery):
    """Proporcionar acceso al grupo VIP"""
    
    # TODO: Implementar verificación de suscripción y enlace al grupo
    # TODO: necesitamos un metodo donde se deniegue el acceso, y que se llame desde el resto de handlers si se deniega el acceso.
    title = text_manager.get("subscription.group_access_title")
    
    text = f"""
        {title}

        **Estado:** ❌ Sin acceso
        **Motivo:** No tienes una suscripción activa

        **Para obtener acceso:**
        1. Suscríbete a uno de nuestros planes
        2. Verifica tu pago
        3. El enlace al grupo se generará automáticamente

        **Grupo Premium incluye:**
        • Servicios exclusivos
        • Análisis técnico avanzado
        • Soporte prioritario
        • Comunidad de usuarios

        *Esta funcionalidad estará disponible próximamente.*
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_main_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

