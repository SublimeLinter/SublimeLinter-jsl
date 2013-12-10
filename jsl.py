#
# jsl.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-jsl
# License: MIT
#

"""This module exports the JSL plugin linter class."""

from SublimeLinter.lint import Linter


class JSL(Linter):

    """Provides an interface to the jsl executable."""

    language = ('javascript', 'html')
    cmd = 'jsl -stdin -nologo -nosummary'
    regex = r'''(?xi)
        # First line is (lineno): type: error message
        ^\((?P<line>\d+)\):.*?(?:(?P<warning>warning)|(?P<error>error)):\s*(?P<message>.+)$\r?\n

        # Second line is the line of code
        ^.*$\r?\n

        # Third line is a caret pointing to the position of the error
        ^(?P<col>[^\^]*)\^$
    '''
    multiline = True
    defaults = {
        '-conf:': None
    }
    selectors = {
        'html': 'source.js.embedded.html'
    }
