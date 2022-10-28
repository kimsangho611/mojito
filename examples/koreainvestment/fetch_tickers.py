# 주식잔고조회
import mojito
import pprint

with open("../../koreainvestment.key") as f:
    lines = f.readlines()

key = lines[0].strip()
secret = lines[1].strip()

broker = mojito.KoreaInvestment(
    api_key = key,
    api_secret = secret,
    acc_no = "63398082"
)

# fetch_tickers
tickers = broker.fetch_tickers()
cond = tickers['그룹코드'] == 'ST'
print(tickers[cond])
#tickers.to_excel("korea_code.xlsx", index=False)
