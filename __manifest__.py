{
    'name': 'Faculty',
    'version': '1.0.0',
    'summary': 'faculty expenses',
    'description': """
        this module for faculty class hours records submission.
    """,
    'author': 'Murshid',
    'website': 'https://www.yourwebsite.com',
    'category': 'Specific Category',
    'license': 'LGPL-3',
    'depends': [
        'base',  # List of module dependencies
        'mail', 'web', 'hr', 'openeducat_core','logic_base_17'
        # Add other module dependencies here
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/faculty_details.xml',# Access rights
        'views/class_record.xml',
        'views/user.xml',
        'views/subject_stnd_hr.xml',
        'views/faculty_rates.xml',
        'views/rejection.xml',
        # 'views/clarification.xml'

    ],
    'assets': {
        'web.assets_backend': [

            '/faculty_17/static/src/css/style.css',

        ],
    },

    'installable': True,  # Whether the module can be installed
    'application': True,  # Set to True if it's an application module
    'auto_install': False,  # Automatically install if dependencies are met

}
