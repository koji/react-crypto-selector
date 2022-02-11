export type SelectMenuOption = {
  name: string;
  symbol: string;
  logo: string;
};

export type CryptoCurrencySelectorProps = {
  id: string;
  open: boolean;
  onToggle: () => void;
  onChange: (symbol: string) => void;
  selectedValue: SelectMenuOption;
};
