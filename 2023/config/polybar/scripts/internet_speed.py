#!/usr/bin/env python3

import subprocess
import re

def get_speed():
    cmd_output = subprocess.check_output(["speedtest-cli", "--simple"]).decode()
    
    ping_match = re.search("Ping:\s(.*?)\s", cmd_output)
    if ping_match:
        ping = ping_match.group(1)
    else:
        ping = "N/A"
    
    download_match = re.search("Download:\s(.*?)\s", cmd_output)
    if download_match:
        download = download_match.group(1)
    else:
        download = "N/A"
    
    upload_match = re.search("Upload:\s(.*?)\s", cmd_output)
    if upload_match:
        upload = upload_match.group(1)
    else:
        upload = "N/A"
    
    return {"ping": ping, "download": download, "upload": upload}

if __name__ == "__main__":
    speed = get_speed()
    print(f"           {speed['ping']} |  {speed['download']} |  {speed['upload']}")