import logging
logging.basicConfig(format='%(levelname)s:line_no %(lineno)d:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
 	