# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
#                           Copyright (c) 2014
#       Data Intensive Applications and Systems laboratory (DIAS)
#                École Polytechnique Fédérale de Lausanne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import json
import os
import sys

if not hasattr(sys, 'argv'):    # Required by the testcases
    sys.argv = ['python']

from multicorn import ForeignDataWrapper
#from multicorn.utils import log_to_postgres
from pyrawcore.core import get_option, load


resource_path = get_option('sql', 'resource_path')
if not resource_path:
    import tempfile
    resource_path = os.path.realpath(tempfile.gettempdir())


class RawForeignDataWrapper(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(RawForeignDataWrapper, self).__init__(options, columns)
        with open(os.path.join(resource_path, options['resource_id']), 'r') as f:
            payload = json.load(f)
        self.table = load(payload)
        #log_to_postgres(str(options['path']))

    def execute(self, quals, columns):
        for row in self.table:
            yield row
