# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'This is the course model of the module Open Academy.'

    name = fields.Char(string='Title', required=True)
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ], string='Difficulty')

    @api.onchange('level')
    def _onchange_level(self):
        raise Exception(str(self.env.context))
