# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'This is the course model of the module Open Academy.'
    _rec_name = 'title'

    title = fields.Char()
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ])
    