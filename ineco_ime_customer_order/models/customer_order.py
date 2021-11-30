# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from odoo import api, fields, models
# from odoo.exceptions import except_orm, Warning, RedirectWarning


class InecoCustomerOrder(models.Model):
    _name = 'ineco.customer.order'
    _description = 'Customer Order Confirmation'
    _inherit = ['mail.thread']

    name = fields.Char(string='Order Number', required=1, track_visibility='onchange', default='NEW', readonly='1')
    date_order = fields.Date(string='Order Date', required=1, track_visibility='onchange',
                             default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    partner_id = fields.Many2one('res.partner', string='Customer')

# domain=[('customer', '=', True), ('supplier', '=', False)], required=1, track_visibility='onchange')

    user_id = fields.Many2one('res.users', string='User', required=1, track_visibility='onchange')
    order_refer = fields.Char(string='Customer Order Reference', track_visibility='onchange')
    order_line_ids = fields.One2many('ineco.customer.order.line', 'order_id', string='Order Lines')
    note = fields.Text(string='Note', track_visibility='onchange')

    _default = {
        'user_id': lambda self, cr, uid, ctx: uid,
    }

    @api.model
    def create(self, vals):
        new_running_number = self.env['ir.sequence'].next_by_code('ineco.customer.order')
        vals['name'] = new_running_number
        record = super(InecoCustomerOrder, self).create(vals)
        return record


class InecoCustomerOrderLine(models.Model):
    _name = 'ineco.customer.order.line'
    _description = 'Customer Order Lines'

    name = fields.Char(string='Description', required=1)
    sequence = fields.Integer(string='Sequence', default=10)
    # product_id = fields.Many2one('product.product', string='Product', required=1, domain=[('sale_ok', '=', True)])
    product_id = fields.Many2one('product.partcode', string='Product', required=1)
    order_qty = fields.Integer(string='Order Qty', required=1)
    date_shipment = fields.Date(string='Ship Date', required=1)
    sale_order_qty = fields.Integer(string='So Qty')
    ship_qty = fields.Integer(string='Delivery Qty')
    balance_qty = fields.Integer(string='Balance Qty')
    order_id = fields.Many2one('ineco.customer.order', string='Customer Order', required=1)
