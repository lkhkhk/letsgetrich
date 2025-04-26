# LetsGetRich

이 프로젝트는 한국 주식에 대한 최신 뉴스 요약 및 주가 예측을 제공하는 Telegram 봇입니다.

## 기능

- 주식 종목에 대한 최신 뉴스 검색 및 요약
- 주가 예측 기능
- Telegram 봇을 통한 사용자 인터페이스

## 프로젝트 구조

```
LetsGetRich/
│
├── bot/
│   ├── __init__.py
│   ├── main.py          # 메인 봇 실행 파일
│   ├── handlers.py      # 핸들러 함수들
│   ├── utils.py         # 유틸리티 함수들
│   ├── stock.py         # 주식 관련 기능
│   └── news.py          # 뉴스 관련 기능
│
├── .env                 # 환경 변수 파일
├── .gitignore           # Git 무시 파일
└── .cursorignore        # Cursor 무시 파일
```

## 설치 방법

1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/yourusername/LetsGetRich.git
   cd LetsGetRich
   ```

2. 가상환경을 생성하고 활성화합니다:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

4. `.env` 파일을 생성하고 다음과 같은 내용을 추가합니다:
   ```plaintext
   TELEGRAM_TOKEN=your_telegram_bot_token
   NAVER_CLIENT_ID=your_naver_client_id
   NAVER_CLIENT_SECRET=your_naver_client_secret
   PPLX_API_KEY=your_perplexity_api_key
   ```

## 봇 시작 방법

1. `main.py` 파일을 실행하여 봇을 시작합니다:
   ```bash
   python bot/main.py
   ```

2. Telegram에서 봇을 찾아 메시지를 보내면 주식 뉴스 요약 및 예측을 받을 수 있습니다.

## 기여

기여를 원하시면 이 저장소를 포크하고 Pull Request를 제출해 주세요.

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.


# 참고

### git 초기화
```pwsh
git init

git branch -M main

git add .
git commit -m "init"

# GitHub 사이트에서 원격저장소를 먼저 만들어야 한다.
# git remote add origin https://github.com/[사용자ID]/[저장소명].git

# 처음 push 할 때만 [-u]를 사용
git push -u origin main

# git push
```

### Windows 포트 사용 프로세스 찾아서 죽이기

```pwsh
# 포트 사용 프로세스 찾기
netstat -ano | findstr [PORT-NO]

# 프로세스 죽이기
taskkill -f /pid [PROCESS-ID]
```