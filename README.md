# Subscription Bot - Bot de Telegram para Gestión de Suscripciones

Un bot de Telegram moderno y seguro para la gestión de suscripciones y servicios premium, con verificación automática de transacciones de criptomonedas.

## 🚀 Características Principales

- ✅ **Gestión de Suscripciones**: Sistema completo de suscripciones premium
- 🔐 **Verificación de Transacciones**: Soporte para BSC y TRON
- 🛡️ **Seguridad Robusta**: Validación de datos, rate limiting, Redis
- 📊 **Sistema de Textos**: Textos personalizables sin tocar código
- 🌐 **Arquitectura Moderna**: Async/await, Docker, configuración flexible
- 📱 **Interfaz Intuitiva**: Menús interactivos y navegación fluida

## 🏗️ Arquitectura

### Stack Tecnológico
- **Framework**: aiogram 3.x (async/await)
- **Cache**: Redis para FSM y rate limiting
- **Validación**: Pydantic para validación robusta
- **Contenedores**: Docker + Docker Compose
- **Configuración**: Variables de entorno flexibles

### Estructura del Proyecto
```
subscribe_bot/
├── app/
│   ├── config/          # Configuración y sistema de textos
│   ├── handlers/        # Handlers de comandos de Telegram
│   ├── keyboards/       # Teclados interactivos
│   └── main.py          # Punto de entrada
├── texts/               # Sistema de textos personalizables
├── docs/                # Documentación completa
├── docker-compose.yml   # Configuración con Redis
└── requirements.txt     # Dependencias
```

## 🚀 Inicio Rápido

### 1. Configurar Variables de Entorno
```bash
cp env.example .env
```

Editar `.env`:
```env
BOT_TOKEN=tu_token_de_telegram_aqui
ADMIN_USER_IDS=123456789,987654321
DEBUG=False
```

### 2. Ejecutar con Docker
```bash
# Construir y ejecutar todos los servicios
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d
```

### 3. Probar el Bot
1. Busca tu bot en Telegram
2. Envía `/start`
3. Explora las opciones del menú

## 📖 Documentación Completa

### 📚 Guías Principales
- **[🚀 Inicio Rápido](docs/QUICK_START.md)** - Configuración y ejecución rápida
- **[🔄 Flujo de la Aplicación](docs/FLOW_DIAGRAM.md)** - Diagramas y estructura de navegación
- **[⚙️ Sistema de Configuración](docs/CONFIGURATION_SYSTEM.md)** - Configuración flexible y Docker Compose
- **[📝 Sistema de Textos](docs/TEXTS_SYSTEM.md)** - Personalización de textos sin código

### 🎯 Funcionalidades Actuales

#### Comandos Disponibles
- `/start` - Iniciar el bot y mostrar menú principal
- Navegación completa por menús interactivos

#### Flujo de Usuario
1. **Menú Principal**: 4 opciones principales
   - 📋 Mi Suscripción
   - 💳 Suscribirse  
   - ❓ Ayuda
   - 📊 Consultar Planes

2. **Gestión de Suscripciones**: Submenú con opciones
   - 🔍 Consultar estado
   - 🔑 Ver credenciales
   - 👥 Acceso al grupo VIP

#### Características Técnicas
- ✅ Sistema de textos personalizables
- ✅ Integración con Redis para FSM
- ✅ Configuración flexible con Docker Compose
- ✅ Teclados interactivos con navegación
- ✅ Logging estructurado
- ✅ Documentación completa

## 🔧 Desarrollo

### Estructura de Código
- **Handlers**: Manejan comandos y callbacks de Telegram
- **Keyboards**: Teclados interactivos y navegación
- **Config**: Sistema de configuración y textos
- **Texts**: Archivos JSON para personalización

### Personalización de Textos
1. Copia el archivo de ejemplo:
   ```bash
   cp texts/custom_texts.example.json texts/custom_texts.json
   ```

2. Edita `texts/custom_texts.json` con tus textos

3. Reinicia el bot para aplicar cambios

### Testing
```bash
# Probar configuración
python test_bot.py

# Verificar imports
python test_imports.py
```

## 🛡️ Seguridad

### Características Implementadas
- ✅ **Configuración Segura**: Variables de entorno para secrets
- ✅ **Rate Limiting**: Con Redis para prevenir spam
- ✅ **Validación de Datos**: Con Pydantic
- ✅ **Logging Estructurado**: Para auditoría y debugging
- ✅ **Textos Separados**: Sin hardcodeo en el código

## 📊 Estado del Proyecto

### ✅ Completado (Etapa 1 - MVP)
- Bot funcional con comando `/start`
- Sistema completo de gestión de suscripciones
- Teclados interactivos con navegación
- Sistema de textos personalizables
- Integración con Redis
- Configuración flexible con Docker Compose
- Documentación completa

### ⏳ Próximos Pasos
- Implementar verificación real de transacciones
- Integrar base de datos PostgreSQL
- Sistema de pagos automático
- Panel de administración
- Testing completo

## 🚀 Despliegue

### Producción
1. Configurar variables de entorno de producción
2. Configurar webhook de Telegram (opcional)
3. Desplegar con Docker Compose
4. Monitorear logs

### Escalabilidad
- Redis para cache distribuido
- Arquitectura async para mejor rendimiento
- Contenedores Docker para fácil escalado
- Configuración flexible para diferentes entornos

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama para feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 📞 Soporte

Para soporte y preguntas:
- Crear un issue en GitHub
- Revisar la documentación en `docs/`
- Contactar al administrador del bot

---

**Subscription Bot** - Gestión moderna de suscripciones en Telegram 🚀