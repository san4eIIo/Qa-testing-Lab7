import pytest
import paramiko
import subprocess
import time
from parser import parse

server_ip = "10.0.2.5"
username = "saniok"
password = "SASHA2002naumchuk"

@pytest.fixture(scope="function")
def server():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, username=username, password=password)

    start_iperf_command = "iperf -s"
    _, stdout, stderr = client.exec_command(start_iperf_command)

    time.sleep(5)

    yield stderr.read().decode('utf-8')

    stop_iperf_command = "killall iperf"
    client.exec_command(stop_iperf_command)

    client.close()

@pytest.fixture(scope="function")
def client(server):
    server_ip = "10.0.2.5"

    iperf_command = f"iperf -c {server_ip}"
    result = subprocess.run(iperf_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    yield result.stdout, result.stderr
