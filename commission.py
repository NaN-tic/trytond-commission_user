# This file is part commission_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields

__all__ = ['AgentUser']


class AgentUser(ModelSQL):
    'Agent User'
    __name__ = 'agent.user'

    agent = fields.Many2One('commission.agent', 'Agent', ondelete='CASCADE',
        select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        required=True)
