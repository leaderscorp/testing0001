# -*- coding: utf-8 -*-
{
    'name': 'PWC',
    'version': '1.0',
    'depends': ['base'],
    'category': 'sale',
    'summary': 'PWC data entery form',
    'description': """PWC data entery form""",
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/cusomer.xml',
        'views/survey.xml',
        # 'report/pwc_report.xml',


    ],

    'installable': True,
    'application': True,
}
