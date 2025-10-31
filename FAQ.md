# Preguntas Frecuentes (FAQ) - Mercado Pago en Odoo 17

## 🔧 Instalación y Configuración

### ¿Cómo obtengo mis credenciales de Mercado Pago?

1. Ingresa a [Mercado Pago Developers](https://www.mercadopago.com.mx/developers/panel)
2. Crea una aplicación o selecciona una existente
3. Ve a "Credenciales" en el menú lateral
4. Encontrarás dos juegos de credenciales:
   - **Prueba**: Para desarrollo (empiezan con TEST-)
   - **Producción**: Para ambiente real (empiezan con APP_USR-)

### ¿Puedo usar el mismo módulo para pruebas y producción?

Sí, el módulo maneja ambos ambientes. Solo cambia el campo "Modo de Prueba" en la configuración:
- **Activado**: Usa credenciales de prueba
- **Desactivado**: Usa credenciales de producción

### ¿Es necesario tener una cuenta verificada de Mercado Pago?

Para **pruebas**: No es necesario
Para **producción**: Sí, debes tener una cuenta verificada y tu aplicación debe estar aprobada por Mercado Pago.

---

## 💳 Pagos

### ¿Qué métodos de pago acepta?

Mercado Pago soporta:
- ✅ Tarjetas de crédito (Visa, Mastercard, Amex)
- ✅ Tarjetas de débito
- ✅ Efectivo (OXXO, 7-Eleven, etc.)
- ✅ Transferencias bancarias
- ✅ Dinero en cuenta de Mercado Pago

### ¿Se pueden hacer pagos en cuotas?

Sí, configura el número máximo de cuotas en **Mercado Pago > Configuración > Número Máximo de Cuotas**. Los clientes podrán elegir hasta ese número de cuotas al pagar.

### ¿Cómo funcionan los pagos en efectivo?

1. El cliente elige pagar en efectivo
2. Mercado Pago genera un código de barras o referencia
3. El cliente paga en el punto físico (OXXO, 7-Eleven, etc.)
4. El webhook notifica cuando el pago es confirmado

### ¿Cuánto tarda en confirmarse un pago?

- **Tarjeta de crédito/débito**: Instantáneo (segundos)
- **Efectivo**: De 1 a 3 días hábiles
- **Transferencia bancaria**: De 1 a 2 días hábiles

---

## 🔔 Webhooks y Notificaciones

### ¿Qué son los webhooks?

Los webhooks son notificaciones automáticas que Mercado Pago envía a tu servidor cuando ocurre un evento (pago aprobado, rechazado, etc.).

### ¿Es obligatorio configurar webhooks?

No es obligatorio, pero **altamente recomendado** para:
- Actualizar automáticamente el estado de los pagos
- Confirmar pagos en efectivo cuando se completan
- Mantener sincronizados los datos sin intervención manual

### ¿Cómo configuro los webhooks?

1. En Odoo, anota la URL de webhook (por defecto: `https://tu-dominio.com/payment/mercadopago/webhook`)
2. En el [Panel de Mercado Pago](https://www.mercadopago.com.mx/developers/panel), ve a "Webhooks"
3. Agrega tu URL
4. Selecciona los eventos a notificar (recomendado: "Pagos")

### Mi webhook no funciona en localhost, ¿qué hago?

Mercado Pago requiere una URL pública con HTTPS. Para desarrollo local:

1. Usa [ngrok](https://ngrok.com/):
   ```bash
   ngrok http 8069
   ```
2. Copia la URL HTTPS de ngrok
3. Configúrala como webhook en Mercado Pago

---

## 🔍 Troubleshooting

### Error: "No se encontró una configuración activa de Mercado Pago"

**Solución**: 
1. Ve a **Mercado Pago > Configuración**
2. Crea un nuevo registro
3. Verifica que esté marcado como "Activo"

### Error: "Error al comunicarse con Mercado Pago: 401 Unauthorized"

**Causa**: Credenciales incorrectas o expiradas

**Solución**:
1. Verifica que las credenciales sean correctas
2. Verifica que el "Modo de Prueba" coincida con el tipo de credenciales
3. Regenera las credenciales en el panel de Mercado Pago si es necesario

### Los pagos quedan en estado "Pendiente" y no se actualizan

**Posibles causas**:
1. Webhooks no configurados
2. URL de webhook incorrecta
3. Servidor no accesible públicamente

**Solución**:
1. Configura correctamente los webhooks
2. Manualmente: hacer clic en "Verificar Estado" en el pago
3. Verifica logs de Odoo: `sudo tail -f /var/log/odoo/odoo-server.log`

### Error: "Module requests not found"

**Solución**:
```bash
pip3 install requests
sudo systemctl restart odoo
```

### El link de pago no redirige correctamente

**Solución**:
1. Verifica que las URLs de retorno estén correctamente configuradas
2. Si no las configuraste, se usarán las por defecto
3. Asegúrate de que tu dominio sea accesible

### No aparece el menú de Mercado Pago después de instalar

**Solución**:
1. Actualiza la página (Ctrl+F5)
2. Cierra sesión y vuelve a iniciar
3. Verifica que el módulo esté correctamente instalado
4. Revisa los logs por errores de instalación

---

## 💰 Costos y Comisiones

### ¿Cuánto cobra Mercado Pago por transacción?

Las comisiones varían según:
- País
- Tipo de pago (tarjeta, efectivo, etc.)
- Volumen de transacciones

Consulta las [tasas actuales](https://www.mercadopago.com.mx/costs-section/1) en tu país.

### ¿El módulo de Odoo tiene costo adicional?

No, este módulo es gratuito y de código abierto (LGPL-3).

---

## 🔐 Seguridad

### ¿Es seguro usar Mercado Pago?

Sí, Mercado Pago cumple con estándares PCI-DSS Level 1 y usa encriptación SSL/TLS para todas las transacciones.

### ¿Dónde se almacenan los datos de las tarjetas?

Los datos sensibles (número de tarjeta, CVV) **nunca** pasan por tu servidor. Se procesan directamente en los servidores de Mercado Pago.

### ¿Qué información se guarda en Odoo?

Solo información de referencia:
- ID de transacción
- Estado del pago
- Monto
- Información del cliente
- **NO** se guardan datos de tarjetas

### ¿Debo usar HTTPS?

**En producción: SÍ, obligatorio**. Mercado Pago requiere HTTPS para webhooks y URLs de retorno.

---

## 🌐 Internacionalización

### ¿Funciona en otros países además de México?

Sí, Mercado Pago opera en:
- 🇦🇷 Argentina
- 🇧🇷 Brasil
- 🇨🇱 Chile
- 🇨🇴 Colombia
- 🇲🇽 México
- 🇵🇪 Perú
- 🇺🇾 Uruguay

Solo necesitas credenciales de tu país.

### ¿Puedo aceptar pagos en múltiples monedas?

Sí, pero cada cuenta de Mercado Pago opera en la moneda de su país. Para múltiples monedas necesitarías múltiples configuraciones.

---

## 📱 Integraciones

### ¿Se puede integrar con el punto de venta (POS)?

Actualmente el módulo está diseñado para e-commerce. Para POS requeriría desarrollo adicional.

### ¿Se integra con facturación electrónica?

El módulo guarda los pagos, pero no genera facturas automáticamente. Puedes extenderlo para crear facturas al aprobar pagos.

### ¿Puedo vincular pagos con órdenes de venta?

Sí, puedes extender el módulo fácilmente para vincular con `sale.order`:

```python
class MercadoPagoPayment(models.Model):
    _inherit = 'mercadopago.payment'
    
    sale_order_id = fields.Many2one('sale.order', string='Orden de Venta')
```

---

## 🛠️ Desarrollo

### ¿Puedo personalizar el módulo?

Sí, el módulo es de código abierto. Puedes:
- Heredar los modelos
- Agregar campos personalizados
- Crear nuevas vistas
- Extender la funcionalidad

### ¿Cómo agrego un campo personalizado al pago?

```python
class MercadoPagoPaymentCustom(models.Model):
    _inherit = 'mercadopago.payment'
    
    custom_field = fields.Char(string='Mi Campo Personalizado')
```

### ¿Puedo usar este módulo como base para otro gateway de pago?

Sí, la estructura es modular y puede adaptarse para otros proveedores de pago.

---

## 📊 Reportes

### ¿Puedo exportar reportes de pagos?

Sí, desde **Mercado Pago > Pagos**:
1. Aplica filtros si necesitas
2. Selecciona los registros
3. Click en "Acción > Exportar"
4. Elige formato (XLSX, CSV)

### ¿Hay reportes de análisis incluidos?

El módulo incluye vistas de lista con filtros y agrupaciones. Para reportes avanzados puedes:
- Usar la vista de pivote
- Crear reportes Qweb personalizados
- Integrar con herramientas BI

---

## 🔄 Actualizaciones

### ¿Cómo actualizo el módulo?

1. Descarga la nueva versión
2. Reemplaza los archivos
3. Reinicia Odoo
4. Ve a **Aplicaciones > Actualizar lista de aplicaciones**
5. Busca el módulo y haz clic en "Actualizar"

### ¿Se perderán mis datos al actualizar?

No, las actualizaciones preservan los datos. Pero siempre haz backup antes de actualizar.

---

## 📞 Soporte

### ¿Dónde obtengo ayuda con el módulo?

1. Lee la documentación: `README.md`
2. Consulta ejemplos: `EXAMPLES.md`
3. Revisa este FAQ
4. Revisa los logs de Odoo

### ¿Dónde obtengo ayuda con Mercado Pago?

- [Centro de ayuda](https://www.mercadopago.com.mx/ayuda)
- [Documentación técnica](https://www.mercadopago.com.mx/developers/es/docs)
- [Foro de desarrolladores](https://www.mercadopago.com.mx/developers/es/support)

---

## 🧪 Testing

### ¿Cómo pruebo el módulo sin hacer pagos reales?

1. Activa "Modo de Prueba" en la configuración
2. Usa credenciales de prueba (TEST-)
3. Usa [tarjetas de prueba](https://www.mercadopago.com.mx/developers/es/docs/checkout-pro/additional-content/test-cards)

### Tarjetas de prueba recomendadas

```
Aprobada:
- Número: 4509 9535 6623 3704
- CVV: 123
- Fecha: 11/25

Rechazada por fondos insuficientes:
- Número: 5031 4332 1540 6351
- CVV: 123
- Fecha: 11/25
```

### ¿Cómo simulo un pago en efectivo?

En modo prueba, los pagos en efectivo se marcan automáticamente como aprobados después de unos minutos para facilitar testing.

---

## 🎯 Mejores Prácticas

### Recomendaciones de seguridad

1. ✅ Usa HTTPS en producción
2. ✅ Mantén las credenciales seguras
3. ✅ No compartas el Access Token
4. ✅ Usa modo de prueba para desarrollo
5. ✅ Haz backups regulares

### Recomendaciones de uso

1. ✅ Configura webhooks
2. ✅ Valida pagos antes de entregar productos
3. ✅ Guarda registros de todas las transacciones
4. ✅ Monitorea pagos pendientes
5. ✅ Prueba en ambiente de test antes de producción

### Optimización

1. ✅ Limpia pagos cancelados antiguos periódicamente
2. ✅ Indexa campos de búsqueda frecuente
3. ✅ Usa cache para configuraciones
4. ✅ Monitorea logs de errores

---

¿Tienes más preguntas? Consulta la [documentación de Mercado Pago](https://www.mercadopago.com.mx/developers/es/docs) o revisa el código del módulo.
