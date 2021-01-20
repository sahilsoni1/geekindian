import argparse
import logging
# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
parser = argparse.ArgumentParser(description='Parsing logging log')
parser.add_argument('log', type=str, 
                    help='Enter the logging level.Eg info')
loglevel = parser.parse_args()
numeric_level = getattr(logging, loglevel.log.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')