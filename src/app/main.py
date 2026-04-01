from fastapi import FastAPI, Request, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# 簡易的な認証用シークレット
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    
    # 1. セキュリティチェック
    if payload.get("secret") != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # 2. 受信ログの表示（まずはこれが見えれば成功）
    print(f"Signal Received: {payload}")
    
    return {"status": "success", "message": "Signal logged"}