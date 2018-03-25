from SublimeLinter.lint import Linter, util


class JSL(Linter):
    cmd = 'jsl -stdin -nologo -nosummary'
    config_file = ('-conf', 'jsl.conf', '~')
    regex = r'''(?xi)
        # First line is (lineno): type: error message
        ^\((?P<line>\d+)\):.*?(?:(?P<warning>warning)|(?P<error>error)):\s*(?P<message>.+)$\r?\n

        # Second line is the line of code
        ^.*$\r?\n

        # Third line is a caret pointing to the position of the error
        ^(?P<col>[^\^]*)\^
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    defaults = {
        'selector': 'source.js - meta.attribute-with-value'
    }
