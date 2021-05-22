from odoo import fields, models, api

class AcademySyllabus(models.Model):
    _name = 'academy.course.syllabus'
    _description = 'Course Syllabus'
    name = fields.Char('Title',required=True)



class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'
    name = fields.Char('Title',index=True,required=True)
