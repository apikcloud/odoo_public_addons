###############################################################################
#
# Copyright(c): 2020 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# See LICENSE file for full copyright and licensing details.
# All Rights Reserved
#
###############################################################################
{
    'name': 'SO terms & conditions',
    'version': '12.0.1.0',
    'summary': 'Add terms and conditions to the SO PDF report',
    'description': '',
    'category': 'Sales',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'sale'
    ],
    'data': [
        'report/sale_order.xml',
        'templates/assets.xml',
        'views/res_company.xml'
    ],
    'installable': True,
    'application': False,
}
