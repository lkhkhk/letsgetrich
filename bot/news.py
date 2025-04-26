import requests
import os
from dotenv import load_dotenv

load_dotenv()

PPLX_API_KEY = os.getenv("PPLX_API_KEY")

def summarize_with_pplx(news_title, news_url):
    prompt = f"다음 뉴스를 한 문장으로 요약해주세요:\n제목: {news_title}\n링크: {news_url}"

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PPLX_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes news articles in Korean."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()
        response_data = res.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content'].strip()
        return "요약 실패"
    except Exception as e:
        print(f"뉴스 요약 오류: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"응답 내용: {e.response.text}")
        return "요약 실패"

def predict_with_pplx(stock_name, news_summaries, price):
    prompt = (
        f"종목명: {stock_name}\n"
        f"현재 주가: {price}원\n"
        f"최근 뉴스 요약:\n" +
        "\n".join(f"{i+1}. {summary}" for i, summary in enumerate(news_summaries)) +
        "\n\n위 정보를 바탕으로 앞으로 1주일 이내 주가가 상승할지, 하락할지, 또는 횡보할지 간단히 예측해주세요. (투자 조언 아님, 참고용)" +
        "\n\n마크다운 형식으로 답변해주세요."
    )
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PPLX_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that analyzes stock market trends in Korean."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()
        response_data = res.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content'].strip()
        return "예측 실패"
    except Exception as e:
        print(f"주가 예측 오류: {e}")
        return "예측 실패"
