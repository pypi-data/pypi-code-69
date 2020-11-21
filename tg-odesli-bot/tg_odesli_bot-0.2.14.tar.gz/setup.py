# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tg_odesli_bot']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0',
 'aiogram>=2.11,<3.0',
 'aiohttp>=3.6.2,<4.0.0',
 'marshmallow>=3.5.0,<4.0.0',
 'python-dotenv>=0.15.0,<0.16.0',
 'sentry-sdk>=0.19.0,<0.20.0',
 'structlog-sentry>=1.2.1,<2.0.0',
 'structlog>=20.1.0,<21.0.0',
 'ujson>=4.0.0,<5.0.0']

entry_points = \
{'console_scripts': ['tg-odesli-bot = tg_odesli_bot.bot:main']}

setup_kwargs = {
    'name': 'tg-odesli-bot',
    'version': '0.2.14',
    'description': 'Telegram Bot to share music with Odesli (former Songlink) service.',
    'long_description': '# Telegram Odesli Bot\n\nSend a song link in any (supported) music streaming service and get back\na message with links in other services.\n\nAdd in Telegram: [@odesli\\_bot](https://t.me/odesli_bot)\n\nIt\'s useful but still work in progress. Some turbulence is expected.\n\n[![PyPI](https://img.shields.io/pypi/v/tg-odesli-bot?color=blue)](https://pypi.org/project/tg-odesli-bot/)\n[![Azure build status](https://dev.azure.com/9dogs/tg-odesli-bot/_apis/build/status/9dogs.tg-odesli-bot?branchName=master)](https://github.com/9dogs/tg-odesli-bot)\n[![Code coverage](https://codecov.io/gh/9dogs/tg-odesli-bot/branch/master/graph/badge.svg?token=3nWZWJ3Bl3)](https://codecov.io/gh/9dogs/tg-odesli-bot)\n[![Docker build](https://img.shields.io/docker/cloud/automated/9dogs/tg-odesli-bot)](https://hub.docker.com/r/9dogs/tg-odesli-bot)\n[![Supported versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://github.com/9dogs/tg-odesli-bot)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## What is it for?\n\nYou love to share music with your friends (or be shared with), but you\nsettled in different streaming services? With the help of this bot you\ncan share any song link to the Bot and get all other links back in\nreply.\n\nPowered by the great [Odesli](https://odesli.co/) (former Songlink) service.\n\nYou can message the bot directly, invite it to group chats or use an inline\nmode (type `@odesli_bot <URL>`). In group chats the bot will react only to\nmessages with music streaming links (it will also skip messages marked with\nspecial token `!skip`). You can promote the bot to a group admin and it\nwill remove original message so that the chat remains tidy.\n\nOriginal message           |  Bot\'s replay\n:-------------------------:|:-------------------------:\n<img alt="Original message" title="Original message" src="https://user-images.githubusercontent.com/432235/67324149-0a2b2580-f51c-11e9-8ce2-033cdf2d6628.png" height="200px">  | <img alt="Bot\'s reply" title="Bot\'s reply" src="https://user-images.githubusercontent.com/432235/67324159-0dbeac80-f51c-11e9-834a-7d4831a661d8.png" height="200px">\n\n## Features\n\n- Inline mode\n- Private chat mode\n- Group chat mode\n\n## Supported services\n\nCurrently the following services are supported:\n\n  - Deezer\n  - Google Music\n  - SoundCloud\n  - Yandex Music\n  - Spotify\n  - YouTube Music\n  - YouTube\n  - Apple Music\n  - Tidal\n\n## Privacy considerations\n\nThe bot have to have access to messages in group chats to operate (that\nis, it operates with disabled [privacy\nmode](https://core.telegram.org/bots#privacy-mode)). It does not store\nnor transfer messages anywhere. However, the only way to be completely\nprivate is to read through source code in this repository **and** run\nyour copy of the bot (see section below). Or simply create a special\ngroup only for music sharing and where no sensitive information will be\nposted.\n\n## Running your own copy\n\n### Prerequisites\n\nYou need a Telegram [bot\ntoken](https://core.telegram.org/bots/api#authorizing-your-bot) to run\nyour copy of the bot. Don\'t worry, it can be obtained easily. Follow the\n[instructions](https://core.telegram.org/bots#6-botfather) to create a\nnew bot (you can set a name and a username to whatever you want). All you\nneed is a string like `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw` -\nthis is your new bot token.\n\nAdditionally, disable privacy mode for your bot in a dialog with\n@BotFather: "Group Privacy" - "Turn off" (that is for the bot to be able\nto read group messages).\n\nBot from this repository will looks for `TG_ODESLI_BOT_TG_API_TOKEN`\nenvironment variable on start, thus you must set it either in shell or\nvia `.env` file:\n\n```console\n$ echo "<your_token>" > .env\n$ # OR\n$ TG_ODESLI_BOT_TG_API_TOKEN=<your_token> <bot_run_command (see below)>\n```\n\nOnes you obtain a Telegram bot token, you can run bot using either Python\n(3.7 or 3.8) or Docker.\n\n### Run PyPI version\n\nCreate virtual environment, install `tg-odesli-bot` package and run the bot\nwith `tg-odesli-bot` command:\n\n```console\n$ python -m venv botenv\n$ source botenv/bin/activate\n$ pip install tg-odesli-bot\n$ TG_ODESLI_BOT_TG_API_TOKEN=<your_token> tg-odesli-bot\n```\n\n### Run with Docker\n\nSet `TG_ODESLI_BOT_TG_API_TOKEN` environment variable and run the image\n`9dogs/tg-odesli-bot` (in order to use the `.env` file, mount it to\n`/opt/tg-odesli-bot/.env`):\n\n```console\n$ docker run --rm -it -v /path/to/.env:/opt/tg-odesli-bot/.env 9dogs/tg-odesli-bot\n# OR\n$ TG_ODESLI_BOT_TG_API_TOKEN=<your_token> docker run -it --rm 9dogs/tg-odesli-bot\n```\n\n\n### Run version from the repository\n\nClone this repository, [install\npoetry](https://python-poetry.org/docs/#installation), copy `.env` file\ninto the project\'s root directory and run the bot:\n\n```console\n$ git clone https://github.com/9dogs/tg-odesli-bot.git && cd tg-odesli-bot\n# Install dependencies\n$ poetry install\n# If you have token in .env file\n$ cp /path/to/.env ./\n$ poetry run tg-odesli-bot\n# If you specify token via shell env var\n$ TG_ODESLI_BOT_TG_API_TOKEN=<your_token> poetry run tg-odesli-bot\n```\n\n## Contributing\n\nContributions are welcome via GitHub pull requests. The easiest way to bootstrap\ndevelopment environment is to build `builder` target of Docker image:\n```console\n$ git clone https://github.com/9dogs/tg-odesli-bot.git && cd tg-odesli-bot\n$ docker build -t 9dogs/tg-odesli-bot:dev --target=builder --build-arg poetry_args= .\n```\nThen you can run a shell inside the container:\n```console\n$ docker run -it --rm -v %cd%:/opt/tg-odesli-bot -v /opt/tg-odesli-bot/.venv 9dogs/tg-odesli-bot:dev bash\n(container)$ make lint test\n```\n',
    'author': 'Mikhail Knyazev',
    'author_email': 'hellishbot@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/9dogs/tg-odesli-bot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
