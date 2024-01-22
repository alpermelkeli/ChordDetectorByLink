import sys
import autochord

inputFile = sys.argv[1]
autochord.recognize(inputFile, lab_fn=inputFile[:-4]+".lab")

