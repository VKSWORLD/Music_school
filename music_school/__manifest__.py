
{
    "name": "Music School Institute",
    "version": "16.0",
    "summary": "Music School Management module. ",
    'sequence': -100,
    "description": """music school""",
    "website": "https://www.odoo.com",
    "depends": ["base", "stock", "sale", "calendar", "event", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/class_type_views.xml",
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
        "views/hr_employee_views.xml",
        "views/class_lesson_views.xml",
        "views/students_attendance_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}
