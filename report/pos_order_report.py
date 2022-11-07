# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import api, models, _


class PosOrder(models.AbstractModel):
    _name = 'report.pos_report_generator.pos_order_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if self.env.context.get('pos_order_report'):

            if data.get('report_data'):
                shop_id = data['report_data']['orders'].get('shop_id')
                data.update({'report_main_line_data': data.get('report_data')['report_lines'],
                             'Filters': data.get('report_data')['filters'],
                             'company': self.env.company,
                             'shop_name': shop_id or 'ALL'
                             })
            return data
