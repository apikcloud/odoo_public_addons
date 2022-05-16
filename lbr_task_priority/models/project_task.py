# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    priority_kanban = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ], string='Kanban priority', default='0')
