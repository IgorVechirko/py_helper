import sys
import os


def res_path():
    exe_folder = sys.argv[0]

    while os.path.split(exe_folder)[1] != "src":
        exe_folder = os.path.split(exe_folder)[0]
    else:
        exe_folder = os.path.split(exe_folder)[0]

    return os.path.join(exe_folder, "res")
