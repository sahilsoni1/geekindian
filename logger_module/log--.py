# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('string', metavar='N', type=str, 
                    help=' add modes')


# parser.add_argument('--sum', dest='accumulate', action='store_const',
                    # const=sum, default=max,
                    # help='sum the integers (default: find the max)')

args = parser.parse_args()


import logging
loglevel =args.string
numeric_level = getattr(logging, loglevel.upper(), None)
print(numeric_level)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(filename='example.log', filemode='w',level=numeric_level)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')