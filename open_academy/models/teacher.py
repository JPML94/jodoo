# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'open_academy.teacher'
    _description = 'This is the teacher for course in the Open Academy module.'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Teacher\'s age')
    vertical = fields.Char(string='The teacher\'s specialty field')

    @api.multi
    def name_get(self):
        return [(rec.id, '{} {}'.format(rec.first_name, last_name)) for rec in self]