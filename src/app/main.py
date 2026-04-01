from fastapi import FastAPI, Request, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# 簡易的な認証用シークレット
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

# src/app/main.py

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    print(f"DEBUG: Received payload: {payload}") # これが出るか確認
    
    # client = AlpacaClient() # ← キーがない間はコメントアウト
    # client.submit_order(...) # ← 同上
    
    return {"status": "success"}