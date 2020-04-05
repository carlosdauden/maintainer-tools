# Copyright 2020 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class Name(models.AbstractModel):
    report_name = 'module.name_report'
    _name = 'report.%s' % report_name
    _description = "Report Name"

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name(self.report_name)
        docargs = {
            "doc_ids": self._ids,
            "doc_model": report.model,
            "docs": self,
        }
        return report_obj.render(self.report_name, docargs)
