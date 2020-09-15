# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools.translate import html_translate


class ResCompany(models.Model):
    _inherit = 'res.company'

    so_terms_and_conditions = fields.Html('Sale order terms and conditions', translate=html_translate)
    show_so_terms_and_conditions = fields.Boolean('Show terms on SO report')
