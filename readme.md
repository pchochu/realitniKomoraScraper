## Program

Scrapovanie informacii o makleroch z realitnikomora.cz

## Pouzitie

```
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
scrapy crawl realitni_komora --nolog
```

## Vystup

Nachadza sa v subore realitaci.json  
Nejedna sa o JSON, ide o slovniky vypisane pod seba  
Pre zmenu je potrebna pridat na koniec kazdeho riadku ,(ciarku)  
a obalit cely obsah suboru do hranatych zatvoriek
