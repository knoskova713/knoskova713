import requests
import time

def check_token(token_address):
    url = f"https://api.dexscreener.com/latest/dex/pairs/ethereum/{token_address}"
    r = requests.get(url)
    data = r.json()
    
    try:
        pair = data['pair']
        liquidity_usd = float(pair['liquidity']['usd'])
        volume_usd = float(pair['volume']['h24'])
        price_change = float(pair['priceChange']['h24'])

        if liquidity_usd < 1000 or price_change < -80:
            print(f"🚨 Rug alert for {token_address} | Liquidity: ${liquidity_usd} | 24h change: {price_change}%")
        else:
            print(f"✅ {token_address} seems fine. Liquidity: ${liquidity_usd}, Change: {price_change}%")
    except:
        print(f"❌ Failed to parse token data for {token_address}")

def main():
    tokens = [
        "0x123...",  # Вставь сюда токены
        "0x456..."
    ]
    for token in tokens:
        check_token(token)
        time.sleep(3)

if __name__ == "__main__":
    main()
