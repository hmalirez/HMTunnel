import json
import os
import struct
import uuid
from pathlib import Path

# لینک‌های سابسکریپشن خود را وارد کنید
subscriptions = [
    {"remarks": "My Config 1", "url": "https://raw.githubusercontent.com/hmalirez/Page/refs/heads/main/iran1.txt"},
    {"remarks": "My Config 2", "url": "https://raw.githubusercontent.com/hmalirez/Page/refs/heads/main/iran2.txt"},
    {"remarks": "My Config 3", "url": "https://raw.githubusercontent.com/hmalirez/Page/refs/heads/main/iran3.txt"}
]

repo_root = Path(__file__).resolve().parent
output_path = repo_root / "V2rayNG/app/src/main/assets/mmkv/SUB"
os.makedirs(output_path.parent, exist_ok=True)

with open(output_path, "wb") as f:
    for sub in subscriptions:
        guid = uuid.uuid4().hex
        data = {
            "remarks": sub["remarks"],
            "url": sub["url"],
            "enabled": True,
            "addedTime": 1775813540349,
            "lastUpdated": -1,
            "autoUpdate": True,
            "filter": "",
            "allowInsecureUrl": False,
            "userAgent": ""
        }
        json_str = json.dumps(data, separators=(',', ':'))
        key_bytes = guid.encode('utf-8')
        value_bytes = json_str.encode('utf-8')
        f.write(struct.pack('>i', len(key_bytes)))
        f.write(key_bytes)
        f.write(struct.pack('>i', len(value_bytes)))
        f.write(value_bytes)

print(f"✅ SUB file created successfully at: {output_path}")
