import sys
import re
import settings

def get_path(path):
	try:
		with open(path, 'r') as fd:
			template = fd.read()
		return template
	except IOError:
		print("Error opening %s" % path)
		return None

def write_in_file(path, data):
	try:
		with open(path, 'w') as fd:
			fd.write(data)
	except IOError:
		print("Error writing %s" % path)

def run(path):
	template = get_path(path)
	if template:
		data_dict = vars(settings)
		try:
			filled_template = template.format(**data_dict)
			write_in_file("%s%s" % (path[0:-9], ".html"), filled_template)
		except KeyError:
			print("Error, cannot fill the template %s" % path)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		if re.search('\.template$', sys.argv[1]) is not None:
			run(sys.argv[1])
		else:
			print("Wrong extension - need .template")
