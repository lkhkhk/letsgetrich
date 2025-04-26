import os
from dotenv import load_dotenv

def load_environment_variables():
    """환경 변수를 로드하고 필수 변수가 설정되어 있는지 확인합니다."""
    load_dotenv(encoding='utf-8')
    
    required_vars = ["TELEGRAM_TOKEN", "NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET", "PPLX_API_KEY"]
    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            raise ValueError(f"{var}가 .env 파일에 정의되지 않았습니다.")
    return {var: os.getenv(var) for var in required_vars}

def log_error(message):
    """오류 메시지를 로그로 기록합니다."""
    print(f"오류: {message}")
