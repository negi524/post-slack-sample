import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from slack_sdk import WebClient
import textwrap

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    # Slack WebClientの初期化
    slack_client = WebClient(token=mycredential.SLACK_TOKEN)

    # 送信するメッセージ
    message = """
    Pythonのコードからメッセージを投稿しています
    改行しています
    """
    # ヒアドキュメントのインデントを除外する
    deleted_indent_message = textwrap.dedent(message)
    try:
        response = slack_client.chat_postMessage(
            channel=mycredential.SLACK_CHANNEL_ID, text=deleted_indent_message
        )
        logger.info(f"Slackにメッセージが投稿されました\t{deleted_indent_message}")
        logger.info(response)
    except Exception as e:
        logger.error(f"Slackへのメッセージ投稿中にエラーが発生しました\t{e}")


if __name__ == "__main__":
    main()
