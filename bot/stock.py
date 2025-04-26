import requests
import os
from dotenv import load_dotenv

load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

KOREAN_STOCKS = {
    '삼성전자': '005930',
    'SK하이닉스': '000660',
    'LG에너지솔루션': '373220',
    'NAVER': '035420',
    '카카오': '035720',
    'HD현대중공업': '329180',
    '현대로템': '064350',
    '한화오션': '042660',
    '한화에어로스페이스': '012450'
}

def get_stock_code(query):
    if query.isdigit() and len(query) == 6:
        return query
    return KOREAN_STOCKS.get(query.strip())

def get_news_list(stock_name, display=3):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {
        "query": stock_name,
        "display": display,
        "sort": "date"
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        items = res.json().get('items', [])
        return [{'title': item['title'], 'link': item['link']} for item in items]
    except Exception as e:
        print(f"뉴스 검색 오류: {e}")
        return []

def get_stock_price(stock_code):
    url = f"https://finance.naver.com/item/main.nhn?code={stock_code}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(res.text, 'html.parser')
        price_element = soup.select_one('p.no_today span.blind')
        if price_element:
            price = price_element.text.replace(',', '')
            return int(price)
    except Exception as e:
        print(f"주가 조회 오류: {e}")
    return None
