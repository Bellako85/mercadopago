# Ejemplos de Uso - API Mercado Pago en Odoo 17
# ================================================

## 1. Crear un Pago desde Python (dentro de Odoo)

```python
# Ejemplo 1: Crear un pago básico
payment = self.env['mercadopago.payment'].create({
    'partner_id': 1,  # ID del cliente
    'amount': 1500.00,
    'description': 'Pago por lentes graduados',
    'currency_id': self.env.ref('base.MXN').id,
})

# Crear la preferencia en Mercado Pago
payment.action_create_preference()

# Obtener el link de pago
print(f"Link de pago: {payment.mp_init_point}")
```

```python
# Ejemplo 2: Crear un pago con más detalles
cliente = self.env['res.partner'].browse(10)
payment = self.env['mercadopago.payment'].create({
    'partner_id': cliente.id,
    'amount': 2500.00,
    'description': f'Pago de servicios para {cliente.name}',
    'payer_email': cliente.email,
})
payment.action_create_preference()
```

## 2. Verificar Estado de un Pago

```python
# Obtener un pago por referencia
payment = self.env['mercadopago.payment'].search([
    ('reference', '=', 'MP00010')
], limit=1)

# Verificar estado en Mercado Pago
payment.action_check_payment_status()

# Verificar el estado actual
if payment.state == 'approved':
    print("¡Pago aprobado!")
elif payment.state == 'rejected':
    print("Pago rechazado")
```

## 3. Reembolsar un Pago

```python
# Obtener un pago aprobado
payment = self.env['mercadopago.payment'].search([
    ('state', '=', 'approved'),
    ('mp_payment_id', '=', '123456789')
], limit=1)

# Realizar reembolso
payment.action_refund_payment()
```

## 4. Buscar Pagos

```python
# Buscar todos los pagos pendientes
pending_payments = self.env['mercadopago.payment'].search([
    ('state', '=', 'pending')
])

# Buscar pagos de un cliente específico
partner_payments = self.env['mercadopago.payment'].search([
    ('partner_id', '=', partner_id),
    ('state', 'in', ['approved', 'pending'])
])

# Buscar pagos del mes actual
from datetime import datetime
payments_this_month = self.env['mercadopago.payment'].search([
    ('create_date', '>=', datetime.now().strftime('%Y-%m-01'))
])
```

## 5. Crear Pago desde API JSON-RPC

```bash
# Usando curl
curl -X POST https://tu-dominio.com/payment/mercadopago/create \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
      "partner_id": 1,
      "amount": 1500.00,
      "description": "Pago de consulta"
    }
  }'
```

```python
# Usando requests en Python
import requests
import json

url = "https://tu-dominio.com/payment/mercadopago/create"
headers = {"Content-Type": "application/json"}
data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "partner_id": 1,
        "amount": 1500.00,
        "description": "Pago de lentes"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

if result.get('result', {}).get('success'):
    print(f"Pago creado: {result['result']['init_point']}")
```

```javascript
// Usando JavaScript (fetch)
fetch('https://tu-dominio.com/payment/mercadopago/create', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    jsonrpc: "2.0",
    method: "call",
    params: {
      partner_id: 1,
      amount: 1500.00,
      description: "Pago de consulta"
    }
  })
})
.then(response => response.json())
.then(data => {
  if (data.result && data.result.success) {
    window.location.href = data.result.init_point;
  }
});
```

## 6. Procesar Webhook

```python
# El webhook se procesa automáticamente en el controlador
# Pero puedes simular el procesamiento manualmente:

payment = self.env['mercadopago.payment'].search([
    ('mp_payment_id', '=', '123456789')
], limit=1)

# Simular actualización desde webhook
mp_response = {
    'id': '123456789',
    'status': 'approved',
    'status_detail': 'accredited',
    'payment_method_id': 'visa',
    'payment_type_id': 'credit_card',
    'installments': 1,
    'payer': {
        'email': 'cliente@ejemplo.com',
        'identification': {
            'type': 'RFC',
            'number': 'XAXX010101000'
        }
    },
    'date_created': '2025-10-30T10:00:00.000Z',
    'date_approved': '2025-10-30T10:00:05.000Z'
}

payment._update_payment_from_mp_response(mp_response)
```

## 7. Obtener Configuración de Mercado Pago

```python
# Obtener la configuración activa
config = self.env['mercadopago.config'].search([
    ('company_id', '=', self.env.company.id),
    ('active', '=', True)
], limit=1)

# Obtener credenciales
credentials = config.get_credentials()
print(f"Public Key: {credentials['public_key']}")
print(f"Access Token: {credentials['access_token']}")
print(f"Modo de prueba: {credentials['is_test_mode']}")
```

## 8. Generar Link de Pago para Enviar por Email

```python
# Crear pago
payment = self.env['mercadopago.payment'].create({
    'partner_id': partner.id,
    'amount': 1500.00,
    'description': 'Pago de consulta oftalmológica',
    'payer_email': partner.email,
})

# Generar preferencia
payment.action_create_preference()

# Enviar email con el link
template = self.env.ref('mi_modulo.email_template_payment_link')
template.send_mail(payment.id, force_send=True)

# O construir un mensaje personalizado
message = f"""
Hola {partner.name},

Te enviamos el link para realizar tu pago:

Monto: ${payment.amount} MXN
Descripción: {payment.description}

Link de pago: {payment.mp_init_point}

Gracias por tu preferencia.
"""
```

## 9. Crear Pago con Cuotas

```python
# Crear pago con configuración de cuotas
payment = self.env['mercadopago.payment'].create({
    'partner_id': partner.id,
    'amount': 3000.00,
    'description': 'Pago de lentes progresivos',
    'installments': 6,  # 6 meses sin intereses
})

payment.action_create_preference()
```

## 10. Filtrar Pagos por Estado y Fecha

```python
from datetime import datetime, timedelta

# Pagos aprobados en los últimos 7 días
seven_days_ago = datetime.now() - timedelta(days=7)
recent_approved = self.env['mercadopago.payment'].search([
    ('state', '=', 'approved'),
    ('date_approved', '>=', seven_days_ago.strftime('%Y-%m-%d'))
])

# Total de ventas del mes
payments_this_month = self.env['mercadopago.payment'].search([
    ('state', '=', 'approved'),
    ('create_date', '>=', datetime.now().strftime('%Y-%m-01'))
])
total_sales = sum(payment.amount for payment in payments_this_month)
print(f"Ventas del mes: ${total_sales} MXN")
```

## 11. Webhook Testing (Simulación Local)

```python
# Para probar webhooks localmente sin esperar notificaciones reales:

# 1. Crear un pago
payment = self.env['mercadopago.payment'].create({
    'partner_id': 1,
    'amount': 100.00,
    'description': 'Pago de prueba',
    'mp_payment_id': '123456789',  # Simular ID de MP
})

# 2. Simular webhook
payment.action_check_payment_status()

# O actualizar manualmente
payment.write({
    'state': 'approved',
    'mp_status': 'approved',
    'date_approved': datetime.now()
})
```

## 12. Crear Checkout Personalizado (Widget)

```python
# En tu controlador personalizado
@http.route('/mi-checkout', type='http', auth='user', website=True)
def mi_checkout(self, **kwargs):
    # Obtener datos del usuario
    partner = request.env.user.partner_id
    
    # Crear pago
    payment = request.env['mercadopago.payment'].create({
        'partner_id': partner.id,
        'amount': kwargs.get('amount', 0),
        'description': kwargs.get('description', ''),
    })
    
    # Crear preferencia
    payment.action_create_preference()
    
    # Renderizar template personalizado
    return request.render('mi_modulo.mi_checkout_template', {
        'payment': payment,
        'partner': partner,
    })
```

## 13. Reportes y Estadísticas

```python
# Obtener estadísticas de pagos
from odoo import fields

def get_payment_stats(self):
    # Total de pagos por estado
    stats = {}
    for state in ['draft', 'pending', 'approved', 'rejected', 'cancelled']:
        count = self.env['mercadopago.payment'].search_count([
            ('state', '=', state)
        ])
        stats[state] = count
    
    # Pagos aprobados
    approved_payments = self.env['mercadopago.payment'].search([
        ('state', '=', 'approved')
    ])
    
    total_amount = sum(p.amount for p in approved_payments)
    average_amount = total_amount / len(approved_payments) if approved_payments else 0
    
    return {
        'stats': stats,
        'total_approved': len(approved_payments),
        'total_amount': total_amount,
        'average_amount': average_amount,
    }
```

## 14. Integración con Facturación

```python
# Crear factura después de pago aprobado
def create_invoice_from_payment(payment):
    if payment.state != 'approved':
        return False
    
    invoice = self.env['account.move'].create({
        'move_type': 'out_invoice',
        'partner_id': payment.partner_id.id,
        'invoice_date': fields.Date.today(),
        'invoice_line_ids': [(0, 0, {
            'name': payment.description,
            'quantity': 1,
            'price_unit': payment.amount,
        })],
    })
    
    # Vincular pago con factura
    payment.write({'invoice_id': invoice.id})
    
    return invoice
```

## 15. Manejo de Errores

```python
from odoo.exceptions import UserError

try:
    payment = self.env['mercadopago.payment'].create({
        'partner_id': partner.id,
        'amount': 1500.00,
        'description': 'Pago de consulta',
    })
    
    result = payment.action_create_preference()
    
except UserError as e:
    # Error de usuario (ej: configuración faltante)
    _logger.error(f"Error al crear pago: {str(e)}")
    return {'error': str(e)}
    
except Exception as e:
    # Error inesperado
    _logger.exception("Error inesperado al procesar pago")
    return {'error': 'Error al procesar el pago'}
```

---

## Notas Importantes

1. **Seguridad**: Nunca expongas tus credenciales en código público
2. **Testing**: Usa siempre el modo de prueba durante desarrollo
3. **Webhooks**: Configura webhooks en producción para actualizaciones automáticas
4. **Logs**: Revisa los logs de Odoo para debugging
5. **Timeout**: La API de Mercado Pago tiene timeout de 10 segundos

## Recursos

- [Documentación API Mercado Pago](https://www.mercadopago.com.mx/developers/es/reference)
- [Checkout Pro](https://www.mercadopago.com.mx/developers/es/docs/checkout-pro/landing)
- [Testing Guide](https://www.mercadopago.com.mx/developers/es/docs/checkout-pro/additional-content/test-cards)
