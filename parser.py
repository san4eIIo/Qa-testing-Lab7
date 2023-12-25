import re

def parse(output):
    match = re.search(r'(\d+\.\d+)\s+[KMG]bits/sec', output)
    if match:
        return float(match.group(1))
    else:
        raise ValueError("Output Error")
