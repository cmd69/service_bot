# Sistema de Configuración - Subscription Bot

## 🎯 **¿Qué es este sistema?**

Este bot utiliza un sistema de configuración flexible que permite personalizar el comportamiento sin modificar el código. Todo se configura mediante variables de entorno y archivos de texto.

## 🚀 **Configuración Inicial para Nuevos Usuarios**

### **Paso 1: Configurar Variables Básicas**

Crea el archivo `.env` copiando el ejemplo:
```bash
cp env.example .env
```

Edita el archivo `.env` con tus datos:
```env
# Configuración del Bot (OBLIGATORIO)
BOT_TOKEN=tu_token_de_telegram_aqui
ADMIN_USER_IDS=123456789,987654321

# Configuración de Desarrollo (OPCIONAL)
DEBUG=False
```

### **Paso 2: Personalizar Textos del Bot**

1. **Copia el archivo de ejemplo:**
   ```bash
   cp texts/custom_texts.example.json texts/custom_texts.json
   ```

2. **Edita los textos:**
   - Abre `texts/custom_texts.json`
   - Modifica los textos según tus necesidades
   - Guarda el archivo

3. **Reinicia el bot** para aplicar los cambios

### **Paso 3: Ejecutar el Bot**

```bash
# Con Docker (recomendado)
docker-compose up --build

# O en segundo plano
docker-compose up -d
```

## ⚙️ **Configuraciones Disponibles**

### **Variables de Entorno Principales**

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `BOT_TOKEN` | Token de tu bot de Telegram | `123456789:ABC...` |
| `ADMIN_USER_IDS` | IDs de usuarios administradores | `123456789,987654321` |
| `DEBUG` | Modo debug (true/false) | `False` |

### **Configuración de Textos**

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `CUSTOM_TEXTS_PATH` | Ruta a textos personalizados | `/app/texts/custom_texts.json` |
| `GENERIC_TEXTS_PATH` | Ruta a textos genéricos | `/app/texts/generic_texts.json` |
| `TEXTS_FALLBACK_TO_GENERIC` | Usar textos genéricos si fallan los personalizados | `true` |
| `TEXTS_AUTO_RELOAD` | Recargar textos automáticamente | `false` |
| `TEXTS_VERBOSE_LOGGING` | Mostrar logs detallados | `true` |

## 🔧 **Configuraciones Avanzadas**

### **Para Desarrollo Local**

Si quieres modificar textos durante el desarrollo:
```env
# .env
TEXTS_AUTO_RELOAD=true
TEXTS_VERBOSE_LOGGING=true
```

### **Para Producción**

Configuración optimizada para producción:
```env
# .env
DEBUG=False
TEXTS_AUTO_RELOAD=false
TEXTS_VERBOSE_LOGGING=false
```

### **Rutas Personalizadas**

Si quieres usar textos en otra ubicación:
```env
# .env
CUSTOM_TEXTS_PATH=/ruta/personalizada/mis_textos.json
GENERIC_TEXTS_PATH=/ruta/personalizada/textos_genericos.json
```

## 📁 **Estructura de Archivos**

```
subscribe_bot/
├── .env                          # Variables de entorno (crear tú)
├── env.example                   # Ejemplo de variables
├── docker-compose.yml            # Configuración de Docker
├── texts/
│   ├── custom_texts.json         # Tus textos personalizados
│   ├── custom_texts.example.json # Ejemplo de textos
│   └── generic_texts.json        # Textos por defecto
└── docs/                         # Documentación
```

## 🛠️ **Casos de Uso Comunes**

### **1. Bot Básico (Recién Instalado)**
```env
# .env - Solo lo mínimo necesario
BOT_TOKEN=tu_token_aqui
ADMIN_USER_IDS=tu_id_aqui
```

### **2. Bot con Textos Personalizados**
```env
# .env
BOT_TOKEN=tu_token_aqui
ADMIN_USER_IDS=tu_id_aqui
TEXTS_VERBOSE_LOGGING=true
```

### **3. Bot en Desarrollo**
```env
# .env
BOT_TOKEN=tu_token_aqui
ADMIN_USER_IDS=tu_id_aqui
DEBUG=True
TEXTS_AUTO_RELOAD=true
TEXTS_VERBOSE_LOGGING=true
```

## 🔍 **Cómo Funciona Internamente**

### **Prioridad de Configuración:**
1. Variables de entorno del sistema
2. Archivo `.env`
3. Valores por defecto en el código

### **Ejemplo:**
```bash
# Si defines en .env:
CUSTOM_TEXTS_PATH=/mi/ruta/personalizada.json

# El bot usará esa ruta en lugar de la por defecto
```

## ❓ **Preguntas Frecuentes**

### **¿Necesito crear el archivo .env?**
Sí, es obligatorio para el `BOT_TOKEN` y `ADMIN_USER_IDS`.

### **¿Puedo cambiar los textos sin reiniciar?**
Solo si activas `TEXTS_AUTO_RELOAD=true` (recomendado solo para desarrollo).

### **¿Qué pasa si no creo custom_texts.json?**
El bot usará los textos genéricos automáticamente.

### **¿Puedo usar rutas absolutas?**
Sí, puedes especificar cualquier ruta en las variables de entorno.

## 🚨 **Solución de Problemas**

### **El bot no inicia**
- Verifica que `BOT_TOKEN` sea correcto
- Asegúrate de que `ADMIN_USER_IDS` contenga tu ID de Telegram

### **Los textos no se cargan**
- Verifica que `custom_texts.json` tenga formato JSON válido
- Revisa los logs con `TEXTS_VERBOSE_LOGGING=true`

### **Cambios no se aplican**
- Reinicia el bot: `docker-compose restart`
- O usa `TEXTS_AUTO_RELOAD=true` para desarrollo

## 📖 **Próximos Pasos**

1. **Configura básica**: Crea `.env` con tu token
2. **Personaliza textos**: Edita `custom_texts.json`
3. **Ejecuta el bot**: `docker-compose up --build`
4. **Prueba**: Envía `/start` a tu bot en Telegram

Para más detalles sobre personalización de textos, consulta [Sistema de Textos](TEXTS_SYSTEM.md).