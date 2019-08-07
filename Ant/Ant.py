import sublime, sublime_plugin

class AntCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		self.view.run_command('sec',{"i":1})
class SecCommand(sublime_plugin.TextCommand):
	def run(self,edit,i):
		if i<=107:
			aa = sublime.load_settings('test.sublime-settings')
			bb = aa.get(str(i))
			region = sublime.Region(0, self.view.size())
			self.view.replace(edit, region, bb)
			sublime.set_timeout(lambda: self.view.run_command('sec',{"i":i+1}),30)
		else:
			self.view.run_command('sec',{"i":1})
