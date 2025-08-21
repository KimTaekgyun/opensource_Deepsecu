# opensource_Deepsecu

# 자동화 기반 침입 탐지 및 대응 시스템

Suricata IDS와 Python을 활용한 보안 자동화 시스템  
실시간 네트워크 트래픽 탐지, 로그 처리, 경고 전송까지 통합 대응

---

## 개요

이 프로젝트는 오픈소스 IDS인 **Suricata**와 **Python 기반의 자동화 스크립트**,  
그리고 **ELK(Elasticsearch, Logstash, Kibana)** 및 **ElastAlert2**를 연동하여,  
**침입 탐지부터 로그 분류, 시각화, 경고 전송까지 전 과정을 자동화**한 경량 보안 시스템입니다.

운영자의 개입 없이 실시간 위협 탐지 → 저장 → 경고까지 처리할 수 있으며,  
중소규모 인프라나 교육 환경에서도 손쉽게 적용할 수 있도록 경량 구조로 설계되었습니다.

---

## 개발 환경

- **운영체제**: Ubuntu 22.04 Desktop (서버 2대 구성)
- **프로그래밍 언어**: Python 
- **보안 탐지 도구**: Suricata 6.x
- **로그 처리/시각화**: Logstash, Filebeat, Elasticsearch, Kibana (ELK Stack 7.17.18)
- **경고 알림**: ElastAlert2
- **알림 채널**: Email, Slack (선택)

---

## 시스템 아키텍처

### 백엔드 구조도


