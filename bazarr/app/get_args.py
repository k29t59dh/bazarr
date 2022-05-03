# coding=utf-8

import os
import argparse

from distutils.util import strtobool

no_update = bool(os.environ.get("NO_UPDATE", False))
parser = argparse.ArgumentParser()


def get_args():
    parser.register('type', bool, strtobool)

    config_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data'))
    parser.add_argument('-c', '--config', default=config_dir, type=str, metavar="DIR",
                        dest="config_dir", help="Directory containing the configuration (default: %s)" % config_dir)
    parser.add_argument('-p', '--port', type=int, metavar="PORT", dest="port",
                        help="Port number (default: 6767)")
    if not no_update:
        parser.add_argument('--no-update', default=False, type=bool, const=True, metavar="BOOL", nargs="?",
                            help="Disable update functionality (default: False)")
    parser.add_argument('--debug', default=False, type=bool, const=True, metavar="BOOL", nargs="?",
                        help="Enable console debugging (default: False)")
    parser.add_argument('--release-update', default=False, type=bool, const=True, metavar="BOOL", nargs="?",
                        help="Enable file based updater (default: False)")
    parser.add_argument('--dev', default=False, type=bool, const=True, metavar="BOOL", nargs="?",
                        help="Enable developer mode (default: False)")
    parser.add_argument('--no-tasks', default=False, type=bool, const=True, metavar="BOOL", nargs="?",
                        help="Disable all tasks (default: False)")

    return parser.parse_args()


args = get_args()
if no_update:
    args.no_update = True