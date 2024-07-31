###############################################################################
#
# Copyright(c): 2020 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# See LICENSE file for full copyright and licensing details.
# All Rights Reserved
#
###############################################################################
{
    'name': 'Task priority',
    'version': '11.0.1.0',
    'summary': 'Priority states for project tasks',
    'description': '',
    'category': 'Project Management',
    'author': 'Libreinnova',
    'website': 'https://github.com/libreinnova/odoo_public_addons',
    'license': 'AGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/icon.png'
    ],
    'depends': [
        'project'
    ],
    'data': [
        'templates/assets.xml',
        'views/project_task.xml'
    ],
    'installable': True,
    'application': False,
}
