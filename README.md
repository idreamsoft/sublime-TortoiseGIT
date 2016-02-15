Sublime-TortoiseGIT
=============
sublime-TortoiseGIT is a tiny and simple plugin for [Sublime Text](http://www.sublimetext.com) .
It's behavior is similar to [subclipse](http://subclipse.tigris.org/) in [Eclipse](http://www.eclipse.org/).
**It runs only on Windows and needs the TortoiseGIT and TortoiseGIT command line tools (TortoiseProc.exe).**

Usage
============
Install it using [Sublime Package Control](http://wbond.net/sublime_packages/package_control).
If TortoiseGIT is not installed at `C:\\Program Files\\TortoiseGIT\\bin\\TortoiseGitProc.exe`, specify the correct path
by setting property "tortoiseproc_path" in your TortoiseGIT.sublime-settings file.


The default key bindings are
- [alt+c] : commit current file.
- [alt+u] : update current file.
- [alt+r] : revert current file.

You can also call TortoiseGIT commands when right-clicking folders or files in the side bar.


IMPORTANT
==============

Do NOT edit the default Sublime-TortoiseGIT settings. Your changes will be lost
when Sublime-TortoiseGIT is updated. ALWAYS edit the user Sublime-TortoiseGIT settings
by selecting "Preferences->Package Settings->TortoiseGIT->Settings - User".
Note that individual settings you include in your user settings will **completely**
replace the corresponding default setting, so you must provide that setting in its entirety.

Settings
==============

If your TortoiseProc.exe path is not the default, please modify the path by selecting
"Preferences->Package Settings->TortoiseGIT->Settings - User" in the menu.

The default setting is:

    {
        // Auto close update dialog when no errors, conflicts and merges
        "autoCloseUpdateDialog": false,
        "tortoiseproc_path": "C:\\Program Files\\TortoiseGIT\\bin\\TortoiseProc.exe"
    }
