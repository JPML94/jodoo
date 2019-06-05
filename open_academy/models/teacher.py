# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'open_academy.teacher'
    _description = 'This is the teacher for course in the Open Academy module.'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Teacher\'s age')
    vertical = fields.Char(string='The teacher\'s specialty field')
    name = fields.Char(compute='_compute_name', store=True)

    # @api.multi
    # def name_get(self):
    #     return [(rec.id, '{} {}'.format(rec.first_name, rec.last_name)) for rec in self]

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = '{} {}'.format(rec.first_name, rec.last_name)