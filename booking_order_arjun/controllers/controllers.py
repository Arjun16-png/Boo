# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderArjun(http.Controller):
#     @http.route('/booking_order_arjun/booking_order_arjun/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_arjun/booking_order_arjun/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_arjun.listing', {
#             'root': '/booking_order_arjun/booking_order_arjun',
#             'objects': http.request.env['booking_order_arjun.booking_order_arjun'].search([]),
#         })

#     @http.route('/booking_order_arjun/booking_order_arjun/objects/<model("booking_order_arjun.booking_order_arjun"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_arjun.object', {
#             'object': obj
#         })
