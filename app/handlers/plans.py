"""
Handlers para consulta de planes
"""
from aiogram import Router, types
# No need for Text filter, using lambda functions

from app.keyboards.main import get_plans_keyboard
from app.config.texts import text_manager

# Router para handlers de planes
router = Router()

@router.callback_query(lambda c: c.data == "view_plans")
async def cmd_view_plans(callback: types.CallbackQuery):
    """Mostrar información de planes disponibles"""
    
    title = text_manager.get("plans.title")
    basic = text_manager.texts["plans"]["basic"]
    premium = text_manager.texts["plans"]["premium"]
    vip = text_manager.texts["plans"]["vip"]
    payment_methods = text_manager.get_list("plans.payment_methods")
    renewal_info = text_manager.get("plans.renewal_info")
    
    basic_features = "\n".join(f"• {feature}" for feature in basic['features'])
    premium_features = "\n".join(f"• {feature}" for feature in premium['features'])
    vip_features = "\n".join(f"• {feature}" for feature in vip['features'])
    payment_methods_text = "\n".join(f"• {method}" for method in payment_methods)
    
    text = f"""
        {title}

        **🔰 {basic['name']} - {basic['price']}**
        {basic_features}

        **⭐ {premium['name']} - {premium['price']}**
        {premium_features}

        **👑 {vip['name']} - {vip['price']}**
        {vip_features}

        **💳 Métodos de Pago:**
        {payment_methods_text}

        {renewal_info}

        **❓ ¿Tienes preguntas?**
        Usa el botón "Ayuda" para más información.
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_plans_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "plan_basic")
async def cmd_plan_basic(callback: types.CallbackQuery):
    """Detalles del plan básico"""
    
    basic = text_manager.texts["plans"]["basic"]
    
    basic_features = "\n".join(f"• {feature}" for feature in basic['features'])
    
    text = f"""
        🔰 **{basic['name']} - {basic['price']}**

        **Incluye:**
        {basic_features}

        **Perfecto para:**
        • Usuarios principiantes
        • Presupuesto limitado
        • Aprendizaje gradual

        **{basic['status']}**
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_plans_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "plan_premium")
async def cmd_plan_premium(callback: types.CallbackQuery):
    """Detalles del plan premium"""
    
    premium = text_manager.texts["plans"]["premium"]
    
    premium_features = "\n".join(f"• {feature}" for feature in premium['features'])
    
    text = f"""
        ⭐ **{premium['name']} - {premium['price']}**

        **Incluye:**
        {premium_features}

        **Perfecto para:**
        • Usuarios intermedios
        • Mayor frecuencia de uso
        • Análisis más profundo

        **{premium['status']}**
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_plans_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "plan_vip")
async def cmd_plan_vip(callback: types.CallbackQuery):
    """Detalles del plan VIP"""
    
    vip = text_manager.texts["plans"]["vip"]
    
    vip_features = "\n".join(f"• {feature}" for feature in vip['features'])
    
    text = f"""
        👑 **{vip['name']} - {vip['price']}**

        **Incluye:**
        {vip_features}

        **Perfecto para:**
        • Usuarios profesionales
        • Máxima frecuencia
        • Servicio premium completo

        **{vip['status']}**
    """
    
    await callback.message.edit_text(
        text,
        reply_markup=get_plans_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

