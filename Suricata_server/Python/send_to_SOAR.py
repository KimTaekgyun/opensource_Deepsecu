import json
import requests
import time
import os

# 설정
input_path = "/var/log/suricata/eve.json"  # Suricata 로그 파일 경로
soar_url = "http://local:5045"  # Logstash or Shuffle Webhook 주소
headers = {
    "Content-Type": "application/json"
}

def follow(file):
    """파일 끝에서부터 실시간 읽기 (tail -f)"""
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line.strip()

def send_to_soar():
    print("Suricata → SOAR 로그 포워딩 시작...")

    try:
        with open(input_path, 'r') as f:
            log_lines = follow(f)
            for line in log_lines:
                try:
                    data = json.loads(line)

                    # event_type이 "alert"일 때만 전송
                    if data.get("event_type") == "alert":
                        response = requests.post(soar_url, headers=headers, json=data, timeout=5)
                        print(f"[전송 완료] {response.status_code} - {response.text}")

                except json.JSONDecodeError:
                    print("JSON 파싱 실패 - 생략된 라인")
                    continue
                except Exception as e:
                    print(f"전송 중 오류 발생: {e}")
                    continue

    except FileNotFoundError:
        print(f"로그 파일을 찾을 수 없습니다: {input_path}")
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")

if __name__ == "__main__":
    send_to_soar()
