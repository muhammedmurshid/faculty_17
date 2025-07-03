from odoo import fields,models,api,_

class FacultyRates(models.Model):
    _name = 'faculty.rates'
    _description = "Faculty Rate"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "display_name"

    faculty_id = fields.Many2one('faculty.details', string="Faculty", required=1, tracking=1)
    course_id = fields.Many2one('op.course', string="Course", required=1,tracking=1)
    subject_id = fields.Many2one('op.subject', string="Subject", required=1, tracking=1)
    salary_per_hour = fields.Float(string="Salary per Hr.", tracking=1)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id)

    def _compute_display_name(self):
        for i in self:
            if i.faculty_id:
                i.display_name = i.faculty_id.name + " "  + 'Rates'
            else:
                i.display_name = 'Faculty Rates'
