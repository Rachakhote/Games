# -*- coding: utf-8 -*-


# from datetime import datetime, timedelta
from odoo import api, fields, models
# from odoo.exceptions import except_orm, Warning, RedirectWarning


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # partcode_ids = fields.One2many('product.partcode', 'product_id', string='Part Codes')
    partcode_ids = fields.One2many('product.partcode', 'product_id', string='Part Codes')


class ProductPartCode(models.Model):
    _name = 'product.partcode'
    _description = 'Product Customer Part Code'

    name = fields.Char(string='Part Code', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Product')
