from richclass import RichPath, RichPathType
import logging
import logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
log_buffer_file = logging.getLogger("buffer file")

WINDOWS_USERNAME = "Family"

dir_documents = RichPath(
    RichPathType.DIRECTORY,
    path_str = "C:/Users/" + WINDOWS_USERNAME,
    req= True,
    logger= log_buffer_file
)

print(dir_documents)


