#!/usr/bin/env python3
"""Genererar Ullevi El-sajten: python3 tools/build.py

Varje sida definieras i PAGES nedan. Header och footer är gemensamma och alla
länkar görs relativa så att sajten fungerar både lokalt och på GitHub Pages.
Skriv länkar i innehållet som "@/sökväg/" så räknas de om per sida.
"""
import hashlib
from pathlib import Path

# Elevate Studio's credit under every footer: the mark and the name, the whole of it one link to elevatestudio.nu.
ELEVATE_CREDIT = '''<!-- elevate-credit -->
<style>.elevate-credit{max-width:1240px;margin:24px auto 0;padding:20px 16px 0;border-top:1px solid rgba(128,128,128,.25);display:flex;justify-content:center;box-sizing:border-box}.elevate-credit a{display:inline-flex;align-items:center;gap:8px;padding:8px 0;font:inherit;font-size:13px;line-height:1;color:inherit;opacity:.55;text-decoration:none;transition:opacity .2s}.elevate-credit a:hover,.elevate-credit a:focus-visible{opacity:1}.elevate-credit svg{width:16px;height:16px;flex:none;display:block}@media(min-width:1024px){.elevate-credit a{font-size:14px}}</style>
<div class="elevate-credit"><a href="https://elevatestudio.nu" target="_blank" rel="noopener"><svg viewBox="0 0 1884.3 1353.9" aria-hidden="true"><path d="M0.0 1353.9 L1218.7 0.0 L1218.7 329.1 L479.7 1136.4 L786.7 1132.4 L1215.5 687.4 L1884.3 1349.9 L1590.1 1349.9 L1218.6 994.7 L865.4 1349.9Z" fill="currentColor"/></svg>Byggd av Elevate Studio</a></div>
'''


ROOT = Path(__file__).resolve().parent.parent


def asset_version(rel):
    """Kort hash av filens innehåll – tvingar webbläsaren att hämta nya CSS/JS efter ändringar."""
    return hashlib.sha1((ROOT / rel).read_bytes()).hexdigest()[:8]

COMPANY = "Ullevi El & Svagströmsmontage AB"
PHONE = "073-364 51 00"
PHONE_HREF = "tel:+46733645100"
EMAIL = "info@ulleviel.se"
ADDRESS = ("Hagliden 15", "438 91 Landvetter")
ORGNR = "556776-3411"
AREAS = ["Göteborg", "Mölndal", "Härryda", "Landvetter", "Partille", "Lerum",
         "Kungsbacka", "Alingsås", "Borås", "Kungälv", "Bollebygd"]

SERVICES = [
    ("tjanster/elinstallation/", "Elinstallation", "elektriker-elcentral"),
    ("tjanster/svagstrom/", "Svagström", "natverk-kablar"),
    ("tjanster/belysning/", "Belysning", "kok-ljust"),
    ("tjanster/badrumsrenovering/", "Badrumsrenovering", "badrum-marmor"),
    ("tjanster/kok-och-vvs/", "Kök, VVS & renovering", "kok-morkt"),
    ("tjanster/solceller/", "Solceller & elproduktion", "solceller-tak"),
]

WORDMARK = '<span class="wordmark">ULLEVI<span class="color-primary">EL</span></span>'


def header():
    svc = "\n".join(f'                <li><a href="@/{p}">{t}</a></li>' for p, t, _ in SERVICES)
    return f'''<header class="site-header" id="top">
  <nav class="menu" aria-label="Huvudmeny">
    <ul class="menu-list">
      <li class="menu-item" data-menu>
        <button class="menu-toggle" aria-expanded="false">Tjänster</button>
        <div class="submenu">
          <div class="submenu-inner">
            <div class="submenu-col wide">
              <p class="submenu-title">Våra tjänster</p>
              <ul class="link-list-lg">
{svc}
              </ul>
            </div>
            <div class="submenu-col">
              <a href="@/tjanster/" class="card card-navy">Alla tjänster</a>
            </div>
            <div class="submenu-col">
              <a href="@/kontakt/#offert" class="card card-img"><img src="@/assets/img/elektriker-skap.webp" alt="" loading="lazy"><span>Begär offert</span></a>
            </div>
          </div>
        </div>
      </li>
      <li class="menu-item" data-menu>
        <button class="menu-toggle" aria-expanded="false">Om oss</button>
        <div class="submenu">
          <div class="submenu-inner">
            <div class="submenu-col wide">
              <p class="submenu-title">Om Ullevi El</p>
              <ul class="link-list-lg">
                <li><a href="@/om-oss/">Vilka vi är</a></li>
                <li><a href="@/om-oss/behorigheter/">Behörigheter &amp; certifikat</a></li>
                <li><a href="@/om-oss/arbetsomrade/">Arbetsområde</a></li>
                <li><a href="@/hemmafixare/">För hemmafixare</a></li>
              </ul>
            </div>
            <div class="submenu-col wide">
              <a href="@/om-oss/" class="card card-img"><img src="@/assets/img/elektriker-hjalm.webp" alt="" loading="lazy"><span>Vilka vi är</span></a>
            </div>
          </div>
        </div>
      </li>
      <li class="menu-item" data-menu>
        <button class="menu-toggle" aria-expanded="false">Kontakt</button>
        <div class="submenu">
          <div class="submenu-inner">
            <div class="submenu-col">
              <p class="submenu-title">Kontakt</p>
              <ul class="link-list">
                <li><a href="@/kontakt/">Kontakta oss</a></li>
                <li><a href="@/kontakt/#offert">Begär offert</a></li>
                <li><a href="{PHONE_HREF}">Ring {PHONE}</a></li>
                <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
              </ul>
              <p class="submenu-title">Besöksadress</p>
              <p>{ADDRESS[0]}<br>{ADDRESS[1]}</p>
            </div>
            <div class="submenu-col">
              <a href="@/kontakt/#offert" class="card card-navy">Offert utan att behöva vänta</a>
            </div>
            <div class="submenu-col">
              <a href="@/om-oss/arbetsomrade/" class="card card-img"><img src="@/assets/img/solceller-tak.webp" alt="" loading="lazy"><span>Arbetsområde</span></a>
            </div>
          </div>
        </div>
      </li>
      <li class="menu-item"><a href="{PHONE_HREF}" class="menu-search menu-phone">{PHONE}</a></li>
    </ul>
  </nav>

  <a href="@/" class="logo" aria-label="Ullevi El – till startsidan">{WORDMARK}</a>

  <button class="menu-btn" aria-label="Öppna menyn" aria-expanded="false"><span></span><span></span><span></span></button>
</header>'''


def footer():
    svc = "\n".join(f'        <li><a href="@/{p}">{t}</a></li>' for p, t, _ in SERVICES)
    areas = "\n".join(f"        <li>{a}</li>" for a in AREAS)
    return f'''<footer class="site-footer bg-dark">
  <div class="container footer-grid">
    <div>
      <p class="footer-title">Tjänster</p>
      <ul>
{svc}
      </ul>
    </div>
    <div>
      <p class="footer-title">Arbetsområde</p>
      <ul class="offices">
{areas}
      </ul>
    </div>
    <div>
      <p class="footer-title">Genvägar</p>
      <ul>
        <li><a href="@/om-oss/">Om oss</a></li>
        <li><a href="@/om-oss/behorigheter/">Behörigheter &amp; certifikat</a></li>
        <li><a href="@/hemmafixare/">För hemmafixare</a></li>
        <li><a href="@/kontakt/#offert">Begär offert</a></li>
        <li><a href="@/kontakt/">Kontakta oss</a></li>
        <li><a href="@/integritetspolicy/">Integritetspolicy</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-title">Kontakt</p>
      <ul>
        <li><a href="{PHONE_HREF}"><strong>{PHONE}</strong></a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ADDRESS[0]}<br>{ADDRESS[1]}</li>
        <li>Org.nr {ORGNR}</li>
      </ul>
      <ul class="cert-list">
        <li>Elsäkerhetsverket</li><li>Våtrumscertifikat</li><li>F-skatt</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <a href="@/" class="logo logo-footer" aria-label="Till startsidan">{WORDMARK}</a>
    <p class="copyright">Service och entreprenad av högsta kvalité – till rätt pris, i rätt tid. © <span id="year">2026</span> {COMPANY}</p>
  </div>
{ELEVATE_CREDIT}</footer>'''


def layout(title, description, body):
    return f'''<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#11243D">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="@/assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="@/css/style.css?v={asset_version('css/style.css')}">
</head>
<body>

{header()}

<main>
{body.strip()}
</main>

{footer()}

<script src="@/js/main.js?v={asset_version('js/main.js')}"></script>
</body>
</html>
'''


# ---------- Återanvändbara block ----------

def page_hero(h1, lead, eyebrow=None):
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    return f'''  <section class="hero page-hero bg-navy">
    <div class="container narrow">
      {eb}
      <h1>{h1}</h1>
      <p class="txt-lg">{lead}</p>
    </div>
  </section>'''


def wide_image(img, alt):
    return f'''  <section class="wide-img"><img src="@/assets/img/{img}.webp" alt="{alt}"></section>'''


def service_cards(exclude=None):
    cards = "\n".join(
        f'    <a href="@/{p}" class="card card-img"><img src="@/assets/img/{img}.webp" alt="" loading="lazy"><span>{t}</span></a>'
        for p, t, img in SERVICES if p != exclude)
    if exclude:
        cards += '\n    <a href="@/kontakt/#offert" class="card card-navy"><span>Begär offert</span></a>'
    return f'  <section class="container cards cards-3">\n{cards}\n  </section>'


def split(h2, text, img, alt, bg="bg-sand", reverse=False, button=None):
    btn = f'<p><a class="{button[2] if len(button) > 2 else "link"}" href="{button[1]}">{button[0]}</a></p>' if button else ""
    rev = " split-reverse" if reverse else ""
    text_html = f'''    <div class="split-text">
      <div>
        <h2>{h2}</h2>
        {text}
        {btn}
      </div>
    </div>'''
    img_html = f'    <div class="split-img"><img src="@/assets/img/{img}.webp" alt="{alt}" loading="lazy"></div>'
    inner = (img_html + "\n" + text_html) if reverse else (text_html + "\n" + img_html)
    return f'  <section class="split {bg}{rev}">\n{inner}\n  </section>'


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def cta():
    return f'''  <section class="cta-band bg-primary">
    <div class="container cta-inner">
      <h2>Offert utan att behöva vänta</h2>
      <p class="txt-lg">Berätta kort vad du behöver hjälp med så återkommer vi med ett prisförslag.</p>
      <p class="buttons">
        <a class="button-lg bg-navy" href="@/kontakt/#offert">Begär offert</a>
        <a class="button-lg bg-white" href="{PHONE_HREF}">Ring {PHONE}</a>
      </p>
    </div>
  </section>'''


def service_page(path, h1, lead, img, alt, intro_h2, intro, bullets, split_block, faq=None):
    faq_html = ""
    if faq:
        items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
        faq_html = f'''  <section class="container section faq">
    <h2>Vanliga frågor</h2>
    {items}
  </section>'''
    body = f'''{page_hero(h1, lead, "Tjänster")}
{wide_image(img, alt)}
  <section class="container section two-col">
    <div>
      <h2>{intro_h2}</h2>
      {intro}
      <p class="buttons"><a class="button-lg" href="@/kontakt/#offert">Begär offert</a></p>
    </div>
    <div>
      <p class="list-title">Det här hjälper vi till med</p>
      {checklist(bullets)}
    </div>
  </section>
{split_block}
{faq_html}
  <section class="container section-sm"><h2>Fler tjänster</h2></section>
{service_cards(exclude=path)}
{cta()}'''
    return body


# ---------- Sidor ----------

PAGES = {}

PAGES["index.html"] = ("Ullevi El – elektriker och svagström i Göteborg & Landvetter",
"Ullevi El & Svagströmsmontage AB i Landvetter utför elinstallationer, svagström, belysning och badrumsrenoveringar i Göteborg med omnejd.",
f'''  <section class="hero-image">
    <img class="cover" src="@/assets/img/elektriker-elcentral.webp" alt="Elektriker arbetar i en elcentral">
    <div class="container hero-image-content">
      <h1><span class="color-primary">Ullevi El installerar el och svagström med kvalité. </span>Till rätt pris, i rätt tid – i hem, företag och offentliga miljöer.</h1>
      <p class="buttons">
        <a class="button-lg" href="@/tjanster/">Våra tjänster</a>
        <a class="button-lg bg-white" href="@/kontakt/#offert">Begär offert</a>
      </p>
    </div>
  </section>

  <section class="contact-band bg-sand">
    <div class="container contact-band-inner">
      <div class="contact-band-text">
        <p class="eyebrow eyebrow-dark">Kontakta oss</p>
        <h2>Behöver du en elektriker som kommer när den sagt?</h2>
        <p class="txt-lg">Ring, mejla eller skicka en förfrågan – du får en offert utan att behöva vänta.</p>
        <p class="buttons"><a class="button-lg bg-navy" href="@/kontakt/#offert">Begär offert</a></p>
      </div>
      <ul class="contact-tiles">
        <li><a href="{PHONE_HREF}"><span class="tile-label">Ring oss</span><span class="tile-value">{PHONE}</span></a></li>
        <li><a href="mailto:{EMAIL}"><span class="tile-label">Mejla oss</span><span class="tile-value">{EMAIL}</span></a></li>
        <li><a href="@/om-oss/arbetsomrade/"><span class="tile-label">Vi finns i</span><span class="tile-value">Landvetter &amp; hela Göteborgsregionen</span></a></li>
      </ul>
    </div>
  </section>

  <section class="container cards cards-home">
    <a href="@/tjanster/elinstallation/" class="card card-img"><img src="@/assets/img/elektriker-skap.webp" alt="" loading="lazy"><span>Elinstallation</span></a>
    <a href="@/tjanster/svagstrom/" class="card card-img"><img src="@/assets/img/natverk-patch.webp" alt="" loading="lazy"><span>Svagström</span></a>
    <a href="@/tjanster/badrumsrenovering/" class="card card-img"><img src="@/assets/img/badrum-dusch.webp" alt="" loading="lazy"><span>Badrums&shy;renovering</span></a>
    <a href="@/tjanster/belysning/" class="card card-img"><img src="@/assets/img/kok-ljust.webp" alt="" loading="lazy"><span>Belysning</span></a>
  </section>

  <section class="features">
    <div class="container">
      <div class="features-head">
        <p class="eyebrow eyebrow-dark">Därför Ullevi El</p>
        <h2>Elfirma i Landvetter för hela Göteborgsregionen</h2>
      </div>
      <div class="feature-grid">
        <a class="feature" href="@/tjanster/">
          <span class="feature-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
          <h3>El och svagström</h3>
          <p>Vi utför elinstallationer i bostäder, lokaler och offentliga miljöer – från nya uttag och elcentraler till larm, nätverk och annan svagström. Arbetet görs med aktuellt material och modern teknik.</p>
          <span class="link">Våra tjänster</span>
        </a>
        <a class="feature" href="@/tjanster/badrumsrenovering/">
          <span class="feature-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5s-6.5 7.2-6.5 12a6.5 6.5 0 0 0 13 0c0-4.8-6.5-12-6.5-12z"/></svg></span>
          <h3>Renovering med el på köpet</h3>
          <p>Vi renoverar badrum och kök med egna elektriker. Våra elektriker har våtrumscertifikat, så el, belysning och golvvärme blir rätt från början – i samma projekt.</p>
          <span class="link">Badrumsrenovering</span>
        </a>
        <a class="feature" href="@/om-oss/behorigheter/">
          <span class="feature-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.6-4.6 1.4 1.4z"/></svg></span>
          <h3>Behörig elfirma</h3>
          <p>{COMPANY} är registrerat hos Elsäkerhetsverket med behörigheter för bland annat bostäder, allmänna och offentliga utrymmen, elnät och elproduktionsanläggningar.</p>
          <span class="link">Behörigheter</span>
        </a>
      </div>
    </div>
  </section>

  <section class="container section-pb">
    <div class="image-block boxed">
      <img class="cover" src="@/assets/img/badrum-marmor.webp" alt="Renoverat badrum med marmor och LED-belysning" loading="lazy">
      <div class="image-block-content">
        <h2 class="txt-h1">Badrum från golv till tak</h2>
        <p class="txt-lg">Hel- eller delrenovering av badrum med kakel, VVS, golvvärme och belysning. Du har en kontaktperson genom hela projektet och el som utförs av våtrumscertifierade elektriker.</p>
        <p><a class="link" href="@/tjanster/badrumsrenovering/">Om badrumsrenovering</a></p>
      </div>
    </div>
  </section>

  <section class="split split-full bg-sand">
    <div class="split-text">
      <div>
        <h2>Service och entreprenad av högsta kvalité.</h2>
        <p class="txt-lg">Vi är ett litet team med kort väg mellan dig och den som utför jobbet. Vi lyssnar, ger tydliga besked och håller det vi lovar – oavsett om det gäller ett nytt uttag i villan eller elen i en hel lokal.</p>
        <p><a class="link" href="@/om-oss/">Om Ullevi El</a></p>
      </div>
    </div>
    <div class="split-img"><img src="@/assets/img/elektriker-hjalm.webp" alt="Elektriker i hjälm vid ett elskåp" loading="lazy"></div>
  </section>

  <section class="split split-full split-reverse bg-navy">
    <div class="split-img"><img src="@/assets/img/natverk-kablar.webp" alt="Nätverkskablar i ett patchskåp" loading="lazy"></div>
    <div class="split-text">
      <div>
        <h2>Svagström som bara fungerar</h2>
        <p class="txt-lg">Data- och nätverksdragning, larm och andra tekniska installationer. Vi drar, kopplar och dokumenterar så att anläggningen är lätt att bygga ut när behoven växer.</p>
        <p><a class="button-lg" href="@/tjanster/svagstrom/">Om svagström</a></p>
      </div>
    </div>
  </section>
''')

PAGES["tjanster/index.html"] = ("Tjänster | Ullevi El",
"Elinstallation, svagström, belysning, badrumsrenovering, kök och solceller i Göteborg med omnejd.",
f'''{page_hero("Tjänster", "Från ett nytt uttag till el, svagström och renovering i hela fastigheter. Välj ett område nedan eller hör av dig direkt – vi hjälper dig att hitta rätt lösning.")}
{service_cards()}
  <section class="container intro">
    <h2>Ett samtal – hela jobbet</h2>
    <div class="cols-3">
      <div><h3>Privatpersoner</h3><p>Villor, radhus och lägenheter: nya uttag, byte av elcentral, belysning, badrum och kök.</p></div>
      <div><h3>Företag &amp; BRF</h3><p>Lokaler, kontor och föreningar: elinstallation, nätverk, larm och service av befintliga anläggningar.</p></div>
      <div><h3>Offentliga miljöer</h3><p>Behörighet för allmänna och offentliga utrymmen – vi arbetar efter gällande regler och dokumenterar allt.</p></div>
    </div>
  </section>
{cta()}''')

PAGES["tjanster/elinstallation/index.html"] = ("Elinstallation | Ullevi El",
"Elinstallationer i bostäder, lokaler och offentliga miljöer i Göteborg, Mölndal, Härryda och Partille.",
service_page("tjanster/elinstallation/", "Elinstallation",
"Pålitliga elinstallationer i hem, företag och offentliga byggnader – utförda med aktuellt material och modern teknik.",
"elektriker-elcentral", "Elektriker felsöker en elcentral",
"Rätt utfört från början",
"<p>Vi utför allt från mindre jobb i villan till nyinstallationer i hela lokaler. Som registrerat elinstallationsföretag hos Elsäkerhetsverket arbetar vi efter gällande regler, och du får en tydlig offert innan vi börjar.</p><p>Behöver du hjälp med något akut eller vill du planera ett större projekt? Ring oss så tar vi det därifrån.</p>",
["Nya uttag, strömbrytare och dragningar", "Byte och uppgradering av elcentral", "Jordfelsbrytare och överspänningsskydd",
 "El vid om- och tillbyggnad", "Värme, kyla och ventilation", "Felsökning och service", "Kabelförläggning"],
split("Elcentralen är hjärtat i huset",
"<p class=\"txt-lg\">En gammal elcentral med proppar kan vara både opraktisk och osäker. Vi byter till en modern central med automatsäkringar och jordfelsbrytare – och ser till att den klarar framtida behov.</p>",
"elektriker-skap", "Elektriker arbetar i ett elskåp", button=("Begär offert", "@/kontakt/#offert")),
faq=[("Måste en behörig elektriker göra jobbet?", "Ja, de flesta elinstallationer får bara utföras av ett registrerat elinstallationsföretag. Det gäller allt från nya uttag till byte av elcentral."),
     ("Vad kostar det?", "Det beror på jobbets omfattning. Beskriv vad du behöver så får du en offert – utan att behöva vänta."),
     ("Kan jag använda ROT-avdrag?", "Arbetskostnaden för elarbeten i bostaden kan ge rätt till ROT-avdrag. Vi drar av det direkt på fakturan när det är tillämpligt.")]))

PAGES["tjanster/svagstrom/index.html"] = ("Svagström | Ullevi El",
"Svagströmsmontage: nätverk, data, larm och tekniska installationer i Göteborgsregionen.",
service_page("tjanster/svagstrom/", "Svagström",
"Nätverk, data, larm och andra tekniska installationer – svagström är en av våra specialiteter, det står till och med i vårt namn.",
"natverk-patch", "Nätverkskablar kopplade i en patchpanel",
"Tekniken bakom väggarna",
"<p>Svagström är allt det som får moderna byggnader att fungera: nätverk, data, larm och kommunikation. Vi planerar, drar och kopplar installationen och lämnar över en tydlig dokumentation.</p><p>Vi arbetar både i nyproduktion och i befintliga fastigheter, och anpassar lösningen efter hur lokalerna faktiskt används.</p>",
["Data- och nätverksdragning", "Patchskåp och nätverksuttag", "Larminstallationer", "Tekniska installationer i lokaler", "Felsökning och utbyggnad av befintliga nät", "Dokumentation och märkning"],
split("Byggt för att växa",
"<p class=\"txt-lg\">Strukturerad kabeldragning och märkning gör det enkelt att felsöka, flytta arbetsplatser och bygga ut när verksamheten växer.</p>",
"natverk-kablar", "Strukturerad kabeldragning", bg="bg-navy", reverse=True, button=("Begär offert", "@/kontakt/#offert", "button-lg"))))

PAGES["tjanster/belysning/index.html"] = ("Belysning | Ullevi El",
"Planering och installation av belysning inomhus och utomhus – för hem, kök, badrum och lokaler.",
service_page("tjanster/belysning/", "Belysning",
"Rätt ljus gör stor skillnad. Vi hjälper dig att planera och installera belysning i hemmet, köket, badrummet och lokalen.",
"kok-ljust", "Ljust kök med pendellampor",
"Ljus som passar rummet",
"<p>Vi installerar takbelysning, spotlights, LED-list, pendlar och utebelysning – och hjälper dig att placera ljuset så att det fungerar i vardagen. Dimmer och smart styrning kan ofta läggas till i samma jobb.</p>",
["Spotlights och infällda armaturer", "LED-belysning i kök och badrum", "Pendlar och takarmaturer", "Utebelysning och fasadbelysning", "Dimmer och styrning", "Byte till energisnål LED"],
split("Kök och badrum",
"<p class=\"txt-lg\">I kök och badrum är belysningen extra viktig. Vi kombinerar arbetsljus med stämningsljus och följer reglerna för våtrum.</p>",
"kok-morkt", "Kök med pendlar och LED-belysning", button=("Om badrumsrenovering", "@/tjanster/badrumsrenovering/"))))

PAGES["tjanster/badrumsrenovering/index.html"] = ("Badrumsrenovering | Ullevi El",
"Total och partiell badrumsrenovering i Göteborg med omnejd – med våtrumscertifierade elektriker.",
service_page("tjanster/badrumsrenovering/", "Badrumsrenovering",
"Vi renoverar badrum i Göteborg med omnejd – helt eller delvis. Elektrikerna har våtrumscertifikat, så el och belysning ingår i samma projekt.",
"badrum-marmor", "Badrum med marmorkakel och glasdusch",
"Ett badrum, en kontakt",
"<p>En badrumsrenovering involverar flera yrken: rivning, tätskikt, kakel, VVS och el. Hos oss har du en kontaktperson genom hela projektet, och elen görs av våra egna elektriker.</p><p>Vi hjälper till med allt från en ny dusch och nya ytskikt till en komplett totalrenovering.</p>",
["Totalrenovering av badrum", "Partiell renovering och byte av ytskikt", "Golvvärme", "Belysning, spotlights och speglar med LED", "VVS: dusch, WC och handfat", "El enligt regler för våtrum"],
split("Våtrumscertifierade elektriker",
"<p class=\"txt-lg\">El i våtrum kräver extra noggrannhet. Våra elektriker har våtrumscertifikat och vet hur uttag, belysning och golvvärme ska placeras och installeras för att bli säkert.</p>",
"badrum-dusch", "Modernt duschrum med belyst spegel", reverse=True, button=("Begär offert", "@/kontakt/#offert")),
faq=[("Hur lång tid tar en badrumsrenovering?", "Det beror på storlek och omfattning. Du får en tidsplan tillsammans med offerten."),
     ("Kan jag göra delar av jobbet själv?", "Ja, se vår sida för hemmafixare. El och tätskikt bör alltid utföras av behörig hantverkare.")]))

PAGES["tjanster/kok-och-vvs/index.html"] = ("Kök, VVS & renovering | Ullevi El",
"Köksrenovering, VVS-service och reparationer i Göteborg med omnejd.",
service_page("tjanster/kok-och-vvs/", "Kök, VVS &amp; renovering",
"Köksrenovering, VVS-reparationer och service – med el och belysning från samma firma.",
"kok-morkt", "Mörkt kök med marmorbänk och pendlar",
"Renovering med helhetsansvar",
"<p>Vi utför köksrenoveringar och mindre renoveringsjobb i hemmet. Eftersom vi själva är elektriker blir el, belysning och vitvaror rätt inkopplade från början.</p><p>Vi hjälper även till med VVS-reparationer och service.</p>",
["Köksrenovering", "El för spis, ugn och vitvaror", "Belysning under skåp och över bänk", "VVS-reparationer och service", "Byte av blandare och anslutningar", "Mindre snickeri- och renoveringsjobb"],
split("Köket är husets mötesplats",
"<p class=\"txt-lg\">Ett nytt kök kräver ofta fler uttag, egna grupper för vitvaror och bättre belysning. Vi planerar elen tillsammans med dig innan skåpen kommer på plats.</p>",
"kok-ljust", "Ljust kök med köksö", button=("Begär offert", "@/kontakt/#offert"))))

PAGES["tjanster/solceller/index.html"] = ("Solceller & elproduktion | Ullevi El",
"Elinstallation för solceller och elproduktionsanläggningar.",
service_page("tjanster/solceller/", "Solceller &amp; elproduktion",
"Vi har behörighet för elproduktionsanläggningar och hjälper till med elinstallationen när du vill producera egen el.",
"solceller-tak", "Solcellspaneler på ett tegeltak",
"Egen el – rätt inkopplad",
"<p>En solcellsanläggning ska kopplas in säkert mot fastighetens el och elnätet. Vi utför elinstallationen och ser till att elcentralen är dimensionerad för anläggningen.</p>",
["Elinstallation för solceller", "Anpassning och uppgradering av elcentral", "Kabeldragning från tak till central", "Kontroll och dokumentation"],
split("Behörighet för elproduktion",
"<p class=\"txt-lg\">Ullevi El är registrerat hos Elsäkerhetsverket med behörighet för lågspänning i elproduktionsanläggningar.</p>",
"elarbete-detalj", "Elektriker kopplar i ett elskåp", reverse=True, button=("Våra behörigheter", "@/om-oss/behorigheter/"))))

PAGES["om-oss/index.html"] = ("Om oss | Ullevi El",
f"{COMPANY} är en elfirma i Landvetter som arbetar med el, svagström och renovering i Göteborgsregionen.",
f'''{page_hero("Om Ullevi El", "Service och entreprenad av högsta kvalité – till rätt pris, i rätt tid. Det är vad vi levererar, varje gång.")}
{wide_image("elektriker-skap", "Elektriker arbetar i ett elskåp")}
  <section class="container section two-col">
    <div>
      <h2>Ett litet team med stort ansvar</h2>
      <p class="txt-lg">{COMPANY} är en elfirma med bas i Landvetter. Vi arbetar med elinstallationer, svagström och renovering åt privatpersoner, företag och bostadsrättsföreningar i Göteborgsregionen.</p>
      <p>Vi är ett litet företag, och det märks på rätt sätt: du pratar med den som gör jobbet, får snabba besked och en offert utan att behöva vänta.</p>
    </div>
    <div>
      <p class="list-title">Fakta</p>
      <dl class="facts">
        <div><dt>Företag</dt><dd>{COMPANY}</dd></div>
        <div><dt>Org.nr</dt><dd>{ORGNR}</dd></div>
        <div><dt>Säte</dt><dd>Landvetter, Härryda kommun</dd></div>
        <div><dt>Registrerad hos</dt><dd>Elsäkerhetsverket</dd></div>
        <div><dt>Certifikat</dt><dd>Våtrumscertifierade elektriker</dd></div>
        <div><dt>F-skatt</dt><dd>Ja</dd></div>
      </dl>
    </div>
  </section>
{split("Kvalité, pris och tid", '<p class="txt-lg">Tre saker som ska stämma i varje uppdrag. Vi använder aktuellt material och teknik, ger tydliga priser och kommer när vi har sagt.</p>', "elektriker-hjalm", "Elektriker vid ett elskåp", button=("Behörigheter & certifikat", "@/om-oss/behorigheter/"))}
{cta()}''')

PAGES["om-oss/behorigheter/index.html"] = ("Behörigheter & certifikat | Ullevi El",
"Ullevi El är registrerat hos Elsäkerhetsverket och har våtrumscertifierade elektriker.",
f'''{page_hero("Behörigheter &amp; certifikat", "El får bara installeras av den som har rätt behörighet. Här ser du vad vi är registrerade för.")}
  <section class="container section two-col">
    <div>
      <h2>Registrerat elinstallationsföretag</h2>
      <p class="txt-lg">{COMPANY} är registrerat hos Elsäkerhetsverket. Det betyder att vi har en elinstallatör med rätt behörighet och ett egenkontrollprogram för arbetet.</p>
      <p>Du kan själv kontrollera ett företags registrering i Elsäkerhetsverkets register över elinstallationsföretag.</p>
      <p><a class="link" href="https://www.elsakerhetsverket.se/" rel="noopener" target="_blank">Elsäkerhetsverket</a></p>
    </div>
    <div>
      <p class="list-title">Behörigheter</p>
      {checklist(["Lågspänning – bostäder", "Lågspänning – allmänna och offentliga utrymmen", "Lågspänning – elnät", "Lågspänning – elproduktionsanläggningar", "Lågspänning – övriga anläggningar för användning av el", "Begränsad lågspänning – maskiner", "Begränsad lågspänning – värme, kyla och ventilation", "Särskild verksamhet – kabelförläggning i koncessionspliktiga nät"])}
    </div>
  </section>
{split("Våtrumscertifikat", '<p class="txt-lg">Våra elektriker har våtrumscertifikat. Det gör att vi kan ta helhetsansvar för el i badrum och andra våtutrymmen.</p>', "badrum-tra", "Badrum med träpanel och kakel", reverse=True, button=("Badrumsrenovering", "@/tjanster/badrumsrenovering/"))}
{cta()}''')

areas_cards = "\n".join(f'      <li>{a}</li>' for a in AREAS)
PAGES["om-oss/arbetsomrade/index.html"] = ("Arbetsområde | Ullevi El",
"Ullevi El utgår från Landvetter och arbetar i Göteborg, Mölndal, Härryda, Partille, Lerum, Kungsbacka, Borås med flera orter.",
f'''{page_hero("Arbetsområde", "Vi utgår från Landvetter och tar uppdrag i hela Göteborgsregionen och Sjuhärad.")}
  <section class="container section">
    <h2>Här arbetar vi</h2>
    <ul class="area-list">
{areas_cards}
    </ul>
    <p>Finns inte din ort med? Hör av dig ändå – vi tar gärna uppdrag även utanför listan.</p>
    <p class="buttons"><a class="button-lg" href="@/kontakt/#offert">Begär offert</a></p>
  </section>
{wide_image("solceller-tak", "Villatak med solceller")}
{cta()}''')

PAGES["hemmafixare/index.html"] = ("För hemmafixare | Ullevi El",
"Renoverar du själv? Vi tar hand om det som kräver behörighet – el och våtrum – så blir det rätt första gången.",
f'''{page_hero("För hemmafixare", "Renoverar du badrummet eller köket själv? Vi hjälper dig med det som kräver behörighet, så att det blir rätt första gången.")}
{wide_image("badrum-tra", "Badrum under renovering med kakel och träpanel")}
  <section class="container section two-col">
    <div>
      <h2>Du gör jobbet – vi gör elen</h2>
      <p class="txt-lg">Många vill göra delar av renoveringen själva för att hålla nere kostnaden. Det går bra, så länge det som kräver behörighet görs av fackmän.</p>
      <p>Elinstallationer får bara utföras av ett registrerat elinstallationsföretag. Vi kommer in i rätt skede, drar och kopplar elen och ser till att allt är dokumenterat.</p>
    </div>
    <div>
      <p class="list-title">Så här brukar det gå till</p>
      <ol class="steps">
        <li><strong>Planering.</strong> Vi går igenom var uttag, belysning och golvvärme ska sitta.</li>
        <li><strong>Grovinstallation.</strong> Vi drar rör och kablar innan väggar och golv stängs.</li>
        <li><strong>Ditt arbete.</strong> Du gör det du har planerat att göra själv.</li>
        <li><strong>Slutinstallation.</strong> Vi kopplar in, kontrollerar och dokumenterar.</li>
      </ol>
    </div>
  </section>
{cta()}''')

PAGES["kontakt/index.html"] = ("Kontakt | Ullevi El",
f"Kontakta Ullevi El: {PHONE}, {EMAIL}. {ADDRESS[0]}, {ADDRESS[1]}.",
f'''{page_hero("Kontakt", "Ring, mejla eller skicka en offertförfrågan. Vi återkommer så snart vi kan.")}
  <section class="container section contact-grid">
    <div class="contact-info">
      <div><p class="list-title">Telefon</p><p class="txt-h2"><a href="{PHONE_HREF}">{PHONE}</a></p></div>
      <div><p class="list-title">E-post</p><p class="txt-lg"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
      <div><p class="list-title">Adress</p><p>{COMPANY}<br>{ADDRESS[0]}<br>{ADDRESS[1]}</p></div>
      <div><p class="list-title">Org.nr</p><p>{ORGNR}</p></div>
    </div>
    <form class="quote-form" id="offert" data-email="{EMAIL}">
      <h2>Begär offert</h2>
      <p>Fyll i formuläret så öppnas ett färdigt mejl till oss i ditt e-postprogram.</p>
      <div class="field-row">
        <label for="f-name">Namn<input id="f-name" name="namn" required autocomplete="name"></label>
        <label for="f-phone">Telefon<input id="f-phone" name="telefon" type="tel" autocomplete="tel"></label>
      </div>
      <div class="field-row">
        <label for="f-email">E-post<input id="f-email" name="epost" type="email" required autocomplete="email"></label>
        <label for="f-place">Ort<input id="f-place" name="ort" autocomplete="address-level2"></label>
      </div>
      <label for="f-service">Tjänst
        <select id="f-service" name="tjanst">
          {"".join(f"<option>{t}</option>" for _, t, _ in SERVICES)}
          <option>Annat</option>
        </select>
      </label>
      <label for="f-msg">Beskriv jobbet<textarea id="f-msg" name="meddelande" rows="5" required></textarea></label>
      <p class="buttons"><button class="button-lg" type="submit">Skicka förfrågan</button></p>
      <p class="form-note" role="status" hidden></p>
    </form>
  </section>
{wide_image("elektriker-skap", "Elektriker arbetar i ett elskåp")}''')

PAGES["integritetspolicy/index.html"] = ("Integritetspolicy | Ullevi El",
"Så hanterar Ullevi El dina personuppgifter.",
f'''{page_hero("Integritetspolicy", "Så hanterar vi dina personuppgifter när du kontaktar oss.")}
  <section class="container section prose">
    <h2>Personuppgiftsansvarig</h2>
    <p>{COMPANY}, org.nr {ORGNR}, {ADDRESS[0]}, {ADDRESS[1]}, är personuppgiftsansvarig.</p>
    <h2>Vilka uppgifter vi behandlar</h2>
    <p>När du kontaktar oss behandlar vi de uppgifter du själv lämnar, till exempel namn, telefonnummer, e-postadress, adress och beskrivning av uppdraget.</p>
    <h2>Varför vi behandlar uppgifterna</h2>
    <p>Uppgifterna används för att besvara din förfrågan, lämna offert, utföra uppdraget och fakturera. Vi sparar dem så länge det behövs för detta och för att uppfylla krav i bokföringslagen.</p>
    <h2>Dina rättigheter</h2>
    <p>Du har rätt att begära utdrag, rättelse eller radering av dina uppgifter. Kontakta oss på <a href="mailto:{EMAIL}">{EMAIL}</a>. Du kan också lämna klagomål till Integritetsskyddsmyndigheten (IMY).</p>
    <h2>Cookies</h2>
    <p>Webbplatsen använder inga spårningscookies.</p>
  </section>''')

PAGES["404.html"] = ("Sidan hittades inte | Ullevi El", "Sidan finns inte.",
f'''{page_hero("Sidan hittades inte", "Sidan du letar efter finns inte eller har flyttats.")}
  <section class="container section"><p class="buttons"><a class="button-lg" href="@/">Till startsidan</a> <a class="button-lg bg-white" href="@/kontakt/">Kontakta oss</a></p></section>''')


def build():
    for out, (title, desc, body) in PAGES.items():
        depth = out.count("/")
        prefix = "../" * depth if depth else "./"
        html = layout(title, desc, body)
        if out == "404.html":
            # 404 visas på godtycklig URL – använd absoluta sökvägar under projektroten
            html = html.replace('"@/', '"/Test_bygg/')
        html = html.replace('"@/', f'"{prefix}').replace('"./"', '"./"')
        path = ROOT / out
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        print("skrev", out)


if __name__ == "__main__":
    build()
