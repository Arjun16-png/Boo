from asyncore import dispatcher_with_send
from email.policy import default
from odoo import api, fields, models


class saleworkorder(models.Model):
    _name = 'sale.work.order'
    _description = 'Sale work order'

    name = fields.Char(string='WO number', readonly=True, default='new', required=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Booking order ref', required=False)
    team_id = fields.Many2one(comodel_name='res.users', string='Service team', readonly=False, default=False, required=True)
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Team leader id', readonly=False, default=team_id, required=True)
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Service member', readonly=False, default=team_id, required=True)
    planned_start = fields.Datetime(string='Planned start', readonly=False, required=True)
    planned_end = fields.Datetime(string='Planned end', readonly=False, required=True)
    date_start = fields.Datetime(string='Date start', readonly=True, default=False, required=True)
    date_end = fields.Datetime(string='Date end', readonly=True, default=False, required=True)
    state = fields.Selection(string='',selection=[('pending', 'pending'), ('in-progress', 'in-progress'), ('done', 'done'), ('cancel', 'cancel')])
    notes = fields.Test(string='Notes', readonly=False, default=False, required=False)
