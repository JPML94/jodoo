# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Owner(models.Model):
  _name = 'pet_shop.owner'
  _description = 'Owner model for Pet Shop module'

  name = fields.Char()
