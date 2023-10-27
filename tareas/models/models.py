# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
     _name = 'tareas.task'
     _description = 'tareas.task'

     nombre = fields.Char(required=True, help="Introduce el nombre")
     descripcion = fields.Text()
     horas = fields.Integer()
     fecha_creacion = fields.Date()
     fecha_comienzo = fields.Datetime()
     fecha_fin = fields.Datetime()
     pausada = fields.Boolean()
     # sprint = fields.Many2one("tareas.sprint")
     # tecno = fields.Many2many("tareas.tecnologia")
    
class sprint(models.Model):
     _name = 'tareas.sprint'
     _description = 'tareas.sprint'

     nombre = fields.Char()
     descripcion = fields.Text()
     fecha_creacion = fields.Datetime()
     fecha_fin = fields.Datetime()
     # sprint = fields.One2many("tareas.task")


class tecnologias(models.Model):
     _name = 'tareas.tecnologia'
     _description = 'tareas.tecnologia'

     nombre = fields.Char()
     imagen = fields.binary("Image", help="Select image here"),

    


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
