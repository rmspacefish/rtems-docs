import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS Source Builder Manual"

latex_documents = [
	('index', 'rsb.tex', u'RTEMS Source Builder', u'RTEMS Documentation Project', 'manual'),
]