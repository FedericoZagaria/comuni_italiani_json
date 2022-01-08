# comuni_italiani_json
Elenco codici comuni italiani
=============================

### [`codici_comuni_italiani.json`](https://github.com/FedericoZagaria/comuni_italiani_json/blob/main/codici_comuni_italiani.json) è il file JSON contenente l'elenco dei 7904 comuni italiani con i relativi codici.


Ogni comune è un oggetto JSON con le seguenti proprietà:
* `nr` indice che conta i 7904 comuni 
* `descrizione comune` nome del comune
* `sigla` provincia 
* `codice elettorale` codice elettorale
* `codice istat` codice istat
* `codice Belfiore` codice nazionale
```json
{
        "nr": "1",
        "descrizione comune": "ABANO TERME",
        "sigla": "PD",
        "codice elettorale": "1050540010",
        "codice istat": "028001",
        "codice Belfiore": "A001"
 },
```

### [`html_to_json.py`](https://github.com/FedericoZagaria/comuni_italiani_json/blob/main/html_to_json.py) è il programma con cui ho estratto i codici dalla [pagina web](https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php) del ministero

**!!!** ho dovuto commentare l'intestazione della tabella nella pagina HTML per evitare errori con il parser dovuti all'indentazione della stessa

```html
<!-- 
<thead>
      <tr>
        <th>NR.</th>
        <th>DESCRIZIONE COMUNE</th>
        <th>SIGLA</th>
        <th>CODICE ELETTORALE</th>
        <th>CODICE ISTAT</th>
        <th>CODICE BELFIORE</th>
      </tr>
</thead>
-->
```
