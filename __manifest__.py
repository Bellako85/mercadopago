# -*- coding: utf-8 -*-
{
    "name": "Mercado Pago Payment Gateway",
    "version": "17.0.1.0.0",
    "category": "Accounting/Payment Providers",
    "summary": "Integración completa con Mercado Pago - Checkout Pro, Webhooks, Reembolsos",
    "description": """
        Mercado Pago Payment Gateway para Odoo 17
        ===========================================
        
        Características principales:
        
        * Integración completa con API de Mercado Pago
        * Checkout Pro (redirección a Mercado Pago)
        * Soporte para múltiples métodos de pago (tarjetas, efectivo, transferencias)
        * Webhooks para actualizaciones automáticas de estado
        * Reembolsos automáticos
        * Modo de prueba y producción
        * Multi-moneda y multi-compañía
        * Configuración de cuotas
        * Panel de administración completo
        * API JSON-RPC para integraciones externas
        * Templates web responsive
        
        Métodos de pago soportados:
        
        * Tarjetas de crédito y débito (Visa, Mastercard, American Express, etc.)
        * Efectivo (OXXO, 7-Eleven, etc.)
        * Transferencias bancarias
        * Mercado Pago Wallet
        
        Requisitos:
        
        * Cuenta de Mercado Pago
        * Credenciales de API (Public Key y Access Token)
        * Python requests library
        
        Documentación:
        
        * README.md - Guía completa de instalación
        * EXAMPLES.md - Ejemplos de código
        * FAQ.md - Preguntas frecuentes
    """,
    "author": "Christian Torres PeeWee",
    "website": "https://www.mercadopago.com.mx",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "contacts",
        "website",
    ],
    "external_dependencies": {
        "python": ["requests"],
    },
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/mercadopago_config_view.xml",
        "views/mercadopago_payment_view.xml",
        "views/mercadopago_templates.xml",
        "views/mercadopago_assets.xml",
        "views/mercadopago_menu.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "odoo_mercadopago/static/src/js/mercadopago_checkout.js",
        ],
    },
    "images": [
        "static/description/banner.png",
        "static/description/icon.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "price": 0.00,
    "currency": "USD",
}
