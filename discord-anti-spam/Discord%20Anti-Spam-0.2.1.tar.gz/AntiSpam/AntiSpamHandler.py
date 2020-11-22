"""
The MIT License (MIT)

Copyright (c) 2020 Skelmis

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import logging

import discord
from discord.ext import commands

from AntiSpam import Guild
from AntiSpam.Exceptions import (
    DuplicateObject,
    BaseASHException,
    MissingGuildPermissions,
)
from AntiSpam.static import Static

"""
The overall handler & entry point from any discord bot,
this is responsible for handling interaction with Guilds etc
"""


# TODO Check on attempted kick/ban that the bot actually has perms


class AntiSpamHandler:
    """
    The overall handler for the DPY Anti-spam package

    DEFAULTS:
        warn_threshold: 3
            This is the amount of duplicates that result in a warning within the message_interval

        kick_threshold: 2
            This is the amount of warns required before a kick is the next punishment

        ban_threshold: 2
            This is the amount of kicks required before a ban is the next punishment

        message_interval: 30000ms (30 Seconds)
            Amount of time a message is kept before being discarded. Essentially the amount of time (In milliseconds) a message can count towards spam

        warn_message: "Hey $MENTIONUSER, please stop spamming/sending duplicate messages."
            The message to be sent upon warn_threshold being reached

        kick_message: "$USERNAME was kicked for spamming/sending duplicate messages."
            The message to be sent up kick_threshold being reached

        ban_message: "$USERNAME was banned for spamming/sending duplicate messages."
            The message to be sent up ban_threshold being reached

        message_duplicate_count: 5
            The amount of duplicate messages needed within message_interval to trigger a punishment

        message_duplicate_accuracy: 90
            How 'close' messages need to be to be registered as duplicates (Out of 100)

        ignore_perms: [8]
            The perms (ID Form), that bypass anti-spam

            *Not Implemented*

        ignore_users: []
            The users (ID Form), that bypass anti-spam

        ignore_channels: []
            Channels (ID Form), that bypass anti-spam

        ignore_roles: []
            The roles (ID Form), that bypass anti-spam

        ignore_guilds: []
            Guilds (ID Form), that bypass anti-spam

        ignore_bots: True
            Should bots bypass anti-spam? (True|False)
    """

    # TODO Add options for group spamming, rather then just per user.
    #      This could possibly be implemented at a Guild() level
    # TODO Add the ability to lockdown channels in certain situations
    # TODO Add bypass's for modes, so bypass warn mode. (Can be avoided by simply setting warn higher then kick)
    #      and that's how it will be implemented internally most likely
    # TODO Add the ability to toggle dm messages for log messages (To affected users)

    def __init__(
        self,
        bot: commands.Bot,
        verbose_level=0,
        *,
        warn_threshold=None,
        kick_threshold=None,
        ban_threshold=None,
        message_interval=None,
        warn_message=None,
        kick_message=None,
        ban_message=None,
        message_duplicate_count=None,
        message_duplicate_accuracy=None,
        ignore_perms=None,
        ignore_users=None,
        ignore_channels=None,
        ignore_roles=None,
        ignore_guilds=None,
        ignore_bots=None,
    ):
        """
        This is the first initialization of the entire spam handler,
        this is also where the initial options are set

        Parameters
        ----------
        bot : commands.Bot
            The commands.Bot instance
        warn_threshold : int, optional
            This is the amount of messages in a row that result in a warning within the message_interval
        kick_threshold : int, optional
            The amount of 'warns' before a kick occurs
        ban_threshold : int, optional
            The amount of 'kicks' that occur before a ban occurs
        message_interval : int, optional
            Amount of time a message is kept before being discarded.
            Essentially the amount of time (In milliseconds) a message can count towards spam
        warn_message : str, optional
            The message to be sent upon warnThreshold being reached
        kick_message : str, optional
            The message to be sent up kickThreshold being reached
        ban_message : str, optional
            The message to be sent up banThreshold being reached
        message_duplicate_count : int, optional
            Amount of duplicate messages needed to trip a punishment
        message_duplicate_accuracy : float, optional
            How 'close' messages need to be to be registered as duplicates (Out of 100)
        ignore_perms : list, optional
            The perms (ID Form), that bypass anti-spam
        ignore_users : list, optional
            The users (ID Form), that bypass anti-spam
        ignore_bots : bool, optional
            Should bots bypass anti-spam?
        """
        # Just gotta casually ignore_type check everything.
        if not isinstance(bot, commands.Bot):
            raise ValueError("Expected channel of ignore_type: commands.Bot")

        if not isinstance(verbose_level, int):
            raise ValueError("Verbosity should be an int between 0-5")
        if 0 > verbose_level or verbose_level > 5:
            raise ValueError("Verbosity should be between 0-5")

        if not isinstance(warn_threshold, int) and warn_threshold is not None:
            raise ValueError("Expected warn_threshold of ignore_type: int")

        if not isinstance(kick_threshold, int) and kick_threshold is not None:
            raise ValueError("Expected kick_threshold of ignore_type: int")

        if not isinstance(ban_threshold, int) and ban_threshold is not None:
            raise ValueError("Expected ban_threshold of ignore_type: int")

        if not isinstance(message_interval, int) and message_interval is not None:
            raise ValueError("Expected message_interval of ignore_type: int")

        if message_interval is not None and message_interval < 1000:
            raise BaseASHException("Minimum message_interval is 1 seconds (1000 ms)")

        if not isinstance(warn_message, str) and warn_message is not None:
            raise ValueError("Expected warn_message of ignore_type: str")

        if not isinstance(kick_message, str) and kick_message is not None:
            raise ValueError("Expected kick_message of ignore_type: str")

        if not isinstance(ban_message, str) and ban_message is not None:
            raise ValueError("Expected ban_message of ignore_type: str")

        if (
            not isinstance(message_duplicate_count, int)
            and message_duplicate_count is not None
        ):
            raise ValueError("Expected message_duplicate_count of ignore_type: int")

        # Convert message_duplicate_accuracy from int to float if exists
        if isinstance(message_duplicate_accuracy, int):
            message_duplicate_accuracy = float(message_duplicate_accuracy)
        if (
            not isinstance(message_duplicate_accuracy, float)
            and message_duplicate_accuracy is not None
        ):
            raise ValueError(
                "Expected message_duplicate_accuracy of ignore_type: float"
            )
        if message_duplicate_accuracy is not None:
            if 1.0 > message_duplicate_accuracy or message_duplicate_accuracy > 100.0:
                # Only accept values between 1 and 100
                raise ValueError(
                    "Expected message_duplicate_accuracy between 1 and 100"
                )

        if not isinstance(ignore_perms, list) and ignore_perms is not None:
            raise ValueError("Expected ignore_perms of ignore_type: list")

        if not isinstance(ignore_users, list) and ignore_users is not None:
            raise ValueError("Expected ignore_users of ignore_type: list")

        if not isinstance(ignore_channels, list) and ignore_channels is not None:
            raise ValueError("Expected ignore_channels of ignore_type: list")

        if not isinstance(ignore_roles, list) and ignore_roles is not None:
            raise ValueError("Expected ignore_roles of ignore_type: list")

        if not isinstance(ignore_guilds, list) and ignore_guilds is not None:
            raise ValueError("Expected ignore_guilds of ignore_type: list")

        if not isinstance(ignore_bots, bool) and ignore_bots is not None:
            raise ValueError("Expected ignore_bots of ignore_type: bool")

        # Now we have ignore_type checked everything, lets do some logic
        if ignore_bots is None:
            ignore_bots = Static.DEFAULTS.get("ignore_bots")

        # TODO Implement #16
        if ignore_roles is not None:
            placeholderIgnoreRoles = []
            for item in ignore_roles:
                if isinstance(item, discord.Role):
                    placeholderIgnoreRoles.append(item.id)
                elif isinstance(item, int):
                    placeholderIgnoreRoles.append(item)
                else:
                    raise ValueError("Expected discord.Role or int for ignore_roles")
            ignore_roles = placeholderIgnoreRoles

        self.options = {
            "warn_threshold": warn_threshold or Static.DEFAULTS.get("warn_threshold"),
            "kick_threshold": kick_threshold or Static.DEFAULTS.get("kick_threshold"),
            "ban_threshold": ban_threshold or Static.DEFAULTS.get("ban_threshold"),
            "message_interval": message_interval
            or Static.DEFAULTS.get("message_interval"),
            "warn_message": warn_message or Static.DEFAULTS.get("warn_message"),
            "kick_message": kick_message or Static.DEFAULTS.get("kick_message"),
            "ban_message": ban_message or Static.DEFAULTS.get("ban_message"),
            "message_duplicate_count": message_duplicate_count
            or Static.DEFAULTS.get("message_duplicate_count"),
            "message_duplicate_accuracy": message_duplicate_accuracy
            or Static.DEFAULTS.get("message_duplicate_accuracy"),
            "ignore_perms": ignore_perms or Static.DEFAULTS.get("ignore_perms"),
            "ignore_users": ignore_users or Static.DEFAULTS.get("ignore_users"),
            "ignore_channels": ignore_channels
            or Static.DEFAULTS.get("ignore_channels"),
            "ignore_roles": ignore_roles or Static.DEFAULTS.get("ignore_roles"),
            "ignore_guilds": ignore_guilds or Static.DEFAULTS.get("ignore_guilds"),
            "ignore_bots": ignore_bots,
        }

        self.bot = bot
        self._guilds = []

        logging.basicConfig(
            format="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
        )
        self.logger = logging.getLogger(__name__)
        if verbose_level == 0:
            self.logger.setLevel(level=logging.NOTSET)
        elif verbose_level == 1:
            self.logger.setLevel(level=logging.DEBUG)
        elif verbose_level == 2:
            self.logger.setLevel(level=logging.INFO)
        elif verbose_level == 3:
            self.logger.setLevel(level=logging.WARNING)
        elif verbose_level == 4:
            self.logger.setLevel(level=logging.ERROR)
        elif verbose_level == 5:
            self.logger.setLevel(level=logging.CRITICAL)

    def propagate(self, message: discord.Message) -> None:
        """
        This method is the base level intake for messages, then
        propagating it out to the relevant guild or creating one
        if that is required

        Parameters
        ==========
        message : discord.Message
            The message that needs to be propagated out
        """
        if not isinstance(message, discord.Message):
            raise ValueError("Expected message of ignore_type: discord.Message")

        # Ensure we only moderate actual guild messages
        if not message.guild:
            return

        if message.author.id == self.bot.user.id:
            return

        # Return if ignored bot
        if self.options["ignore_bots"] and message.author.bot:
            return

        # Return if ignored user
        if message.author.id in self.options["ignore_users"]:
            return

        # Return if ignored channel
        if message.channel.id in self.options["ignore_channels"]:
            return

        # Return if user has an ignored role
        userRolesId = [role.id for role in message.author.roles]
        for userRoleId in userRolesId:
            if userRoleId in self.options.get("ignore_roles"):
                return

        # Return if ignored guild
        if message.guild.id in self.options.get("ignore_guilds"):
            return

        self.logger.debug(
            f"Propagating message for: {message.author.name}({message.author.id})"
        )

        guild = Guild(self.bot, message.guild.id, self.options, logger=self.logger)
        try:
            guild = next(iter(g for g in self.guilds if g == guild))
        except StopIteration:
            # Check we have perms to actually create this guild object
            # and punish based upon our guild wide permissions
            perms = message.guild.me.guild_permissions
            if not perms.kick_members or not perms.ban_members:
                raise MissingGuildPermissions

            self.guilds = guild
            self.logger.info(f"Created Guild: {guild.id}")

        guild.propagate(message)

    def add_ignored_item(self, item: int, ignore_type: str) -> None:
        """
        Add an item to the relevant ignore list

        Parameters
        ----------
        item : int
            The id of the thing to ignore
        ignore_type : str
            A string representation of the ignored
            items overall container

        Raises
        ======
        BaseASHException
            Invalid ignore ignore_type
        ValueError
            item is not of ignore_type int or int convertible

        Notes
        =====
        This will silently ignore any attempts
        to add an item already added.
        """
        ignore_type = ignore_type.lower()
        if not isinstance(item, int):
            item = int(item)

        if ignore_type == "user":
            if item not in self.options["ignore_users"]:
                self.options["ignore_users"].append(item)
        elif ignore_type == "channel":
            if item not in self.options["ignore_channels"]:
                self.options["ignore_channels"].append(item)
        elif ignore_type == "perm":
            if item not in self.options["ignore_perms"]:
                self.options["ignore_perms"].append(item)
        elif ignore_type == "guild":
            if item not in self.options["ignore_guilds"]:
                self.options["ignore_guilds"].append(item)
        elif ignore_type == "role":
            if item not in self.options["ignore_roles"]:
                self.options["ignore_roles"].append(item)
        else:
            raise BaseASHException("Invalid ignore ignore_type")

        self.logger.debug(f"Ignored {ignore_type}: {item}")

    def remove_ignored_item(self, item: int, ignore_type: str) -> None:
        """
        Remove an item from the relevant ignore list

        Parameters
        ----------
        item : int
            The id of the thing to unignore
        ignore_type : str
            A string representation of the ignored
            items overall container

        Raises
        ======
        BaseASHException
            Invalid ignore ignore_type
        ValueError
            item is not of ignore_type int or int convertible

        Notes
        =====
        This will silently ignore any attempts
        to remove an item not ignored.
        """
        ignore_type = ignore_type.lower()
        if not isinstance(item, int):
            item = int(item)

        if ignore_type == "user":
            if item in self.options["ignore_users"]:
                index = self.options["ignore_users"].index(item)
                self.options["ignore_users"].pop(index)
        elif ignore_type == "channel":
            if item in self.options["ignore_channels"]:
                index = self.options["ignore_channels"].index(item)
                self.options["ignore_channels"].pop(index)
        elif ignore_type == "perm":
            if item in self.options["ignore_perms"]:
                index = self.options["ignore_perms"].index(item)
                self.options["ignore_perms"].pop(index)
        else:
            raise BaseASHException("Invalid ignore ignore_type")

        self.logger.debug(f"Un-Ignored {ignore_type}: {item}")

    # <-- Getter & Setters -->
    @property
    def guilds(self):
        return self._guilds

    @guilds.setter
    def guilds(self, value):
        """
        Raises
        ======
        DuplicateObject
            It won't maintain two guild objects with the same
            id's, and it will complain about it haha
        ObjectMismatch
            Raised if `value` wasn't made by this person, so they
            shouldn't be the ones maintaining the reference
        """
        if not isinstance(value, Guild):
            raise ValueError("Expected Guild object")

        for guild in self._guilds:
            if guild == value:
                raise DuplicateObject

        self._guilds.append(value)
