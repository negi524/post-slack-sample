import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    logger.info("hello, world.")
    print(mycredential.SLACK_TOKEN)
    print(mycredential.SLACK_CHANNEL_ID)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()
