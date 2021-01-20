
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-e","--echo" , help ="show the output")
args = parser.parse_args()

if args.echo:
	print("output is %s"%str(args.echo))
