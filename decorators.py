from telegram import Update
from telegram.ext import CallbackContext

from settings import main_users_id


def is_main_user(callback):
    def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        if update.message.from_user.id not in main_users_id:
            update.effective_chat.send_message("❌ Для этого действия нужно быть администратором бота")
            return None
        return callback(update, context, *args, **kwargs)

    return wrapper
