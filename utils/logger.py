from loguru import logger

def configure_logger():
    logger.add(
        "research.log",
        format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{message}",
        rotation="10 MB",
        retention="30 days",
        level="INFO"

    )
    return logger

log=configure_logger()