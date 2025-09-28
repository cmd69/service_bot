# 🔄 Flujo de la Aplicación Subscription Bot

## 📱 Flujo Principal

```
/start
├── [📋 Mi Suscripción] [💳 Suscribirse]
│   ├── [🔍 Consultar] [🔑 Credenciales]
│   ├── [👥 Acceso al Grupo]
│   └── [⬅️ Volver al Menú Principal]
├── [❓ Ayuda] [📊 Consultar Planes]
│   └── [⬅️ Volver al Menú Principal]
```

**Nota:** Los botones entre corchetes `[]` están en la misma fila

## 🏗️ Estructura de Handlers

### 1. **start.py** - Handler Principal
- `cmd_start()` - Comando `/start` con menú principal
- `cmd_back_to_main()` - Volver al menú principal

### 2. **subscription.py** - Gestión de Suscripciones
- `cmd_my_subscription()` - Menú de suscripción
- `cmd_check_subscription()` - Consultar estado
- `cmd_view_credentials()` - Ver credenciales
- `cmd_group_access()` - Acceso al grupo VIP

### 3. **subscribe.py** - Proceso de Suscripción
- `cmd_subscribe()` - Iniciar suscripción

### 4. **help.py** - Ayuda y Soporte
- `cmd_help()` - Ayuda detallada

### 5. **plans.py** - Consulta de Planes
- `cmd_view_plans()` - Información de planes

## 🎹 Estructura de Keyboards

### **main.py** - Teclados Principales
- `get_main_menu_keyboard()` - Menú principal con 4 opciones
- `get_subscription_menu_keyboard()` - Submenú de suscripción
- `get_back_to_main_keyboard()` - Botón volver

## 🔄 Flujo de Navegación

1. **Usuario envía `/start`**
   - Se muestra mensaje de bienvenida
   - Se presenta teclado principal con 4 opciones

2. **Usuario selecciona "Mi Suscripción"**
   - Se muestra submenú con 3 opciones
   - Cada opción muestra información mock
   - Botón "Volver" en cada pantalla

3. **Usuario selecciona "Suscribirse"**
   - Se muestra información del proceso (mock)
   - Botón "Volver" al menú principal

4. **Usuario selecciona "Ayuda"**
   - Se muestra ayuda detallada
   - Botón "Volver" al menú principal

5. **Usuario selecciona "Consultar Planes"**
   - Se muestra información de planes
   - Botón "Volver" al menú principal

## 📋 Estado Actual

✅ **Completado:**
- Estructura de handlers implementada
- Teclados inline funcionales
- Flujo de navegación completo
- Integración en main.py
- Sistema de textos personalizables
- Integración con Redis para FSM
- Configuración flexible con Docker Compose
- Documentación completa

⏳ **Próximos Pasos:**
- Implementar lógica real de suscripciones
- Integrar verificación de transacciones
- Conectar con base de datos
- Implementar sistema VIP real
- Sistema de pagos automático

## 🎯 Callback Data

| Callback | Handler | Función |
|----------|---------|---------|
| `my_subscription` | subscription.py | Mostrar menú suscripción |
| `check_subscription` | subscription.py | Consultar estado |
| `view_credentials` | subscription.py | Ver credenciales |
| `group_access` | subscription.py | Acceso al grupo |
| `subscribe` | subscribe.py | Iniciar suscripción |
| `help` | help.py | Mostrar ayuda |
| `view_plans` | plans.py | Ver planes |
| `back_to_main` | start.py | Volver al menú |
