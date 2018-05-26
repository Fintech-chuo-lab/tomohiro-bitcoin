/env
while True:
    import requests
    from bs4 import BeautifulSoup

    target_url = "https://bitflyer.jp/?bf=hhbmzc42"
    r = requests.get(target_url)

    soup = BeautifulSoup(r.text,"html.parser")

    buy_price = soup.select_one("#bfPriceAsk_1").string
    sell_price = soup.select_one("#bfPriceBid_1").string

    print(buy_price)
    print(sell_price)

