from telegram import Update, ParseMode
from telegram.ext import ContextTypes

from decorators import is_main_user


def help_command(update: Update, context: ContextTypes) -> None:
    update.effective_chat.send_message(
        "<b>Я — бот, работающий на Chat GPT-3</b>\n\n"
        "Исходные коды бота: <a href='https://github.com/oleonov/chatgpt_telegram_bot'>chatgpt_telegram_bot</a>\n\n"
        "Если переслать мне собщение из чата, в котором я есть и написать название чата, то я смогу ответить на него.",
        parse_mode=ParseMode.HTML
    )


@is_main_user
def cancel_command(update: Update, context: ContextTypes) -> None:
    clear_forwarded_message(context)
    update.effective_chat.send_message("Действие отменено")


def save_forwarded_message(update: Update, context: ContextTypes) -> bool:
    if update.message.forward_from is None:
        return False
    context.user_data["reply_user_id"] = update.message.forward_from.id
    context.user_data["mention_markdown"] = update.message.forward_from.mention_markdown()
    context.user_data["text"] = update.message.text
    return True


def clear_forwarded_message(context: ContextTypes):
    context.user_data["reply_user_id"] = ""
    context.user_data["mention_markdown"] = ""
    context.user_data["text"] = ""
