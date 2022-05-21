from odoo import api, models, fields, _


class Comsumersurvey(models.Model):
    _name = 'consumers.survey'
    _description = 'Consumers Survey'

    sr_no = fields.Many2one("consumers", string="S.No")
    name = fields.Char("Name")
    date_survey = fields.Datetime('Date of survey:')
    consumer_ke_mis_id = fields.Char('Consumer ke MIS Id', related='sr_no.consumer_no')
    name_ibc = fields.Char('Name of IBC', related='sr_no.ibc_name')
    consumer_no = fields.Char('Consumer number as per KE MIS:', related='sr_no.consumer_no')
    consumer_name = fields.Char('Consumer Name:', related='sr_no.name')
    consumer_account_no = fields.Char('Contract account as per KE MIS: ',
                                      related='sr_no.consumer_account_no')
    contract_account_no = fields.Char('Contract account as per KE MIS: ',
                                      related='sr_no.contract_account_no')
    meter_number = fields.Char('Meter number as per KE MIS: ', related='sr_no.meter_number')
    surveyor_name = fields.Char('Surveyor Representative Name:', related='sr_no.surveyor_name')
    ibc_surveyor_name = fields.Char('IBC Field Surveyor Name:', related='sr_no.ibc_surveyor_name')

    """check group of A"""
    a_merter_check = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="1 Meter present")
    a_merter_description = fields.Char("Meter Description")
    a_merter_image_1920 = fields.Image("Meter Image", max_width=1920, max_height=1920)

    a_elect_met = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="2 Electricity in use through meter")
    a_elect_met_description = fields.Char("Meter Description")
    a_elect_met_image_1920 = fields.Image("Meter Image", max_width=1920, max_height=1920)

    a_hook_connection = fields.Selection([('yes', 'Yes'), ('no', 'No')], default = 'no', string="3 Hook connection/connection from nearby premises")

    a_meter_phy = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="4 Meter physically found disconnected")
    a_meter_phy_description = fields.Char("Meter physically Description")
    a_meter_phy_image_1920 = fields.Image("Meter physically Image", max_width=1920, max_height=1920)


    a_site_survay = fields.Selection([('yes', 'Yes'), ('no', 'No')],  string="6 Site survey indicates use of electricity through meter")
    a_site_survay_description = fields.Char("Site survey Description")
    a_site_survay_image_1920 = fields.Image("Site survey Image", max_width=1920, max_height=1920)

    a_meter_no_found = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                     string="7 Meter number found")
    a_meter_no_found_description = fields.Char("Meter number Description")
    a_meter_no_found_image_1920 = fields.Image("Meter number Image", max_width=1920, max_height=1920)

    a_consumer_no_found = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                        string="8 Meter number found")



    """End group A"""

    """check group of B"""


    b_arial_bundle_cables = fields.Selection([('yes', 'Yes'), ('no', 'No')],  string="1 Aerial Bundle Cables (ABC) installed in area")

    """End group B"""

    """check group of C"""

    c_hook_connection  = fields.Selection([('yes', 'Yes'), ('no', 'No')], default='yes',
                                             string="1 Hook Connection")
    c_meter = fields.Selection([('yes', 'Yes'), ('no', 'No')], default='yes',
                                         string="2 Meter")
    c_elevation = fields.Selection([('yes', 'Yes'), ('no', 'No')], default='yes',
                                         string="3 Elevation, overall premises, boundaries, gate etc.")
    c_evidence = fields.Selection([('yes', 'Yes'), ('no', 'No')], default='yes',
                                   string="4  Evidenc of Disconnection")
    c_evidence_arieal = fields.Selection([('yes', 'Yes'), ('no', 'No')], default='yes',
                                   string="5 Evidence of Aerial Bundle Cables(ABC) installation on premises")

    """End group C"""

    """check group of D"""

    d_person_ceck = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                             string="1 Name Of Person")
    d_name = fields.Char('Person Name')
    d_customer_willling = fields.Selection([('yes', 'Yes'), ('no', 'No')], default = 'no', string="2 Customer willing to opt for rebate offered by KE")
    d_not_willling_talk = fields.Selection([('yes', 'Yes'), ('no', 'No')], default = 'yes', string="3 Consumer not willing to talk    ")

    images_ids = fields.One2many(
        comodel_name='surveys.images',
        inverse_name='survey_id',
        string='Images',
        required=False)
    name_of_person =fields.Char('Name of Person')


    """End group D"""

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('consumers.survey')
        result = super(Comsumersurvey, self).create(vals)
        return result


class surveyImages(models.Model):
    _name = 'surveys.images'
    _description = 'Survey Images'

    survey_id = fields.Many2one('consumers.survey')
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
