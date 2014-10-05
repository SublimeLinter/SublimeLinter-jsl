SublimeLinter-jsl
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jsl.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jsl)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [jsl (JavaScript Lint)](http://javascriptlint.com/index.htm). It will be used with files that have the “JavaScript” syntax, or within `<script>` tags in HTML files.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `jsl 0.3.0` is installed on your system. To install `jsl`, download and install the appropriate package from the [JavaScript Lint download page](http://javascriptlint.com/download.htm).

**NOTE:** Do **not** use the latest development version from svn. This plugin is only compatible with one of the 0.3.0 releases.

### Linter configuration
In order for `jsl` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `jsl` is installed and configured, you can proceed to install the SublimeLinter-jsl plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `jsl`. Among the entries you should see `SublimeLinter-jsl`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `jsl` options in the way you would from the command line, with `jsl.conf` files. For more information, see the [jsl docs](http://www.javascriptlint.com/docs/). The linter plugin does this by searching for a `jsl.conf` file itself in the linted file's working directory, its parent directories, and the user's home directory (`~`).

You may provide a custom config file by setting the linter's `"args"` setting to `["-conf", "/path/to/file"]`. To create a `jsl` config file, type the following in a terminal:

```
jsl -help:conf > jsl.conf
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
