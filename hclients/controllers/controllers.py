# -*- coding: utf-8 -*-
from odoo import http

# class Hclients(http.Controller):
#     @http.route('/hclients/hclients/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hclients/hclients/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hclients.listing', {
#             'root': '/hclients/hclients',
#             'objects': http.request.env['hclients.hclients'].search([]),
#         })

#     @http.route('/hclients/hclients/objects/<model("hclients.hclients"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hclients.object', {
#             'object': obj
#         })