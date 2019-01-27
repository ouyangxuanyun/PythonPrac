import logging
import logging.config

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename="app.log"
# )

logging.config.fileConfig('logging.conf')

# logging.debug('AAAAAAAAA')
# logging.info('AAAAAAAAAAAA')
# logging.warning('AAAAAAAAAA')
# logging.error('AAAAAAAAA')
# logging.critical('AAAAAAAAA')


console_logger = logging.getLogger()