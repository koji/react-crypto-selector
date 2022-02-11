import React, { useState } from "react";
import { SelectMenuOption } from "../types/types";
import { CryptoCurrencySelector } from "../components/selector";
import { CryptoCurrencies } from "../constants/cryptocurrencies";

export default function Home() {
  const myRef = React.createRef<HTMLDivElement>();

  const [isOpen, setIsOpen] = useState(false);
  // Default this to a country's code to preselect it
  const [crypto, setCrypto] = useState("BTC");

  return (
    <div
      className={"w-screen h-screen flex flex-col justify-center items-center"}
    >
      <div className={"w-96 px-5 mt-auto"}>
        <label className="block text-sm font-medium text-gray-700">
          Select a cryptocurrency
        </label>
        <CryptoCurrencySelector
          id={"cryptocurrencies"}
          ref={myRef}
          open={isOpen}
          onToggle={() => setIsOpen(!isOpen)}
          onChange={(val) => setCrypto(val)}
          selectedValue={
            CryptoCurrencies.find(
              (option) => option.symbol === crypto
            ) as SelectMenuOption
          }
        />
      </div>
      <footer className={"mt-auto pb-2"}>
        <a
          className={
            "text-gray-500 hover:text-gray-800 cursor-pointer transition mx-2"
          }
          href={"https://github.com/driaug/react-country-selector"}
          target={"_blank"}
        >
          Github
        </a>
        <a
          className={
            "text-gray-500 hover:text-gray-800 cursor-pointer transition mx-2"
          }
          href={"https://twitter.com/driaug_"}
          target={"_blank"}
        >
          Twitter
        </a>
        <br />
        <a
          className={
            "text-gray-500 hover:text-gray-800 cursor-pointer transition mx-2"
          }
          href={"https://github.com/koji/react-crypto-selector"}
          target={"_blank"}
        >
          Github
        </a>
        <a
          className={
            "text-gray-500 hover:text-gray-800 cursor-pointer transition mx-2"
          }
          href={"https://twitter.com/0xkoji"}
          target={"_blank"}
        >
          Twitter
        </a>
      </footer>
    </div>
  );
}
