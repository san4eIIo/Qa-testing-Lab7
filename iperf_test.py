import pytest
from parser import parse

class TestSuite:
    def test_iperf3_client_connection(self, client):
        stdout, stderr = client

        print(f"Result:\n{stdout}")
        if stderr is not "":
            print(f"Error:\n{stderr}")

        assert stderr == '', f"iperf error: {stderr}"
        #print("block")
        transfer_speed = parse(stdout)
        #print("Parce works")
        if transfer_speed > 2:
            print(f"Success transfer speed is more than 2GB/s and is {transfer_speed} GBits/sesc")
        else:
            print(f"Transfer speed is lower than 2 Gb/s and is{transfer_speed}")
        assert transfer_speed > 1.5, f"Invalid iperf transfer speed: {transfer_speed}"

