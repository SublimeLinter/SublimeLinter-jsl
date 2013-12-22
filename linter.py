#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the JSL plugin linter class."""

from SublimeLinter.lint import Linter, util


class JSL(Linter):

    """Provides an interface to the jsl executable."""

    syntax = ('javascript', 'html')
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
    error_stream = util.STREAM_STDOUT
    defaults = {
        '-conf:': None
    }
    selectors = {
        'html': 'source.js.embedded.html'
    }
