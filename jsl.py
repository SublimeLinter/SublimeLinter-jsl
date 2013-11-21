#
# gjslint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-gjslint
# License: MIT
#

import re

from SublimeLinter.lint import Linter


class JSL(Linter):
    language = 'javascript'
    cmd = ('jsl', '-stdin', '-nologo', '-nosummary')
    regex = r'''
        # First line is (lineno): type: error message
        ^\((?P<line>\d+)\):.*?(?P<type>warning|error):\s*(?P<error>.+)$\r?\n

        # Second line is the line of code
        ^.*$\r?\n

        # Third line is a caret pointing to the position of the error
        ^(?P<col>[^\^]*)\^$
    '''
    re_flags = re.VERBOSE | re.IGNORECASE
    multiline = True
    defaults = {
        '-conf:': None
    }


class EmbeddedJSL(JSL):
    language = 'html'
    selector = 'source.js.embedded.html'
