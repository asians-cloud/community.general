# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Komang Suryadana <komang.surya@asians.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


def ord_filter(char):
    '''Convert a char to ascii code.

    Example: ``'b' | community.general.ord`` results in ``98``
    '''
    return ord(char)


class FilterModule(object):
    '''Ansible jinja2 filters'''

    def filters(self):
        return {
            'ord': ord_filter,
        }
