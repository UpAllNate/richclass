from richclass import RichPath, RichPathType
import logging
import logging.config

# Set up and configure the logger for this program
LOG_FILE_NAME = "uppyrclasstest.log"

with open('logging.conf', 'r') as f:
    with open('_logging.conf', 'w') as _f:
        for line in f:
            if "log_name.log" in line:
                line = line.replace('log_name.log', LOG_FILE_NAME)

            _f.write(line)

logging.config.fileConfig('_logging.conf', disable_existing_loggers=False)
os.remove('_logging.conf')

logger = logging.getLogger("root")

WINDOWS_USERNAME = "Family"

dir_documents = RichPath(
    RichPathType.DIRECTORY,
    path_str = "C:/Users/" + WINDOWS_USERNAME,
    req= True,
    logger= log_buffer_file
)

print(dir_documents)


