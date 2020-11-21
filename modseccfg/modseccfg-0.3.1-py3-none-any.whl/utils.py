# encoding: utf-8
# api: python
# type: functions
# category: utils
# title:  Utils & Config
# description: various shortcut functions, config data, UI and remoting wrappers
# version: 0.4
# depends: pluginconf (>= 0.7.2), python:appdirs, python:pathlib
# config:
#   { name: sshfs_mount, type: str, value: "~/.config/modseccfg/mnt/", description: "Remote connection (sshfs) mount point", help: "This will be used for `modseccfg vps123:` invocations to bind the servers / root locally." }
#    { name: "test[key]", type: bool, value: 1, description: "Array[key] test" }
# state: alpha
#
# Contains some utility code, and Python module monkeypatching.
#
# With `srvroot` all file access gets encapsulated, so it works
# locally or over sshfs.
#
# The `conf` dict is read from `~/.config/modseccfg/settings.json`.
# Defaults are built in, or module-extracted via pluginconf. The
# settings GUI also courtesy of.
#


import sys
import os
import pathlib
import re
import functools
import subprocess
import atexit
import json
import pluginconf, pluginconf.gui
import appdirs
try: import frosch; frosch.hook()
except: pass


#-- config defaults
conf = {
    # mainwindow
    "theme": "DefaultNoNagging",
    "switch_auto": 0,
    "keyboard_binds": 1,
    # writer
    "edit_sys_files": False,
    "backup_files": True,
    "backup_dir": "~/backup-config/",
    # logs
    "log_entries": 5000,
    "log_filter": "(?!404|429)[45]\d\d",
    "log_skip_rx" : "PetalBot|/.well-known/ignore.cgi",
    "add_stub_logs": 1,    # data/common_false_*.log
    # utils
    "sshfs_mount": "~/mnt/",
    "sshfs_o": "",
    "conf_dir": appdirs.user_config_dir("modseccfg", "io"),
    "conf_file": "settings.json",
    "plugins": {
        "__init__": 1,
        "mainwindow": 1,
        "appsettings": 1,
        "utils": 1,
        "vhosts": 1,
        "logs": 1,
        "writer": 1
    }
}

#-- plugin lookup
pluginconf.module_base = __name__
pluginconf.plugin_base = [__package__]
for module,meta in pluginconf.all_plugin_meta().items():
    pluginconf.add_plugin_defaults(conf, {}, meta, module)


#-- path
def expandpath(dir):
    return str(pathlib.Path(dir).expanduser())

#-- @decorator to override module function
@functools.singledispatch
def inject(mod):
    def decorator(func):
        setattr(mod, func.__name__, func)
    return decorator
#-- patch re for \h support
@inject(re)
def compile(regex, *kargs, re_compile_orig=re.compile, **kwargs):
    if type(regex) is str:
        regex = re.sub(r'\\h(?![^\[]*\])', r'[\ \t\f]', regex)
        #print("re_compile: " + regex)
    return re_compile_orig(regex, *kargs, **kwargs)
@inject(re)
def grep(regex, list, flags=0):
    return [s for s in list if re.search(regex, s, flags)]
    





#-- remote/sshfs bindings
#
# This wraps any modseccfg file operations on config or log files.
# If modseccfg is started with a ssh:/ parameter, then we'll connect
# the remote file system. All file IO uses the mount prefix henceforth;
# thusly enabling remote log scans and config editing.
# (Because X11 forwarding with Python/Tkinter is unworkable at best.)
#
class remote:

    # initialize if argv[] contains any `(user@)hostname:/`
    def __init__(self, srv=[]):
        if not srv:
            self.local = 1
            self.mnt = ""
            self.srv = self.srvname = ""
        else:
            self.local = 0
            self.srvname = re.sub(":.*?$", "", srv[0])
            self.srv = self.srvname + ":/"   # must be / root
            self.mnt = expandpath(conf["sshfs_mount"]) + "/" + self.srv
            os.makedirs(self.mnt, 0o0700, True)
            sshfs_o = re.sub("(^\s*(?=\w)|-o\s*|[^\w=]+)", "-o ", conf.get("sshfs_o", ""))
            os.system(f"sshfs {sshfs_o} {self.srv}/ {self.mnt}")
            atexit.register(self.umount)

    def umount(self):
        if self.mnt and self.srv:
            os.system("fusermount -u " + self.mnt)
            os.rmdir(self.mnt)

    def fn(self, fn):
        return self.mnt + fn

    def read(self, fn):
        if not self.exists(fn):
            if not re.search("letsencrypt|ssl", fn):
                print("WARNING: file not found", self.mnt, fn)
            return ""
        with open(self.fn(fn), "r", encoding="utf8") as f:
            return f.read()

    def write(self, fn, src):
        with open(self.fn(fn), "w", encoding="utf8") as f:
            return f.write(src)

    def popen(self, cmd, action="r"):
        if not self.local:
            cmd = ["ssh", self.srvname] + cmd
        if action=="r":
            return subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
        else:
            return subprocess.Popen(cmd, stdin=subprocess.PIPE).stdin

    def exists(self, fn):
        return os.path.exists(self.fn(fn))

    def writable(self, fn):
        if self.local:
            return os.access(self.fn(fn), os.W_OK)
        else:
            return True  # need a real test here
    writeable=writable  # alias
            
# initialize with argv[]
srvroot = remote(re.grep("\w+:", sys.argv[1:]))


#-- read config file
def cfg_read():
    fn = conf["conf_dir"] + "/" + conf["conf_file"]
    if os.path.exists(fn):
        conf.update(json.load(open(fn, "r", encoding="utf8")))

# write config file
def cfg_write():
    os.makedirs(conf["conf_dir"], 0o755, True)
    #print(str(conf))
    fn = conf["conf_dir"] + "/" + conf["conf_file"]
    json.dump(conf, open(fn, "w", encoding="utf8"), indent=4)

# show config option dialog
def cfg_window(mainself, *kargs):
    fn_py = __file__.replace("utils", "*")
    save = pluginconf.gui.window(conf, conf["plugins"], files=[fn_py], theme=conf["theme"])
    if save:
        cfg_write()

# initialze conf{}
cfg_read()
