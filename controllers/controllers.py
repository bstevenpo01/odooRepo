# -*- coding: utf-8 -*-
# from odoo import http


# class Alquiler(http.Controller):
#     @http.route('/alquiler/alquiler/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquiler/alquiler/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquiler.listing', {
#             'root': '/alquiler/alquiler',
#             'objects': http.request.env['alquiler.alquiler'].search([]),
#         })

#     @http.route('/alquiler/alquiler/objects/<model("alquiler.alquiler"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquiler.object', {
#             'object': obj
#         })
