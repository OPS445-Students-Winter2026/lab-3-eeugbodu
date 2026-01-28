#!/usr/bin/env python3
# Author ID: 153259239

import subprocess

def free_space():
    process = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        shell=True
    )
    output = process.communicate()[0]
    return output.decode('utf-8').strip()


if __name__ == '__main__':
    print(free_space())
