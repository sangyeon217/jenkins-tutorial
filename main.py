import logging
import logging_config

if __name__ == '__main__':
    logging_config.init()
    logger = logging.getLogger()
    logger.error(msg='Jenkins Console Output 에 로그 스트림 출력이 남는지 확인')
    logger.debug(msg='DEBUG 로그 메세지')
    logger.info(msg='INFO 로그 메세지')
    logger.warning(msg='WARNING 로그 메세지')
