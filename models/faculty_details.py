from odoo import models,api,fields,_

class FacultyDetails(models.Model):
    _name = 'faculty.details'
    _description = 'Faculty Details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name", required=1)
    last_name = fields.Char(string="Last Name", required=1)
    email = fields.Char(string="Email", widget='mail', required=1)
    mobile = fields.Char(string="Mobile", widget='phone', required=1)
    photo = fields.Binary(string="Photo")
    birth_date = fields.Date(string="Date of Birth")
    bank_name = fields.Char(string="Bank Name", required=1)
    account_holder_name = fields.Char(string="Bank Holder Name")
    account_no = fields.Char(string="Account No.", required=1)
    ifsc_code = fields.Char(string="IFSC Code", required=1)
    gst_no = fields.Char(string="GST No.")
    pan_no = fields.Char(string="Pan No.")
    qualification = fields.Char(string="Qualification")
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state_id = fields.Many2one("res.country.state", string='State')
    zip = fields.Char(string='Zip')
    country_id = fields.Many2one('res.country', string='Country')
    gender = fields.Selection([('male','Male'), ('female','Female')], string="Gender")
    tax_active = fields.Boolean(string="Tax Active")
    gst_number = fields.Char(string="GST Number")

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        self.name = str(self.first_name) + " " + str(self.last_name)


