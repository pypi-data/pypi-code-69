""" application entry point """
import json
import logging
import os
import tornado.ioloop
import tornado.web
import tornado.log
import convoke
from dotenv import load_dotenv
from pkg_resources import resource_filename

from .handlers import EditorHandler
from .handlers import SiteHandler
from .handlers import DirHandler
from .handlers import MarkHandler
from .handlers import S3Browser
from .handlers import AssetHandler
from .handlers import LoginHandler, LogoutHandler

LOGGER = logging.getLogger(__name__)


def make_app_path(settings, name, default):
    """ return path relative to app """
    return os.path.join(
        settings.get("app_path", ""), settings.get(name, default)
    )


def make_app():
    """ make a tornado application """
    settings = convoke.get_settings("duckdown")

    static_path = make_app_path(settings, "static_path", "static")
    template_path = make_app_path(settings, "template_path", "templates")
    pages_path = make_app_path(settings, "pages_path", "pages")
    users_path = make_app_path(settings, "users_path", "users.json")
    img_path = settings.get("img_path", "")

    tornado_settings = {
        "debug": settings.as_bool("debug", default="False"),
        "port": settings.as_int("port", default="8080"),
        "duck_users": users_path,
        "duck_path": "/edit/assets/",
        "duck_assets": resource_filename("duckdown", "assets"),
        "duck_templates": resource_filename("duckdown", "templates"),
        "static_path": settings.get("static", static_path),
        "template_path": settings.get("templates", template_path),
        "cookie_name": settings.get("cookie_name", "duckdown-cookie"),
        "cookie_secret": settings.get(
            "cookie_secret", "it was a dark and stormy duckdown"
        ),
        "login_url": settings.get("login_url", "/login"),
        "app_name": settings.get("app_name", "duckdown-app"),
        "local_images": settings.as_bool("local_images", default="False"),
        "img_path": img_path,
    }

    # load aws credentials
    image_bucket = {
        "bucket_name": settings.get("image_bucket", ""),
        "aws_access_key_id": settings.get("AWS_ACCESS_KEY_ID", ""),
        "aws_secret_access_key": settings.get("AWS_SECRET_ACCESS_KEY", ""),
    }

    LOGGER.info("settings:")
    for key, value in tornado_settings.items():
        LOGGER.info("\t%s: %r", key, value)

    routes = [
        (r"/login", LoginHandler, {"users": json.load(open(users_path))}),
        (r"/logout", LogoutHandler),
        (r"/browse/(.*)", S3Browser, image_bucket),
        (
            r"/edit/assets/(.*)",
            AssetHandler,
            {"path": tornado_settings["duck_assets"]},
        ),
        (r"/edit/mark/", MarkHandler),
        (r"/edit/pages/(.*)", DirHandler, {"directory": pages_path}),
        (r"/edit", EditorHandler),
        (r"/(.*)", SiteHandler, {"docs": pages_path}),
    ]

    return tornado.web.Application(routes, **tornado_settings)


def main():
    """ make an app and run it """
    load_dotenv(verbose=True)
    app = make_app()

    app.listen(app.settings["port"])
    LOGGER.info("listening on port: %s", app.settings["port"])

    if app.settings["debug"] is True:
        LOGGER.info("running in debug mode")

    ioloop = tornado.ioloop.IOLoop.current()
    try:
        ioloop.start()
    except KeyboardInterrupt:
        LOGGER.info("shutting down")
        ioloop.stop()


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    main()
