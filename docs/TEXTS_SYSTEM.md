# Sistema de Textos del Bot - Subscription Bot

## Resumen

Se ha implementado un sistema completo de gestión de textos que separa los contenidos del código, permitiendo:

- ✅ **Textos personalizados** en archivos JSON separados
- ✅ **Textos genéricos** como fallback para GitHub
- ✅ **No se suben textos personalizados** a GitHub
- ✅ **Fácil personalización** sin tocar código
- ✅ **Variables dinámicas** en los textos
- ✅ **Estructura organizada** y mantenible

## Archivos Creados/Modificados

### Nuevos Archivos
- `app/config/texts.py` - Sistema de gestión de textos
- `app/config/texts_config.py` - Configuración del sistema
- `texts/custom_texts.json` - Textos personalizados (NO se sube a GitHub)
- `texts/custom_texts.example.json` - Archivo de ejemplo
- `texts/.gitignore` - Excluye textos personalizados
- `texts/README.md` - Documentación del sistema
- `TEXTS_SYSTEM.md` - Este archivo

### Archivos Modificados
- `app/handlers/start.py` - Usa sistema de textos
- `app/handlers/help.py` - Usa sistema de textos
- `app/handlers/plans.py` - Usa sistema de textos
- `app/handlers/subscription.py` - Usa sistema de textos
- `app/handlers/subscribe.py` - Usa sistema de textos
- `app/keyboards/main.py` - Usa sistema de textos
- `.gitignore` - Excluye textos personalizados

## Cambios en los Textos

### Antes (Hardcoded)
```python
text = """
🤖 **¡Hola! Soy Subscription Bot** 

Bienvenido al bot de gestión de suscripciones y servicios premium.

**¿Qué puedo hacer por ti?**
• Gestionar suscripciones premium
• Acceso a servicios VIP
• Verificación de pagos
• Soporte técnico especializado
"""
```

### Después (Sistema de Textos)
```python
bot_name = text_manager.get("bot.name")
title = text_manager.get("welcome.title", bot_name=bot_name)
description = text_manager.get("welcome.description")
features = text_manager.get_list("welcome.features")

text = f"""
{title}

{description}

**¿Qué puedo hacer por ti?**
{chr(10).join(f"• {feature}" for feature in features)}
"""
```

## Nuevos Textos (Enfoque en Servicios)

Los textos han sido actualizados para reflejar que el bot es principalmente un **bot de gestión de suscripciones y servicios premium**:

### Características Principales
- **Gestión de suscripciones** como función principal
- **Servicios premium** con diferentes niveles de acceso
- **Múltiples métodos de pago** (BSC, TRON)
- **Verificación automática** de transacciones
- **Soporte técnico especializado**
- **Acceso a grupos VIP** tras verificación

### Planes Actualizados
- **Plan Básico**: Acceso básico a servicios premium
- **Plan Premium**: Acceso completo + análisis avanzado
- **Plan VIP**: Acceso VIP completo + soporte 24/7

## Cómo Usar

### 1. Textos por Defecto
El bot usa textos genéricos por defecto que se muestran en GitHub.

### 2. Personalizar Textos
1. Copia el archivo de ejemplo:
   ```bash
   cp texts/custom_texts.example.json texts/custom_texts.json
   ```

2. Edita `texts/custom_texts.json` con tus textos

3. Reinicia el bot para aplicar cambios

### 3. Estructura de Textos
```json
{
  "bot": {
    "name": "TuBot",
    "description": "Descripción del bot"
  },
  "welcome": {
    "title": "🤖 ¡Hola! Soy {bot_name}",
    "features": ["Característica 1", "Característica 2"]
  },
  "plans": {
    "basic": {
      "name": "Plan Básico",
      "price": "$10/mes",
      "features": ["Feature 1", "Feature 2"]
    }
  }
}
```

## Ventajas del Sistema

1. **Separación de responsabilidades**: Código vs contenido
2. **Fácil mantenimiento**: Cambiar textos sin tocar código
3. **Personalización simple**: Solo editar JSON
4. **Control de versiones**: Textos genéricos en GitHub
5. **Flexibilidad**: Variables dinámicas y listas
6. **Robustez**: Fallback automático a textos genéricos

## Próximos Pasos

1. **Personalizar textos** según necesidades específicas
2. **Agregar más idiomas** si es necesario
3. **Implementar recarga automática** en desarrollo
4. **Agregar validación** de estructura JSON
5. **Crear interfaz web** para editar textos (opcional)

## Notas Técnicas

- Los textos se cargan al iniciar el bot
- Cambios requieren reinicio del bot
- El sistema es robusto ante errores de JSON
- Soporte completo para Unicode/emojis
- Compatible con Markdown de Telegram
