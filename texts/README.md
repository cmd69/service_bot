# Sistema de Textos del Bot

Este directorio contiene la configuración de textos para el bot de Telegram.

## Estructura

- `custom_texts.json` - Textos personalizados (NO se sube a GitHub)
- `custom_texts.example.json` - Archivo de ejemplo con la estructura de textos
- `.gitignore` - Excluye los textos personalizados del control de versiones

## Cómo usar

### 1. Textos por defecto
El bot usa textos genéricos por defecto que se muestran en GitHub como ejemplo.

### 2. Textos personalizados
Para personalizar los textos:

1. Copia `custom_texts.example.json` a `custom_texts.json`:
   ```bash
   cp custom_texts.example.json custom_texts.json
   ```

2. Edita `custom_texts.json` con tus textos personalizados

3. El bot cargará automáticamente los textos personalizados

### 3. Estructura de textos

Los textos están organizados en secciones:

- `bot` - Información del bot (nombre, descripción, versión)
- `welcome` - Mensajes de bienvenida
- `subscription` - Textos relacionados con suscripciones
- `plans` - Información de planes de suscripción
- `help` - Textos de ayuda y soporte
- `subscribe` - Proceso de suscripción
- `buttons` - Textos de botones

### 4. Variables dinámicas

Puedes usar variables en los textos usando la sintaxis `{variable}`:

```json
{
  "welcome": {
    "title": "🤖 ¡Hola! Soy {bot_name}",
    "description": "Bienvenido a {bot_name}"
  }
}
```

### 5. Listas de textos

Para listas de elementos, usa arrays:

```json
{
  "welcome": {
    "features": [
      "Característica 1",
      "Característica 2",
      "Característica 3"
    ]
  }
}
```

## Ventajas

- ✅ Textos separados del código
- ✅ Fácil personalización sin tocar código
- ✅ Textos genéricos como fallback
- ✅ No se suben textos personalizados a GitHub
- ✅ Soporte para variables dinámicas
- ✅ Estructura organizada y mantenible

## Notas

- Los textos personalizados tienen prioridad sobre los genéricos
- Si hay un error cargando textos personalizados, se usan los genéricos
- Los cambios en `custom_texts.json` se aplican al reiniciar el bot
- Mantén la estructura JSON válida para evitar errores
