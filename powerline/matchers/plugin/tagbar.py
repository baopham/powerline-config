# vim:fileencoding=utf-8:noet

import os


def tagbar(matcher_info):
	name = matcher_info['buffer'].name
	return name and os.path.basename(name) == '__Tagbar__'
