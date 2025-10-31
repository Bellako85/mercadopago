# Mercado Pago Payment Gateway para Odoo 17

<div align="center">
  <img src="https://http2.mlstatic.com/storage/logos-api-admin/51b446b0-571c-11e8-9a2d-4b2bd7b1bf77-m.svg" alt="Mercado Pago" width="200"/>
  
  **Integración completa con Mercado Pago para Odoo 17**
  
  [![Odoo](https://img.shields.io/badge/Odoo-17.0-purple)](https://www.odoo.com)
  [![License: LGPL-3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
  [![Python](https://img.shields.io/badge/Python-3.10+-green)](https://www.python.org/)
</div>

---

## 📋 Descripción

Módulo completo e independiente de Odoo 17 que proporciona integración total con **Mercado Pago**, el procesador de pagos líder en América Latina. Permite a tu negocio aceptar pagos en línea de manera segura y eficiente.

## ✨ Características Principales

### 💳 Métodos de Pago
- **Tarjetas de crédito y débito** (Visa, Mastercard, American Express, etc.)
- **Efectivo** (OXXO, 7-Eleven, Farmacias, etc.)
- **Transferencias bancarias**
- **Mercado Pago Wallet**

### 🚀 Funcionalidades
- ✅ **Checkout Pro** - Redirección a Mercado Pago con interfaz responsive
- ✅ **Webhooks** - Notificaciones automáticas de estado de pagos
- ✅ **Reembolsos** - Procesamiento automático de devoluciones
- ✅ **Multi-moneda** - Soporte para diferentes monedas
- ✅ **Multi-compañía** - Configuraciones por compañía
- ✅ **Modo Test/Producción** - Fácil cambio entre ambientes
- ✅ **API JSON-RPC** - Integración con sistemas externos
- ✅ **Cuotas** - Configuración de pagos en cuotas
- ✅ **Tracking completo** - Historial de cambios y actividades

### 🔐 Seguridad
- Credenciales encriptadas
- HTTPS obligatorio en producción
- Sin almacenamiento de datos de tarjetas
- Validación de webhooks

## 📦 Instalación

### Requisitos Previos

```bash
# Python 3.10 o superior
python3 --version

# Librería requests
pip3 install requests
```

### Instalación del Módulo

#### Opción 1: Instalación Automática

```bash
cd /path/to/odoo/addons
git clone [URL_DEL_REPO] odoo_mercadopago
cd odoo_mercadopago
chmod +x install.sh
./install.sh
```

#### Opción 2: Instalación Manual

1. **Copiar el módulo a la carpeta addons:**
   ```bash
   cp -r odoo_mercadopago /path/to/odoo/addons/
   ```

2. **Instalar dependencias:**
   ```bash
   pip3 install requests
   ```

3. **Reiniciar Odoo:**
   ```bash
   sudo systemctl restart odoo
   # O si usas el binario:
   ./odoo-bin -c /etc/odoo.conf
   ```

4. **Instalar el módulo en Odoo:**
   - Ir a **Aplicaciones**
   - Click en **Actualizar lista de aplicaciones**
   - Buscar "Mercado Pago"
   - Click en **Instalar**

## ⚙️ Configuración

### 1. Obtener Credenciales de Mercado Pago

1. Crear cuenta en [Mercado Pago](https://www.mercadopago.com.mx)
2. Ir al [Panel de Desarrolladores](https://www.mercadopago.com.mx/developers/panel)
3. Crear una aplicación
4. Obtener credenciales:
   - **Public Key** (pk_test_... para pruebas / pk_live_... para producción)
   - **Access Token** (TEST-... para pruebas / APP_USR-... para producción)

### 2. Configurar en Odoo

1. Ir a **Mercado Pago > Configuración**
2. Click en **Crear**
3. Completar datos:
   - **Compañía**: Seleccionar tu compañía
   - **Public Key**: Pegar tu Public Key
   - **Access Token**: Pegar tu Access Token
   - **Modo de Prueba**: ✅ Activado (para desarrollo)
   - **Número Máximo de Cuotas**: 12 (o según preferencia)
   - **Descriptor de Estado de Cuenta**: "MI NEGOCIO"
4. **Guardar**

### 3. Configurar Webhooks (Opcional pero Recomendado)

Para recibir notificaciones automáticas de pago:

1. En el Panel de Mercado Pago, ir a **Webhooks**
2. Agregar URL de tu sitio:
   ```
   https://tu-dominio.com/payment/mercadopago/webhook
   ```
3. Seleccionar eventos: **Pagos**

## 📝 Uso

### Crear un Pago (Backend)

1. Ir a **Mercado Pago > Pagos**
2. Click en **Crear**
3. Completar:
   - **Cliente**: Seleccionar cliente
   - **Monto**: Ingresar monto
   - **Descripción**: Descripción del pago
   - **Email del Pagador**: Email del cliente
4. Click en **Crear Link de Pago**
5. Compartir el link generado con el cliente

### Formulario de Checkout (Frontend)

Acceder a la URL del checkout:
```
https://tu-dominio.com/payment/mercadopago/checkout
```

## 🧪 Pruebas

### Tarjetas de Prueba

Para realizar pruebas en modo de prueba, usa estas tarjetas:

| Tarjeta | Número | CVV | Fecha | Resultado |
|---------|---------|-----|-------|-----------|
| **Visa** | 4509 9535 6623 3704 | 123 | 11/25 | ✅ Aprobado |
| **Mastercard** | 5031 7557 3453 0604 | 123 | 11/25 | ✅ Aprobado |
| **American Express** | 3711 803032 57522 | 1234 | 11/25 | ✅ Aprobado |
| Visa (Rechazo) | 4111 1111 1111 1111 | 123 | 11/25 | ❌ Rechazado |

Más información: [Tarjetas de Prueba MP](https://www.mercadopago.com.mx/developers/es/docs/checkout-pro/additional-content/test-cards)

## 🔌 API y Endpoints

### Endpoints Disponibles

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/payment/mercadopago/create` | POST (JSON) | Crear nuevo pago |
| `/payment/mercadopago/webhook` | POST (JSON) | Recibir notificaciones de MP |
| `/payment/mercadopago/checkout` | GET | Formulario de checkout |
| `/payment/mercadopago/success` | GET | Página de éxito |
| `/payment/mercadopago/failure` | GET | Página de error |
| `/payment/mercadopago/pending` | GET | Página de pendiente |

### Ejemplo de Uso de API

```python
# Crear pago desde código Python
payment = self.env['mercadopago.payment'].create({
    'partner_id': partner.id,
    'amount': 1500.00,
    'description': 'Pago de servicios',
    'payer_email': 'cliente@ejemplo.com',
})

# Generar link de pago
payment.action_create_preference()

# Obtener URL de pago
print(payment.mp_init_point)
```

```javascript
// Crear pago desde JavaScript (JSON-RPC)
fetch('/payment/mercadopago/create', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    jsonrpc: "2.0",
    method: "call",
    params: {
      partner_id: 1,
      amount: 1500.00,
      description: "Pago de servicios"
    }
  })
})
.then(response => response.json())
.then(data => {
  if (data.result.success) {
    window.location.href = data.result.init_point;
  }
});
```

## 📊 Estructura del Módulo

```
odoo_mercadopago/
├── __init__.py
├── __manifest__.py
├── README.md
├── EXAMPLES.md
├── FAQ.md
├── install.sh
├── controllers/
│   ├── __init__.py
│   └── mercadopago_controller.py
├── models/
│   ├── __init__.py
│   ├── mercadopago_config.py
│   └── mercadopago_payment.py
├── views/
│   ├── mercadopago_config_view.xml
│   ├── mercadopago_payment_view.xml
│   ├── mercadopago_templates.xml
│   ├── mercadopago_assets.xml
│   └── mercadopago_menu.xml
├── static/
│   ├── description/
│   │   ├── icon.png
│   │   └── banner.png
│   └── src/
│       └── js/
│           └── mercadopago_checkout.js
├── security/
│   └── ir.model.access.csv
└── data/
    └── ir_sequence_data.xml
```

## 🔧 Configuración Avanzada

### Variables de Entorno (Opcional)

Crea un archivo `.env` para gestionar credenciales:

```bash
# Credenciales de Prueba
MP_PUBLIC_KEY_TEST=TEST-xxxxx
MP_ACCESS_TOKEN_TEST=TEST-xxxxx

# Credenciales de Producción
MP_PUBLIC_KEY_PROD=APP_USR-xxxxx
MP_ACCESS_TOKEN_PROD=APP_USR-xxxxx
```

### Webhooks Locales (Desarrollo)

Para probar webhooks en desarrollo local, usa **ngrok**:

```bash
# Instalar ngrok
brew install ngrok  # macOS
# o descargar de https://ngrok.com/

# Ejecutar ngrok
ngrok http 8069

# Copiar la URL HTTPS generada y configurarla en Mercado Pago
```

## 🐛 Solución de Problemas

### Error: "No se encontró configuración de Mercado Pago"
**Solución**: Crear una configuración en **Mercado Pago > Configuración**

### Los webhooks no funcionan
**Solución**:
1. Verificar que la URL sea accesible públicamente
2. Usar HTTPS en producción
3. Revisar logs: `sudo tail -f /var/log/odoo/odoo-server.log`

### Pagos quedan en "Pendiente"
**Solución**:
1. Click en "Verificar Estado"
2. Verificar configuración de webhooks
3. Revisar estado en panel de Mercado Pago

### Error: "requests module not found"
**Solución**: `pip3 install requests`

## 📚 Documentación Adicional

- **EXAMPLES.md** - Ejemplos de código y uso de API
- **FAQ.md** - Preguntas frecuentes
- [Documentación Oficial MP](https://www.mercadopago.com.mx/developers/es/docs)
- [API Reference](https://www.mercadopago.com.mx/developers/es/reference)

## 🤝 Integración con Otros Módulos

Este módulo es completamente independiente pero puede integrarse fácilmente con otros módulos de Odoo:

```python
# Ejemplo: Integrar con tu módulo personalizado
class MiModelo(models.Model):
    _name = 'mi.modelo'
    
    payment_id = fields.Many2one('mercadopago.payment', string='Pago MP')
    
    def action_create_payment(self):
        payment = self.env['mercadopago.payment'].create({
            'partner_id': self.partner_id.id,
            'amount': self.total_amount,
            'description': f'Pago de {self.name}',
        })
        payment.action_create_preference()
        return {
            'type': 'ir.actions.act_url',
            'url': payment.mp_init_point,
            'target': 'new',
        }
```

## 🎯 Roadmap

Próximas características:

- [ ] Pagos recurrentes (suscripciones)
- [ ] Split payments
- [ ] Integración con facturación automática
- [ ] Dashboard de analytics
- [ ] QR codes para pagos
- [ ] Notificaciones por email/SMS
- [ ] Punto de venta (POS)

## 👨‍💻 Autor

**Christian Torres PeeWee**

## 📄 Licencia

Este módulo está licenciado bajo [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html)

## 🌟 Soporte

¿Necesitas ayuda?

- 📧 Email: soporte@ejemplo.com
- 📖 Documentación: [Wiki del proyecto]
- 🐛 Reportar bugs: [GitHub Issues]

## 💖 Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

---

<div align="center">
  <strong>¿Te gusta este módulo? ⭐ Dale una estrella en GitHub!</strong>
  
  Hecho con ❤️ para la comunidad de Odoo
</div>
