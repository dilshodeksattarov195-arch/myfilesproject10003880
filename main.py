import sys
import json

def run_backend_sync():
    data = {"node": 8849, "status": "online"}
    print(f"Syncing node data: {json.dumps(data)}")

if __name__ == '__main__':
    run_backend_sync()