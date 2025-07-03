from odoo import fields, models
from datetime import date, datetime, time

class RejectReason(models.TransientModel):
    _name = 'reject.reason'
    _description = "Reject Wizard"

    record_id = fields.Many2one('faculty.records', string="Record")
    rejected_reason = fields.Text(string="Rejected Reason", required=1)

    def reject(self):
        for rec in self:
            rec.record_id.state = 'rejected'
            rec.record_id.rejected_person = self.env.user
            rec.record_id.rejected_date = date.today()
            rec.record_id.rejected_reason = rec.rejected_reason
