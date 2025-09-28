# 🚀 Subscription Bot MVP - Inicio Rápido

## ✅ Estado Actual
**Etapa 1 completada:** Bot funcional con sistema completo de gestión de suscripciones

## 🏗️ Estructura del Proyecto
```
subscribe_bot/
├── app/
│   ├── main.py              # Punto de entrada
│   ├── config/              # Configuración y textos
│   │   ├── settings.py      # Configuración principal
│   │   ├── texts.py         # Sistema de textos
│   │   └── texts_config.py  # Configuración de textos
│   ├── handlers/            # Handlers de comandos
│   │   ├── start.py         # Comando /start
│   │   ├── subscription.py  # Gestión de suscripciones
│   │   ├── subscribe.py     # Proceso de suscripción
│   │   ├── help.py          # Ayuda
│   │   └── plans.py         # Consulta de planes
│   └── keyboards/           # Teclados interactivos
│       └── main.py          # Teclados principales
├── texts/                   # Sistema de textos
│   ├── custom_texts.json    # Textos personalizados
│   ├── generic_texts.json   # Textos genéricos
│   └── custom_texts.example.json
├── docs/                    # Documentación
├── docker-compose.yml       # Docker Compose con Redis
├── Dockerfile              # Imagen Docker
├── requirements.txt        # Dependencias
├── env.example            # Variables de entorno
└── test_bot.py            # Script de prueba
```

## 🚀 Cómo Ejecutar

### 1. Configurar Variables de Entorno
```bash
cp env.example .env
```

Editar `.env`:
```env
BOT_TOKEN=tu_token_de_telegram_aqui
ADMIN_USER_IDS=123456789,987654321
DEBUG=False

# Configuración de textos (opcional)
CUSTOM_TEXTS_PATH=/app/texts/custom_texts.json
GENERIC_TEXTS_PATH=/app/texts/generic_texts.json
TEXTS_FALLBACK_TO_GENERIC=true
TEXTS_AUTO_RELOAD=false
TEXTS_VERBOSE_LOGGING=true
```

### 2. Probar Configuración
```bash
python test_bot.py
```

### 3. Ejecutar con Docker
```bash
docker-compose up --build
```

### 4. Probar en Telegram
1. Busca tu bot
2. Envía `/start`
3. Deberías ver el mensaje de bienvenida

## 📋 Funcionalidades Actuales
- ✅ Comando `/start` con mensaje de bienvenida
- ✅ Sistema completo de gestión de suscripciones
- ✅ Teclados interactivos con navegación
- ✅ Sistema de textos personalizables
- ✅ Integración con Redis para FSM
- ✅ Configuración flexible mediante Docker Compose
- ✅ Docker y Docker Compose con Redis
- ✅ Logging estructurado
- ✅ Documentación completa

## 🔄 Próximos Pasos
Ver documentación en `docs/` para detalles completos.

**Siguiente etapa:** Implementación de verificación de transacciones y base de datos
