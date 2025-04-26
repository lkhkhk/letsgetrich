from telegram import Update
from telegram.ext import ContextTypes
from stock import get_stock_code, get_news_list, get_stock_price, KOREAN_STOCKS
from news import summarize_with_pplx, predict_with_pplx

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("안녕하세요! 종목명을 입력하시면 최신 뉴스 요약과 주가 예측을 알려드립니다.\n예시: 삼성전자 또는 005930")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    code = get_stock_code(query)
    if not code:
        await update.message.reply_text("종목명을 정확히 입력해주세요. (예: 삼성전자, 005930)")
        return

    await update.message.reply_text("정보를 수집하고 있습니다. 잠시만 기다려주세요...")

    stock_name = [k for k, v in KOREAN_STOCKS.items() if v == code]
    stock_name = stock_name[0] if stock_name else query

    news_list = get_news_list(stock_name)
    if not news_list:
        await update.message.reply_text("뉴스를 찾을 수 없습니다.")
        return

    news_summaries = []
    for news in news_list:
        summary = summarize_with_pplx(news['title'], news['link'])
        if summary != "요약 실패":
            news_summaries.append(summary)

    price = get_stock_price(code)
    if not price:
        await update.message.reply_text("주가 정보를 불러올 수 없습니다.")
        return

    prediction = predict_with_pplx(stock_name, news_summaries, price)

    msg = f"📈 [{stock_name} ({code})]\n\n"
    msg += "■ 최신 뉴스 요약\n"
    for i, summary in enumerate(news_summaries, 1):
        msg += f"{i}. {summary}\n"
    msg += f"\n■ 현재 주가: {price:,}원\n"
    msg += f"\n■ 주가 예측(참고용):\n{prediction}"

    await update.message.reply_text(msg)
