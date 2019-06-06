# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Pet(models.Model):
  _name = 'pet_shop.pet'
  _description = 'Pet model for Pet Shop module'

  name = fields.Char()
