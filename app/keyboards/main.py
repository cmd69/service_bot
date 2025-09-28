"""
Teclados inline principales del bot
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config.texts import text_manager

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Teclado principal después de /start"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.my_subscription"),
                    callback_data="my_subscription"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.subscribe"),
                    callback_data="subscribe"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.help"),
                    callback_data="help"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.view_plans"),
                    callback_data="view_plans"
                )
            ]
        ]
    )
    
    return keyboard

def get_subscription_menu_keyboard() -> InlineKeyboardMarkup:
    """Teclado del menú de suscripción"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.check_subscription"),
                    callback_data="check_subscription"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.view_credentials"),
                    callback_data="view_credentials"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.group_access"),
                    callback_data="group_access"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.back_to_main"),
                    callback_data="back_to_main"
                )
            ]
        ]
    )
    
    return keyboard

def get_back_to_main_keyboard() -> InlineKeyboardMarkup:
    """Teclado para volver al menú principal"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.back_to_main"),
                    callback_data="back_to_main"
                )
            ]
        ]
    )
    
    return keyboard

def get_help_keyboard() -> InlineKeyboardMarkup:
    """Teclado para opciones de ayuda"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.contact_support"),
                    callback_data="contact_support"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.tutorial"),
                    callback_data="tutorial"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.faq"),
                    callback_data="faq"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.back_to_main"),
                    callback_data="back_to_main"
                )
            ]
        ]
    )
    
    return keyboard

def get_plans_keyboard() -> InlineKeyboardMarkup:
    """Teclado para opciones de planes"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.plan_basic"),
                    callback_data="plan_basic"
                ),
                InlineKeyboardButton(
                    text=text_manager.get("buttons.plan_premium"),
                    callback_data="plan_premium"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.plan_vip"),
                    callback_data="plan_vip"
                )
            ],
            [
                InlineKeyboardButton(
                    text=text_manager.get("buttons.back_to_main"),
                    callback_data="back_to_main"
                )
            ]
        ]
    )
    
    return keyboard
