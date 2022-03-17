from email.policy import default
from odoo import api, fields, models


class salesorder(models.Model):
    _name = 'sale.order'
    _description = 'Sale order'

    is_booking_order = fields.Boolean(string='Is booking order', readonly=True, default=True)
    team_id = fields.Many2one(comodel_name='res.users', string='Service team', readonly=False, default=False, required=True)
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Team leader id', readonly=False, default=team_id, required=True)
    team_member_ids= fields.Many2many(comodel_name='res.users', string='Service member', readonly=False, default=team_id, required=True)
    booking_start= fields.Datetime(string='Datetime', readonly=False, required=True)
    booking_end= fields.Datetime(string='Datetime', readonly=False, required=True)
    
