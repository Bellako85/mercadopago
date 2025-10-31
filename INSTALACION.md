# 🎉 MÓDULO MERCADO PAGO - INSTALACIÓN RÁPIDA

## 📍 Ubicación del Módulo

Tu módulo **odoo_mercadopago** está listo en:

```
/Users/nueva/Desktop/custom addons/odoo_mercadopago
```

---

## 🚀 INSTALACIÓN RÁPIDA

### Método 1: Instalación Automática (Recomendado)

```bash
cd "/Users/nueva/Desktop/custom addons/odoo_mercadopago"
./install.sh
```

### Método 2: Manual

#### Paso 1: Copiar a la carpeta de addons de Odoo

```bash
# Si tu Odoo está en /opt/odoo:
sudo cp -r "/Users/nueva/Desktop/custom addons/odoo_mercadopago" /opt/odoo/addons/

# O si está en otro lugar:
sudo cp -r "/Users/nueva/Desktop/custom addons/odoo_mercadopago" /ruta/de/tu/odoo/addons/

# Dar permisos
sudo chown -R odoo:odoo /opt/odoo/addons/odoo_mercadopago
```

#### Paso 2: Agregar a la configuración de Odoo (Alternativa)

Si prefieres mantener el módulo en tu carpeta actual:

```bash
# Editar configuración de Odoo
sudo nano /etc/odoo/odoo.conf

# O si usas odoo17.conf:
sudo nano /etc/odoo/odoo17.conf

# Buscar la línea "addons_path" y agregar tu carpeta:
addons_path = /opt/odoo/addons,/Users/nueva/Desktop/custom addons

# Guardar: Ctrl+O, Enter, Ctrl+X
```

#### Paso 3: Reiniciar Odoo

```bash
# Con systemctl:
sudo systemctl restart odoo

# O con el binario directamente:
./odoo-bin -c /etc/odoo/odoo.conf

# O con odoo17:
sudo systemctl restart odoo17
```

#### Paso 4: Instalar en Odoo

1. Abrir Odoo en el navegador
2. Ir a **Aplicaciones**
3. Click en el menú de tres puntos (⋮) → **Actualizar lista de aplicaciones**
4. Buscar "**Mercado Pago**"
5. Click en **Instalar**

---

## ⚙️ CONFIGURACIÓN POST-INSTALACIÓN

### 1. Obtener Credenciales

1. Ir a: https://www.mercadopago.com.mx/developers/panel
2. Crear aplicación (si no tienes una)
3. Copiar:
   - **Public Key**: `TEST-xxxxx...` (para pruebas)
   - **Access Token**: `TEST-xxxxx...` (para pruebas)

### 2. Configurar en Odoo

1. Ir a: **Mercado Pago > Configuración**
2. Click en **Crear**
3. Completar:
   ```
   Compañía: [Tu compañía]
   Public Key: TEST-xxxxx...
   Access Token: TEST-xxxxx...
   Modo de Prueba: ✅ (activado)
   Número de Cuotas: 12
   ```
4. **Guardar**

---

## 🧪 PROBAR EL MÓDULO

### Crear un Pago de Prueba

1. Ir a: **Mercado Pago > Pagos**
2. Click en **Crear**
3. Completar:
   ```
   Cliente: [Seleccionar cliente]
   Monto: 100.00
   Descripción: Pago de prueba
   Email: test@ejemplo.com
   ```
4. Click en **Crear Link de Pago**
5. Click en **Abrir Link de Pago**

### Tarjeta de Prueba

```
Número: 4509 9535 6623 3704
CVV: 123
Fecha: 11/25
Nombre: APRO
```

---

## 📂 ESTRUCTURA DEL MÓDULO

```
odoo_mercadopago/
├── 📄 README.md              ← Documentación completa
├── 📄 EXAMPLES.md            ← 15 ejemplos de código
├── 📄 FAQ.md                 ← Preguntas frecuentes
├── 🔧 install.sh             ← Script de instalación
├── ⚙️  .env.example           ← Plantilla de configuración
├── 📁 models/                ← Lógica de negocio
│   ├── mercadopago_config.py
│   └── mercadopago_payment.py
├── 📁 controllers/           ← Endpoints HTTP
│   └── mercadopago_controller.py
├── 📁 views/                 ← Interfaces UI
│   ├── mercadopago_config_view.xml
│   ├── mercadopago_payment_view.xml
│   ├── mercadopago_templates.xml
│   ├── mercadopago_assets.xml
│   └── mercadopago_menu.xml
├── 📁 static/src/js/         ← JavaScript frontend
│   └── mercadopago_checkout.js
├── 📁 security/              ← Permisos
│   └── ir.model.access.csv
└── 📁 data/                  ← Datos iniciales
    └── ir_sequence_data.xml
```

---

## ✅ VERIFICAR INSTALACIÓN

```bash
# Verificar que todos los archivos estén presentes
cd "/Users/nueva/Desktop/custom addons/odoo_mercadopago"
ls -la

# Debería mostrar:
# - README.md
# - EXAMPLES.md
# - FAQ.md
# - install.sh
# - __manifest__.py
# - models/, controllers/, views/, static/, security/, data/
```

---

## 🔍 ENCONTRAR ODOO EN TU SISTEMA

Si no sabes dónde está instalado Odoo:

```bash
# Buscar el ejecutable de Odoo
which odoo-bin
which odoo

# Buscar el archivo de configuración
sudo find / -name "odoo.conf" 2>/dev/null

# Ver el servicio de Odoo
systemctl status odoo
# o
systemctl status odoo17

# Ver la configuración del servicio
sudo cat /etc/systemd/system/odoo.service
```

---

## 🆘 PROBLEMAS COMUNES

### "Módulo no aparece en Aplicaciones"

```bash
# Verificar que la ruta esté en addons_path
grep addons_path /etc/odoo/odoo.conf

# Reiniciar Odoo
sudo systemctl restart odoo

# Actualizar lista de aplicaciones en Odoo
```

### "Error de permisos"

```bash
# Dar permisos correctos
sudo chown -R odoo:odoo /ruta/a/odoo_mercadopago
sudo chmod -R 755 /ruta/a/odoo_mercadopago
```

### "requests module not found"

```bash
# Instalar requests
pip3 install requests

# O para el usuario de Odoo:
sudo -u odoo pip3 install requests
```

---

## 📚 RECURSOS

- **README.md** - Guía completa
- **EXAMPLES.md** - Ejemplos de código
- **FAQ.md** - Preguntas frecuentes
- [Docs Mercado Pago](https://www.mercadopago.com.mx/developers)

---

## 🎯 SIGUIENTE PASO

Una vez instalado el módulo:

1. **Configurar credenciales** en Mercado Pago > Configuración
2. **Crear un pago de prueba** en Mercado Pago > Pagos
3. **Probar con tarjeta de prueba**
4. **¡Listo para usar!** 🚀

---

**¿Necesitas ayuda?** Consulta README.md o FAQ.md
