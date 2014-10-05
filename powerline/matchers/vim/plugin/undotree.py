# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

import os
import re

from powerline.bindings.vim import buffer_name


def undotree(matcher_info):
	name = matcher_info['buffer'].name
	return name and re.match(r'undotree_\d+', os.path.basename(name))


def undotree_preview(matcher_info):
	name = matcher_info['buffer'].name
	return name and re.match(r'diffpanel_\d+', os.path.basename(name))