import cryptocompare
import json

IMG_URL = 'https://www.cryptocompare.com'

top_list = [
"BTC",
"ETH",
"USDT",
"BNB",
"USDC",
"XRP",
"ADA",
"SOL",
"AVAX",
"LUNA",
"DOT",
"DOGE",
"BUSD",
"SHIB",
"MATIC",
"CRO",
"WBTC",
"UST",
"DAI",
"LTC",
"ATOM",
"LINK",
"NEAR",
"UNI",
"TRX",
"BCH",
"ALGO",
"FTT",
"MANA",
"LEO",
"XLM",
"FTM",
"ETC",
"SAND",
"BTCB",
"HBAR",
"ICP",
"THETA",
"VET",
"AXS",
"EGLD",
"XTZ",
"FIL",
"HNT",
"XMR",
"KLAY",
"MIOTA",
"EOS",
"FLOW",
"ONE",
"AAVE",
"GALA",
"GRT",
"CAKE",
"STX",
"BTT",
"MKR",
"BSV",
"XEC",
"ZEC",
"QNT",
"NEO",
"ENJ",
"KCS",
"HT",
"KSM",
"KDA",
"RUNE",
"TUSD",
"CRV",
"LRC",
"CHZ",
"BAT",
"OKB",
"CELO",
"CVX",
"AMP",
"ROSE",
"DASH",
"AR",
"TFUEL",
"NEXO",
"WAVES",
"IOTX",
"MINA",
"XEM",
"SCRT",
"XYM",
"HOT",
"USDP",
"DCR",
"BORA",
"YFI",
"COMP",
"1INCH",
"CEL",
"XDC",
"RVN",
"LPT",
"AUDIO"
] # This was on 2/10/2022

# This will get cryptocurrencies that are on top_list
def get_topcrypto_list():
    coins = cryptocompare.get_coin_list(format=False)
    output_str = []
    for c in top_list:
        name = coins[c]["CoinName"]
        symbol = coins[c]["Symbol"]
        try:
            logo = IMG_URL + coins[c]['ImageUrl']
        except KeyError:
            logo = 'dummy'
            continue

        output_format = "{" + "name: '{}', symbol: '{}', logo: '{}'".format(name, symbol, logo) + "}"
        output_str.append(output_format)

    with open('top_coinslistjson', 'w') as f:
        json.dump(output_str, f, ensure_ascii=False)


# This will get more than 7000 cryptocurrencies
def get_crypto_list():
    coins = cryptocompare.get_coin_list(format=False)
    output_str = []
    for coin in coins.values():
        symbol = coin['Symbol']
        name = coin['CoinName']
        try:
            logo = IMG_URL+coin['ImageUrl']
        except KeyError:
            logo = 'dummy'
            continue
        output_format = "{" + "name: '{}', symbol: '{}', logo: '{}'".format(name, symbol, logo) + "}"
        output_str.append(output_format)

    with open('coinslistjson', 'w') as f:
        json.dump(output_str, f, ensure_ascii=False)


if __name__ == "__main__":
    # get_crypto_list()
    get_topcrypto_list()