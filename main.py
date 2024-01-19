import autochord

import sys


inputFile = sys.argv[1]

autochord.recognize(inputFile, lab_fn=inputFile+".lab")