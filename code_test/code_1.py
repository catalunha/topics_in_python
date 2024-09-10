import logging

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


print("Oi")
logger.debug("msg debug")
logger.info("msg info")
logger.warning("msg warning")
logger.error("msg error")
logger.critical("msg critical")

print("fui")
