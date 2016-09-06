import sublime
import sublime_plugin
import os
import os.path
import subprocess

class TortoiseGitCommand(sublime_plugin.WindowCommand):
    def run(self, cmd, paths=None, isHung=False):
        dir = self.get_path(paths)

        if not dir:
            return

        settings = self.get_setting()
        tortoiseproc_path = settings.get('tortoiseproc_path')

        if not os.path.isfile(tortoiseproc_path):
            sublime.error_message('can\'t find TortoiseProc.exe,'
                ' please config setting file' '\n   --sublime-TortoiseGIT')
            raise

        proce = subprocess.Popen('"' + tortoiseproc_path + '"' +
            ' /command:' + cmd + ' /path:"%s"' % dir , stdout=subprocess.PIPE)

        # This is required, cause of ST must wait TortoiseGIT update then revert
        # the file. Otherwise the file reverting occur before GIT update, if the
        # file changed the file content in ST is older.
        if isHung:
            proce.communicate()

    def get_path(self, paths):
        path = None
        if paths:
            path = '*'.join(paths)
        else:
            view = sublime.active_window().active_view()
            path = view.file_name() if view else None

        return path

    def get_setting(self):
        return sublime.load_settings('TortoiseGIT.sublime-settings')


class MutatingTortoiseGitCommand(TortoiseGitCommand):
    def run(self, cmd, paths=None):
        TortoiseGitCommand.run(self, cmd, paths, True)

        self.view = sublime.active_window().active_view()
        row, col = self.view.rowcol(self.view.sel()[0].begin())
        self.lastLine = str(row + 1);
        sublime.set_timeout(self.revert, 100)

    def revert(self):
        self.view.run_command('revert')
        sublime.set_timeout(self.revertPoint, 600)

    def revertPoint(self):
        self.view.window().run_command('goto_line', {'line':self.lastLine})


class GitPullCommand(MutatingTortoiseGitCommand):
    def run(self, paths=None):
        settings = self.get_setting()
        closeonend = ('3' if True == settings.get('autoCloseUpdateDialog')
            else '0')
        MutatingTortoiseGitCommand.run(self, 'pull /closeonend:' + closeonend,
            paths)

class GitPushCommand(MutatingTortoiseGitCommand):
    def run(self, paths=None):
        settings = self.get_setting()
        closeonend = ('3' if True == settings.get('autoCloseUpdateDialog')
            else '0')
        MutatingTortoiseGitCommand.run(self, 'push /closeonend:' + closeonend,
            paths)

class GitSyncCommand(MutatingTortoiseGitCommand):
    def run(self, paths=None):
        settings = self.get_setting()
        closeonend = ('3' if True == settings.get('autoCloseUpdateDialog')
            else '0')
        MutatingTortoiseGitCommand.run(self, 'sync  /closeonend:' + closeonend,
            paths)
            
class GitCommitCommand(TortoiseGitCommand):
    def run(self, paths=None):
        settings = self.get_setting()
        closeonend = ('3' if True == settings.get('autoCloseCommitDialog')
            else '0')
        TortoiseGitCommand.run(self, 'commit /closeonend:' + closeonend, paths)


class GitRevertCommand(MutatingTortoiseGitCommand):
    def run(self, paths=None):
        MutatingTortoiseGitCommand.run(self, 'revert', paths)


class GitLogCommand(TortoiseGitCommand):
    def run(self, paths=None):
        TortoiseGitCommand.run(self, 'log', paths)


class GitSwitchCommand(TortoiseGitCommand):
    def run(self, paths=None):
        TortoiseGitCommand.run(self, 'switch', paths)


class GitDiffCommand(TortoiseGitCommand):
    def run(self, paths=None):
        TortoiseGitCommand.run(self, 'diff', paths)


class GitBlameCommand(TortoiseGitCommand):
    def run(self, paths=None):
        view = sublime.active_window().active_view()
        row = view.rowcol(view.sel()[0].begin())[0] + 1

        TortoiseGitCommand.run(self, 'blame /line:' + str(row), paths)

    def is_visible(self, paths=None):
        file = self.get_path(paths)
        return os.path.isfile(file) if file else False


class GitAddCommand(TortoiseGitCommand):
    def run(self, paths=None):
        TortoiseGitCommand.run(self, 'add', paths)
