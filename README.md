SublimeLinter-jsl
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jsl.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jsl)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [jsl (JavaScript Lint)](http://javascriptlint.com/index.htm).
It will be used with files that have the "JavaScript" syntax, or within `<script>` tags in HTML files.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `jsl 0.3.0` is installed on your system.
To install `jsl`, download and install the appropriate package from the [JavaScript Lint download page](http://javascriptlint.com/download.htm).

Please make sure that the path to `jsl` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

You can configure `jsl` options in the way you would from the command line, with `jsl.conf` files. For more information, see the [jsl docs](http://www.javascriptlint.com/docs/). 

You may provide a custom config file by setting the linter's `"args"` setting to `["-conf", "/path/to/file"]`. To create a `jsl` config file, type the following in a terminal:

```
jsl -help:conf > jsl.conf
```
