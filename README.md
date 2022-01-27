# psychescape_price_fetcher

This is a simple poe.ninja price fetcher with JSON's, that I am doing for practical and learning purposes at APIs + datas. Icons folder has 1.200 icons that I fetched alongside with prices that can be used for OCR in the future.

Current features: (  Additional informations are also fetched if necessary on processes. )

1 - Fetch current prices from poe.ninja

2 - Download item icons for detailed OCR search. (Icons are downloaded while fetching, if exists skipping all.)

3 - Search item values from names

options:
```
  options:
  -h, --help            show this help message and exit
  -fa, --fetchall       Fetch everything listed on poe.ninja
  -search, --search     Search the item on values folder
  -general, --general   Fetch all general values
  -crafting, --crafting Fetch all crafting values
  -unique, --unique     Fetch all unique item values
  -scarab, --scarab     Fetch scarab prices
  -sg, --skillgem       Fetch skill gem prices

```

Crafting and general is done, need to implement cluster jewel to unique items section, then I will implement the Atlas currencies. Data is the always longest and most boring section ever.

When I finish working with poe.ninja, I will work with PoE's PSApi (Public Stash) but I am waiting for OAuth key for 4-5 days. They are giving me time to finish poe.ninja I assume lol.

Also, university sucks.
  
 
[![Psychescape](https://img.youtube.com/vi/b7JSv-36m68/0.jpg)](https://www.youtube.com/watch?v=b7JSv-36m68)
