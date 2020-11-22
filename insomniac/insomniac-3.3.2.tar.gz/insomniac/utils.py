import json
import os
import re
import shutil
import ssl
import urllib.request
from datetime import datetime
from random import randint
from time import sleep
from urllib.error import URLError

from insomniac.__version__ import __version__

COLOR_HEADER = '\033[95m'
COLOR_OKBLUE = '\033[94m'
COLOR_OKGREEN = '\033[92m'
COLOR_REPORT = '\033[93m'
COLOR_FAIL = '\033[91m'
COLOR_ENDC = '\033[0m'
COLOR_BOLD = '\033[1m'
COLOR_UNDERLINE = '\033[4m'


def print_version():
    current_version = __version__
    print_timeless(COLOR_HEADER + f"Insomniac v{current_version}" + COLOR_ENDC)
    latest_version = _get_latest_version('insomniac')
    if latest_version is not None and latest_version > current_version:
        print_timeless(COLOR_HEADER + f"Newer version is available (v{latest_version}). Please run" + COLOR_ENDC)
        print_timeless(COLOR_HEADER + COLOR_BOLD + "python3 -m pip install insomniac --upgrade" + COLOR_ENDC)
    print_timeless("")


def get_instagram_version(device_id):
    stream = os.popen("adb" + ("" if device_id is None else " -s " + device_id) +
                      " shell dumpsys package com.instagram.android")
    output = stream.read()
    version_match = re.findall('versionName=(\\S+)', output)
    if len(version_match) == 1:
        version = version_match[0]
    else:
        version = "not found"
    stream.close()
    return version


def check_adb_connection(is_device_id_provided):
    stream = os.popen('adb devices')
    output = stream.read()
    devices_count = len(re.findall('device\n', output))
    stream.close()

    is_ok = True
    message = "That's ok."
    if devices_count == 0:
        is_ok = False
        message = "Cannot proceed."
    elif devices_count > 1 and not is_device_id_provided:
        is_ok = False
        message = "Use --device to specify a device."

    print_timeless(("" if is_ok else COLOR_FAIL) + "Connected devices via adb: " + str(devices_count) + ". " + message +
                   COLOR_ENDC)
    return is_ok


def random_sleep():
    delay = randint(1, 4)
    print("Sleep for " + str(delay) + (delay == 1 and " second" or " seconds"))
    sleep(delay)


def open_instagram(device_id):
    print("Open Instagram app")
    os.popen("adb" + ("" if device_id is None else " -s " + device_id) +
             " shell am start -n com.instagram.android/com.instagram.mainactivity.MainActivity").close()
    random_sleep()


def close_instagram(device_id):
    print("Close Instagram app")
    os.popen("adb" + ("" if device_id is None else " -s " + device_id) +
             " shell am force-stop com.instagram.android").close()


def save_crash(device):
    global print_log

    directory_name = "Crash-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    try:
        os.makedirs("crashes/" + directory_name + "/", exist_ok=False)
    except OSError:
        print(COLOR_FAIL + "Directory " + directory_name + " already exists." + COLOR_ENDC)
        return

    screenshot_format = ".png" if device.is_old() else ".jpg"
    try:
        device.screenshot("crashes/" + directory_name + "/screenshot" + screenshot_format)
    except RuntimeError:
        print(COLOR_FAIL + "Cannot save screenshot." + COLOR_ENDC)

    view_hierarchy_format = ".xml"
    try:
        device.dump_hierarchy("crashes/" + directory_name + "/view_hierarchy" + view_hierarchy_format)
    except RuntimeError:
        print(COLOR_FAIL + "Cannot save view hierarchy." + COLOR_ENDC)

    with open("crashes/" + directory_name + "/logs.txt", 'w', encoding="utf-8") as outfile:
        outfile.write(print_log)

    shutil.make_archive("crashes/" + directory_name, 'zip', "crashes/" + directory_name + "/")
    shutil.rmtree("crashes/" + directory_name + "/")

    print(COLOR_OKGREEN + "Crash saved as \"crashes/" + directory_name + ".zip\"." + COLOR_ENDC)
    print(COLOR_OKGREEN + "Please attach this file if you gonna report the crash at" + COLOR_ENDC)
    print(COLOR_OKGREEN + "https://github.com/alexal1/Insomniac/issues\n" + COLOR_ENDC)


def detect_block(device):
    block_dialog = device.find(resourceId='com.instagram.android:id/dialog_root_view',
                               className='android.widget.FrameLayout')
    is_blocked = block_dialog.exists()
    if is_blocked:
        print(COLOR_FAIL + "Probably block dialog is shown." + COLOR_ENDC)
        raise ActionBlockedError("Seems that action is blocked. Consider reinstalling Instagram app and be more careful"
                                 " with limits!")


def print_copyright():
    print_timeless("\nIf you like this script, please " + COLOR_BOLD + "give us a star" + COLOR_ENDC + ":")
    print_timeless(COLOR_BOLD + "https://github.com/alexal1/Insomniac\n" + COLOR_ENDC)


def _print_with_time_decorator(standard_print, print_time):
    def wrapper(*args, **kwargs):
        global print_log
        if print_time:
            time = datetime.now().strftime("%m/%d %H:%M:%S")
            print_log += re.sub(r"\[\d+m", '', ("[" + time + "] " + str(*args, **kwargs) + "\n"))
            return standard_print("[" + time + "]", *args, **kwargs)
        else:
            print_log += re.sub(r"\[\d+m", '', (str(*args, **kwargs) + "\n"))
            return standard_print(*args, **kwargs)

    return wrapper


def _get_latest_version(package):
    latest_version = None
    try:
        with urllib.request.urlopen(f"https://pypi.python.org/pypi/{package}/json",
                                    context=ssl.SSLContext()) as response:
            if response.code == 200:
                json_package = json.loads(response.read())
                latest_version = json_package['info']['version']
    except URLError:
        return None
    return latest_version


def get_value(count, name, default, max_count=None):
    def print_error():
        print(COLOR_FAIL + name.format(default) + f". Using default value instead of \"{count}\", because it must be "
                                                  "either a number (e.g. 2) or a range (e.g. 2-4)." + COLOR_ENDC)

    parts = count.split("-")
    if len(parts) <= 0:
        value = default
        print_error()
    elif len(parts) == 1:
        try:
            value = int(count)
            print(COLOR_BOLD + name.format(value) + COLOR_ENDC)
        except ValueError:
            value = default
            print_error()
    elif len(parts) == 2:
        try:
            value = randint(int(parts[0]), int(parts[1]))
            print(COLOR_BOLD + name.format(value) + COLOR_ENDC)
        except ValueError:
            value = default
            print_error()
    else:
        value = default
        print_error()

    if max_count is not None and value > max_count:
        print(COLOR_FAIL + name.format(max_count) + f". This is max value." + COLOR_ENDC)
        value = max_count
    return value


def get_left_right_values(left_right_str, name, default):
    def print_error():
        print(COLOR_FAIL + name.format(default) + f". Using default value instead of \"{left_right_str}\", because it "
                                                  "must be either a number (e.g. 2) or a range (e.g. 2-4)." + COLOR_ENDC)

    parts = left_right_str.split("-")
    if len(parts) <= 0:
        value = default
        print_error()
    elif len(parts) == 1:
        try:
            value = (int(left_right_str), int(left_right_str))
            print(COLOR_BOLD + name.format(value) + COLOR_ENDC)
        except ValueError:
            value = default
            print_error()
    elif len(parts) == 2:
        try:
            value = (int(parts[0]), int(parts[1]))
            print(COLOR_BOLD + name.format(value) + COLOR_ENDC)
        except ValueError:
            value = default
            print_error()
    else:
        value = default
        print_error()
    return value


def get_count_of_nums_in_str(string):
    count = 0
    for i in range(0, 10):
        count += string.count(str(i))

    return count


print_log = ""
print_timeless = _print_with_time_decorator(print, False)
print = _print_with_time_decorator(print, True)


class ActionBlockedError(Exception):
    pass
