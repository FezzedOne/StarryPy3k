"""
StarryPy Chat Logger Plugin

Log all in-game chat messages to the logger.

Original authors: kharidiron
"""

from base_plugin import BasePlugin


class ChatLogger(BasePlugin):
    name = "chat_logger"

    def __init__(self):
        super().__init__()

    async def activate(self):
        await super().activate()

    async def on_chat_sent(self, data, connection):
        """
        Catch when someone sends any form of message or command and log it.

        :param data: The packet containing the message.
        :param connection: The connection from which the packet came.
        :return: Boolean; Always true.
        """
        message = data["parsed"]["message"]
        # FezzedOne: Log entry format is `<NICK> [<ORIGINAL NAME>] {<UUID>}: <MESSAGE>`.
        self.logger.info("{} [{}] {{{}}}: {}".format(connection.player.alias, connection.player.name,
                                                     connection.player.uuid, message))
        return True
