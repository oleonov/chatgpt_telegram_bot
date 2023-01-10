import time

import settings


class MessagesCache:
    class UserMessage:
        def __init__(self, user_id: int, message: str, date: float):
            self.user_id = user_id
            self.message = message
            self.date = date

    def __init__(self):
        self.messages = dict()

    def add(self, user_id: int, message: str, is_bot_answer: bool):
        self.messages.setdefault(user_id, []).append(self.UserMessage(-1 if is_bot_answer else user_id, message, time.time()))
        self.__shrink_array(user_id, settings.store_last_messages)
        self.__remove_old_messages(user_id,  time.time() - settings.message_cache_minutes * 60)

    def __shrink_array(self, user_id: int, max_size: int):
        self.messages[user_id] = self.messages[user_id][-max_size:]

    def __remove_old_messages(self, user_id: int, delete_before_time: float):
        self.messages[user_id] = [item for item in self.messages[user_id] if item.date > delete_before_time]

    def get_formatted(self, user_id: int):
        if self.messages.get(user_id) is None:
            return ""
        formatted_message = ""
        for message in self.messages.get(user_id):
            formatted_message += f'AI: {message.message}\n' if message.user_id == -1 else f'Human: {message.message}\n'
        return formatted_message
