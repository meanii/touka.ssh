import subprocess


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Building the command. Ex: "ping -c 1 google.com"
    command = ["ping", "-c", "1", host, "-W", "2"]

    return subprocess.call(args=command, stdout=subprocess.PIPE) == 0
