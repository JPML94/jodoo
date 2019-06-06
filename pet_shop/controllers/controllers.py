# -*- coding: utf-8 -*-
from odoo import http

# class PetShop(http.Controller):
#     @http.route('/pet_shop/pet_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pet_shop/pet_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pet_shop.listing', {
#             'root': '/pet_shop/pet_shop',
#             'objects': http.request.env['pet_shop.pet_shop'].search([]),
#         })

#     @http.route('/pet_shop/pet_shop/objects/<model("pet_shop.pet_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pet_shop.object', {
#             'object': obj
#         })