# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Asset(models.Model):
  _name = 'pet_shop.asset'
  _description = 'Asset model for Pet Shop module'

  name = fields.Char()
