import sys
import getopt
import typing

class Application:
	name = 'My First CLI'
	version  = '1.0'
	commands = []

	def __init__(self, name, version):
		self.name = name
		self.version = version

	def add(self, command):
		self.commands.append(command)

	def run(self):
		if len(sys.argv) == 1:
			welcome_message = self.name + ' ' + self.version
			welcome_message += '\n-- Info table here --'
			return print(welcome_message)
		else:
			self.process(sys.argv)

	def process(self, argv):
		try:
			opts, args = getopt.getopt(argv[1:], 'v')
		except getopt.GetoptError as err:
			print(err)
			sys.exit(2)
		print(opts)
		print(args)
