# Singleton para manejar mensajes de error
class MessageHandler:
    _instance = None

    def __new__(message):
        if message._instance is None:
            message._instance = super(MessageHandler, message).__new__(message)
            message._instance.messages = []  # Lista para almacenar mensajes
        return message._instance

    def add_message(self, message):
        self.messages.append(message)  # Agregar un mensaje a la lista

    def get_messages(self):
        return self.messages  