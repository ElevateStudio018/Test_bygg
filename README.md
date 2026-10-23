# Ullevi El – webbplats

Webbplats för **Ullevi El & Svagströmsmontage AB** (Landvetter). Ren HTML, CSS och JavaScript – inga beroenden.

## Struktur

- `tools/build.py` – genererar alla sidor (gemensam header/footer, relativa länkar). **Redigera innehållet här** och kör:
  ```sh
  python3 tools/build.py
  ```
- `index.html`, `tjanster/…`, `om-oss/…`, `hemmafixare/`, `kontakt/`, `integritetspolicy/`, `404.html` – genererade sidor
- `css/style.css` – design och komponenter
- `js/main.js` – megameny, mobilmeny och offertformulär (öppnar ett ifyllt mejl)
- `assets/img/` – foton från [Pexels](https://www.pexels.com/license/) (fri licens)
- `test-demo/` – tidigare demo (återskapad byggföretagssida)

## Kör lokalt

```sh
python3 -m http.server 8000
# öppna http://localhost:8000
```

## Källor för företagsuppgifter

Företagets egen webbplats (ulleviel.se) var inte nåbar vid bygget, så uppgifterna kommer från offentliga kataloger: Allabolag, Byggkatalogen, Dorunner (behörigheter enligt Elsäkerhetsverket), Svenska Hantverkare, Eniro och Facebook. Texterna är nyskrivna utifrån dessa uppgifter och bör granskas av företaget.
