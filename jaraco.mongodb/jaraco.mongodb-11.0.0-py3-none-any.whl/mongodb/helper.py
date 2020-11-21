"""
Helper functions to augment PyMongo
"""

import warnings

import pymongo
import gridfs


def filter_warnings():
    warnings.warn(
        "filter_warnings is deprecated and has no effect; do not call",
        DeprecationWarning,
    )


def connect(uri, factory=pymongo.MongoClient):
    """
    Use the factory to establish a connection to uri.
    """
    warnings.warn("do not use. Just call MongoClient directly.", DeprecationWarning)
    return factory(uri)


def connect_db(uri, default_db_name=None, factory=pymongo.MongoClient):
    """
    Use pymongo to parse a uri (possibly including database name) into
    a connected database object.

    This serves as a convenience function for the common use case where one
    wishes to get the Database object and is less concerned about the
    intermediate MongoClient object that pymongo creates (though the
    connection is always available as db.client).

    >>> db = connect_db(
    ...     'mongodb://mongodb.localhost/mydb?readPreference=secondary')
    >>> db.name
    'mydb'
    >>> db.client.read_preference
    Secondary(...)

    If no database is indicated in the uri, fall back to default.

    >>> db = connect_db('mongodb://mgo/', 'defaultdb')
    >>> db.name
    'defaultdb'

    The default should only apply if no db was present in the URI.

    >>> db = connect_db('mongodb://mgo/mydb', 'defaultdb')
    >>> db.name
    'mydb'
    """
    uri_p = pymongo.uri_parser.parse_uri(uri)
    client = factory(uri)
    return client.get_database(uri_p['database'] or default_db_name)


def get_collection(uri):
    return pymongo.uri_parser.parse_uri(uri)['collection']


def connect_gridfs(uri, db=None):
    """
    Construct a GridFS instance for a MongoDB URI.
    """
    return gridfs.GridFS(
        db or connect_db(uri),
        collection=get_collection(uri) or 'fs',
    )
