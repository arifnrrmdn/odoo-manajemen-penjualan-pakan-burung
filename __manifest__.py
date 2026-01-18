{
    'name': 'Penjualan Pakan Burung',
    'version': '1.0',
    'summary': 'Sistem Penjualan Pakan Burung dengan CRM',
    'category': 'Sales',
    'author': 'Arif Nur Ramadhan',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pakan_views.xml',
        'views/partner_views.xml',
        'views/transaksi_views.xml',
        'views/crm_views.xml',
        'views/pakan_burung_views.xml',
    ],
    'application': True,
    'installable': True,
}
