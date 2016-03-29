# This file is part commission_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['User']


class User:
    __metaclass__ = PoolMeta
    __name__ = "res.user"
    agents = fields.Many2Many('agent.user', 'user', 'agent', 'Agents')
    agent = fields.Many2One('commission.agent', 'Agent', domain=[
            ('id', 'in', Eval('agents', [])),
            ], depends=['agents'])

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
                'agent',
                'agents',
                ])
        cls._context_fields.insert(0, 'agent')
        cls._context_fields.insert(0, 'agents')

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.agent:
            status += ' - %s' % (self.agent.rec_name)
        return status
