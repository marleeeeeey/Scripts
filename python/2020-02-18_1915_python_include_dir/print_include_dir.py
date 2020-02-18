from sysconfig import get_paths
from pprint import pprint
import sys

# way 01
info = get_paths()  # a dictionary of key-paths
pprint(info)

# way 02
pprint(sys.path)