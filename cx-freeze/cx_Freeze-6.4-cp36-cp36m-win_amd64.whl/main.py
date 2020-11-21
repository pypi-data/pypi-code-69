"""
cxfreeze command line tool
"""

import argparse
import os
import sys

import cx_Freeze
from cx_Freeze.common import normalize_to_list

__all__ = ["main"]

DESCRIPTION = """
Freeze a Python script and all of its referenced modules to a base \
executable which can then be distributed without requiring a Python \
installation.
"""

VERSION = """
%(prog)s {}
Copyright (c) 2007-2020 Anthony Tuininga. All rights reserved.
Copyright (c) 2001-2006 Computronix Corporation. All rights reserved.
""".format(
    cx_Freeze.__version__
)


def prepare_parser():
    parser = argparse.ArgumentParser(epilog=VERSION)
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("script", nargs="?", metavar="SCRIPT")
    parser.add_argument(
        "-O",
        action="count",
        default=0,
        dest="optimize_flag",
        help="optimize generated bytecode as per PYTHONOPTIMIZE; "
        "use -OO in order to remove doc strings",
    )
    parser.add_argument(
        "-c",
        "--compress",
        action="store_true",
        dest="compress",
        help="compress byte code in zip files",
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        dest="silent",
        help="suppress all output except warnings and errors",
    )
    parser.add_argument(
        "--base-name",
        dest="base_name",
        metavar="NAME",
        help="file on which to base the target file; if the name of the file "
        "is not an absolute file name, the subdirectory bases (rooted in the "
        "directory in which the freezer is found) will be searched for a file "
        "matching the name",
    )
    parser.add_argument(
        "--init-script",
        dest="init_script",
        metavar="NAME",
        help="script which will be executed upon startup; if the name of the "
        "file is not an absolute file name, the subdirectory initscripts "
        "(rooted in the directory in which the cx_Freeze package is found) "
        "will be searched for a file matching the name",
    )
    parser.add_argument(
        "--target-dir",
        "--install-dir",
        dest="target_dir",
        metavar="DIR",
        help="the directory in which to place the target file and any "
        "dependent files",
    )
    parser.add_argument(
        "--target-name",
        dest="target_name",
        metavar="NAME",
        help="the name of the file to create instead of the base name "
        "of the script and the extension of the base binary",
    )
    parser.add_argument(
        "--default-path",
        action="append",
        dest="default_path",
        metavar="DIRS",
        help="list of paths separated by the standard path separator for the "
        "platform which will be used to initialize sys.path prior to running "
        "the module finder",
    )
    parser.add_argument(
        "--include-path",
        action="append",
        dest="include_path",
        metavar="DIRS",
        help="list of paths separated by the standard path separator for the "
        "platform which will be used to modify sys.path prior to running the "
        "module finder",
    )
    parser.add_argument(
        "--replace-paths",
        dest="replace_paths",
        metavar="DIRECTIVES",
        help="replace all the paths in modules found in the given paths with "
        "the given replacement string; multiple values are separated by the "
        "standard path separator and each value is of the form "
        "path=replacement_string; path can be * which means all paths not "
        "already specified",
    )
    parser.add_argument(
        "--includes",
        "--include-modules",
        dest="includes",
        metavar="NAMES",
        help="comma separated list of modules to include",
    )
    parser.add_argument(
        "--excludes",
        "--exclude-modules",
        dest="excludes",
        metavar="NAMES",
        help="comma separated list of modules to exclude",
    )
    parser.add_argument(
        "--packages",
        dest="packages",
        metavar="NAMES",
        help="comma separated list of packages to include, which includes all "
        "submodules in the package",
    )
    parser.add_argument(
        "--include-files",
        dest="include_files",
        metavar="NAMES",
        help="comma separated list of paths to include",
    )
    parser.add_argument(
        "-z",
        "--zip-include",
        dest="zip_includes",
        action="append",
        default=[],
        metavar="SPEC",
        help="name of file to add to the zip file or a specification of the "
        "form name=arcname which will specify the archive name to use; "
        "multiple --zip-include arguments can be used",
    )
    parser.add_argument(
        "--zip-include-packages",
        dest="zip_include_packages",
        metavar="NAMES",
        help="comma separated list of packages which should be included in "
        "the zip file; the default is for all packages to be placed in the "
        "file system, not the zip file; those packages which are known to "
        "work well inside a zip file can be included if desired; use * to "
        "specify that all packages should be included in the zip file",
    )
    parser.add_argument(
        "--zip-exclude-packages",
        dest="zip_exclude_packages",
        default="*",
        metavar="NAMES",
        help="comma separated list of packages which should be excluded from "
        "the zip file and placed in the file system instead; the default is "
        "for all packages to be placed in the file system since a number of pa"
        "ckages assume that is where they are found and will fail when placed "
        "in a zip file; use * to specify that all packages should be placed "
        "in the file system and excluded from the zip file (the default)",
    )
    parser.add_argument(
        "--icon", dest="icon", help="name of the icon file for the application"
    )
    # remove the initial "usage: " of format_usage()
    parser.usage = parser.format_usage()[len("usage: ") :] + DESCRIPTION
    return parser


def parse_command_line(parser):
    args = parser.parse_args()
    if args.script is None and args.includes is None:
        parser.error("script or a list of modules must be specified")
    if args.script is None and args.target_name is None:
        parser.error("script or a target name must be specified")
    args.excludes = normalize_to_list(args.excludes)
    args.includes = normalize_to_list(args.includes)
    args.packages = normalize_to_list(args.packages)
    args.zip_include_packages = normalize_to_list(args.zip_include_packages)
    args.zip_exclude_packages = normalize_to_list(args.zip_exclude_packages)
    replace_paths = []
    if args.replace_paths:
        for directive in args.replace_paths.split(os.pathsep):
            from_path, replacement = directive.split("=")
            replace_paths.append((from_path, replacement))
    args.replace_paths = replace_paths
    if args.default_path is not None:
        sys.path = [
            p for mp in args.default_path for p in mp.split(os.pathsep)
        ]
    if args.include_path is not None:
        paths = [p for mp in args.include_path for p in mp.split(os.pathsep)]
        sys.path = paths + sys.path
    if args.script is not None:
        sys.path.insert(0, os.path.dirname(args.script))
    args.include_files = normalize_to_list(args.include_files)
    zip_includes = []
    if args.zip_includes:
        for spec in args.zip_includes:
            if "=" in spec:
                zip_includes.append(spec.split("=", 1))
            else:
                zip_includes.append(spec)
    args.zip_includes = zip_includes
    return args


def main():
    args = parse_command_line(prepare_parser())
    executables = [
        cx_Freeze.Executable(
            args.script,
            args.init_script,
            args.base_name,
            args.target_name,
            args.icon,
        )
    ]
    freezer = cx_Freeze.Freezer(
        executables,
        includes=args.includes,
        excludes=args.excludes,
        packages=args.packages,
        replacePaths=args.replace_paths,
        compress=args.compress,
        optimizeFlag=args.optimize_flag,
        path=None,
        targetDir=args.target_dir,
        includeFiles=args.include_files,
        zipIncludes=args.zip_includes,
        silent=args.silent,
        zipIncludePackages=args.zip_include_packages,
        zipExcludePackages=args.zip_exclude_packages,
    )
    freezer.Freeze()
