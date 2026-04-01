from fastapi import FastAPI, Request, HTTPException
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal

# 作成済みの設定クラスをインポート
from src.config.settings import settings 

load_dotenv()
app = FastAPI()

# Webhookのデータ構造を定義（rikuさんの仕様案を反映）
class TradingSignal(BaseModel):
    secret: str
    ticker: str
    action: Literal["buy", "sell"] 
    qty: int 
    strategy: str
    price: float
    timestamp: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/webhook")
async def receive_webhook(signal: TradingSignal):
    # 1. settings.py から読み込んだ合言葉でチェック
    if signal.secret != settings.webhook_secret:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # 2. 受信成功のログ出力
    print(f"Validated Signal: {signal.ticker} {signal.action} {signal.qty} shares")
    
    # 3. rikuさんへのレスポンス
    return {
        "status": "validated", 
        "ticker": signal.ticker,
        "strategy": signal.strategy
    }