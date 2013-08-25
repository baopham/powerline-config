# vim:fileencoding=utf-8:noet

import os
import re


def undotree(matcher_info):
	name = matcher_info['buffer'].name
	return name and re.match(r'undotree_\d+', os.path.basename(name))


def undotree_preview(matcher_info):
	name = matcher_info['buffer'].name
	return name and re.match(r'diffpanel_\d+', os.path.basename(name))
