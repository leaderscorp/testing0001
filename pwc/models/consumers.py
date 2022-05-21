from odoo import api, models, fields, _


class comsumers(models.Model):
    _name = 'consumers'
    _description = 'Consumers Info'
    _rec_name= 'record_name'

    def name_get(self):
        res = []
        for ddt in self:
            name=ddt.s_no or ""+' '+ddt.name or "" 
            res.append((ddt.id, ("%s") % (name)))
        return res
        
    record_name=fields.Char(compute="get_Rec_name",string="Name")

    s_no = fields.Char("Sr. No")
    name = fields.Char('Consumer Name')
    ibc_name = fields.Char('Name of IBC:')
    consumer_no = fields.Char('Consumer number as per KE MIS:')
    consumer_account_no = fields.Char('Contract account as per KE MIS: ')
    contract_account_no = fields.Char('Contract account as per KE MIS:')
    meter_number = fields.Char('Meter number as per KE MIS: ')
    surveyor_name = fields.Char('Surveyor Representative Name:')
    ibc_surveyor_name = fields.Char('IBC Field Surveyor Name:')
    
    
    @api.depends('s_no','name')
    def get_Rec_name(self):
        for rec in self:
            name=rec.s_no or ""+' '+rec.name or "" 
            rec.record_name=name
        
