# react-crypto-selector
cryptocurrency selector for reactjs

https://user-images.githubusercontent.com/474225/153540514-7b340865-a98d-4d76-ad54-9219ef0e3cde.mov

This repo is using [react-country-selector)](https://github.com/driaug/react-country-selector)

In terms of crypto data, I used [cryptocompare](https://github.com/lagerfeuer/cryptocompare).
Just picked a couple of items such as name, symbol and logoUrl.

## How to update the list
run python script, generate_list.py and copy and paste from `coinslistjson` into `cryptocurrencies.ts`

```zsh
$ pip install cryptocompare
$ python generate_list.py
```

The python script isn't really good so need a couple of manual operation to use crypto data as a constant typescript file.  
1. remove double quotations from the json file
2. need to add `\` for cryptocurrencies that are using a single quotation for a name.

## How to run example project
```zsh
$ cd example
$ yarn
$ yarn dev
```
Then open localhost:3000
