import json
import time
import os
from datetime import datetime

# 설정
INPUT_LOG_PATH = "/home/computer/AI_Model/suricata-log.json"
OUTPUT_LOG_PATH = "/home/computer/AI_Model/final.json"

# 악성 시그니처 키워드
MALICIOUS_KEYWORDS = [
    "trojan", "exploit", "sql injection", "ransomware", "xss",
    "brute force", "ddos", "malware", "scan", "botnet"
]

def classify_label(alert_signature):
    if not alert_signature:
        return "Begin"
    lower_sig = alert_signature.lower()
    for keyword in MALICIOUS_KEYWORDS:
        if keyword in lower_sig:
            return f"Malicious-{keyword.replace(' ', '_')}"
    return "Begin"

def follow(file):
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def process_log():
    with open(INPUT_LOG_PATH, 'r') as f_in:
        log_lines = follow(f_in)
        for line in log_lines:
            try:
                data = json.loads(line)
                signature = data.get("alert", {}).get("signature", "")
                label = classify_label(signature)

                data["@timestamp"] = datetime.utcnow().isoformat() + "Z"
                data["label"] = label

                with open(OUTPUT_LOG_PATH, 'a') as f_out:
                    f_out.write(json.dumps(data) + '\n')

                print(f"[SAVED] {label} - {signature}")

            except json.JSONDecodeError:
                print("JSON Decode 오류 - 생략된 라인")
            except Exception as e:
                print(f"오류 발생: {e}")

if __name__ == "__main__":
    print("suricata-log.json 파일을 실시간 처리하여 final.json에 저장 중...")
    process_log()

