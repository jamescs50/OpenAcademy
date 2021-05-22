from odoo import fields, models, api
import datetime

class AcademySession(models.Model):
    _name = 'academy.session'
    _description = 'Academy Session'

    name = fields.Char('Description',index=True,required=True)
    start_date = fields.DateTime('Start Date / Time',required=true)
    priority = fields.Integer('Priority')
