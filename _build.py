# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
ORIGIN = "https://www.antalyamodernmermer.com.tr"

def ico(name):
    raw = (ROOT / "assets" / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    raw = raw.replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
    return raw.replace("<svg", '<svg class="ico"', 1).strip()


ICO_PHONE = ico("phone")
ICO_WA = ico("whatsapp")
ICO_IG = ico("instagram")
ICO_FB = ico("facebook")
ICO_YT = ico("youtube")
ICO_PIN = ico("location")
ICO_CLK = ico("work-time")
ICO_RAN = ico("randevu")
ICO_MAIL = ico("mail")
ICO_MENU = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 7h16v2H4zm0 4h16v2H4zm0 4h16v2H4z"/></svg>'
ICO_CHEV = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 10l5 5 5-5z"/></svg>'

MARBLE = '''<svg viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">
  <path class="vein v1" d="M-40 90 C 140 20, 280 160, 460 80 S 780 20, 980 110 S 1220 40, 1280 90"/>
  <path class="vein v2" d="M-20 130 C 180 60, 340 180, 520 100 S 840 40, 1040 140 S 1260 80, 1300 120"/>
  <path class="vein v3" d="M-10 50 C 220 120, 400 10, 600 70 S 900 150, 1200 40"/>
</svg>'''

DISTRICTS = [
    ("Döşemealtı", "dosemealti-mermer-tezgah", "villa ve müstakil mutfaklar", "Çıplaklı, Yeşilbayır, Yeniköy ve Kırkavak hattında ölçü için sabah randevusu daha rahat. Villa ada tezgahı ile bahçe barbeküsü aynı günde ölçülür; montajı dolapçı ile aynı saate yazıyoruz.", "Ada ve sırtlık için damarlı mermer; bahçe barbekü için granit; banyo ve açık mutfak için porselen veya çimstone."),
    ("Muratpaşa", "muratpasa-mermer-tegah", "şehir içi daire ve işyerleri", "Atölye Yeşildere’de olduğu için Muratpaşa keşfi çoğu gün aynı gün yapılabiliyor. Lara, Fener, Meltem ve Güzeloba mutfaklarında L köşe ve ada tezgahına sık bakıyoruz.", "Şehir içi dairede çimstone veya mat mermer; işyeri tezgahında granit daha az çizilir."),
    ("Alanya", "alanya-mermer-tezgah", "sahil siteleri ve yazlık mutfaklar", "Alanya–Mahmutlar hattında tuzlu hava ve nem için gözeneksiz yüzey (porselen veya çimstone) öneriyoruz. Ölçü günü siteden giriş saatini önceden alıyoruz.", "Tuzlu hava için porselen veya çimstone. Açık mermer yazlıkta leke ve tuz izi gösterir."),
    ("Kemer", "kemer-mermer-tezgah", "bungalov ve otel mutfakları", "Kemer–Göynük yolunda teslimat öğleden sonra planlanıyor. Dar merdivenli evlerde tezgahı iki parça kesip yerinde birleştiriyoruz.", "Dar merdiven için ince porselen veya parçalı granit. Bungalov bar tezgahında mat yüzey daha az bakım ister."),
    ("Kumluca", "kumluca-mermer-tezgah", "sera evleri ve müstakil mutfaklar", "Kumluca–Mavikent hattında toz ve sulama izi çok görüldüğü için koyu granit veya mat porselen daha az leke gösteriyor.", "Toz ve sulama izi için koyu granit veya mat porselen. Açık mermer sera evinde çabuk leke alır."),
    ("Finike", "finike-mermer-tezgah", "bahçe evi ve mutfak adaları", "Finike ölçüsü sabah erken alınırsa aynı hafta kesime girebiliyor. Portakal bahçeli evlerde dış tezgah için dona dayanıklı granit seçiyoruz.", "Bahçe tezgahı için dona dayanıklı granit; iç ada için mermer veya kuvars."),
    ("Kaş & Kalkan", "kas-kalkan-memrer-tezgah", "taş ev ve dar mutfaklar", "Kaş ve Kalkan’da merdiven ve dar kapı ölçüsünü önce alıyoruz. Kalın plakayı siteye sokmadan atölyede parçalıyoruz.", "Taş evin dar kapısına ince porselen veya iki parça mermer. Kalın granit merdivenden geçmez."),
    ("Manavgat", "manavgat-mermer-tezgah", "yeni konut ve site mutfakları", "Manavgat–Side sitelerinde yönetimin asansör gününü soruyoruz. Ada tezgahı tek parça gitmezse görünmez derz ile birleştiriyoruz.", "Yeni sitede çimstone veya porselen; ada tek parça sığmazsa görünmez derz açıyoruz."),
    ("Serik", "seri-memer-tezgah", "Belek ve Kadriye mutfakları", "Serik–Belek villalarında açık mutfak adası çok isteniyor. Golf sitelerinde teslimat aracı için güvenlik kaydı gerekiyor.", "Villa adası için damarlı mermer; dış bar için granit. Golf sitelerinde plaka giriş kaydı şart."),
    ("Aksu", "aksu-mermer-tezgah", "yeni yerleşim mutfakları", "Aksu–Kundu hattı atölyeye yakın; ölçü ile montaj arasında 2–4 gün yetebiliyor. Evye deliğini dolap geldiğinde yerinde açıyoruz.", "Stoktaki mermer veya çimstone 2–4 günde biter. Kundu yazlıklarında porselen daha az leke tutar."),
    ("Kepez", "kepez-mermer-tezgah", "apartman mutfakları", "Kepez’de asansör ölçüleri dar kalabiliyor. 3 cm plakayı kat holünde dik taşıyıp yerinde yatırıyoruz.", "Apartman mutfağında çimstone bakımı kolay. Asansöre sığmayan graniti atölyede ikiye keseriz."),
    ("Konyaaltı", "konyaalti-memer-tezgah", "deniz manzaralı daireler", "Konyaaltı–Liman mahallelerinde nem için silika esaslı yüzey veya iyi emprenye edilmiş mermer konuşuyoruz. Balkon bar tezgahı ayrı ölçü alıyor.", "Nem için porselen veya emprenye mermer. Balkon barı granit veya UV’li kuvars ister."),
]

PRODUCTS = [
    ("Mermer tezgahlar", "/urunlerimiz/mermer-tezgahlar/", "/assets/img/urunler/mermer-tezgah-antalya.jpg", "Mermer damarlı, serin tutan bir yüzey. Limon ve sirkeyi bezle silmek gerekir; mat cilayı mutfakta daha çok tercih ediyoruz."),
    ("Porselen tezgahlar", "/urunlerimiz/porselen-tezgahlar/", "/assets/img/urunler/porselen-tezgah-antalya.png", "Leke ve çizilmeye kapalı, ince plaka. Sıcak tencere için yine altlık öneririz; damar deseni mermere yakın durur."),
    ("Granit yüzeyler", "/urunlerimiz/granit-yuzeyler/", "/assets/img/urunler/granit-tezgah-antalya.jpg", "Çizilmeye dayanıklı, mat veya parlak. Koyu taneli taşlar yağ izini daha az gösterir; eviye kenarı suyun altına düşmez."),
    ("Çimstone & Kuvars", "/urunlerimiz/cimstone-kuvars/", "/assets/img/urunler/cimstone-kuvars-antalya.jpg", "Tek parça görünüm, az derz. Çay ve zerdeçal izini aynı gün silmek yeterli; dış mekânda UV’siz seri seçiyoruz."),
    ("Antalya Mezar Modelleri", "/urunlerimiz/antalya-mezar-modelleri/", "/assets/img/urunler/mezar-modelleri-antalya.jpg", "Baştaşı, çerçeve ve kapak aynı taş ailesinden kesilir. Mezarlık idaresinin ölçü kağıdını işe başlamadan istiyoruz."),
]

PHONE_A = ("0533 317 11 46", "+905333171146")
PHONE_B = ("0533 659 28 66", "+905336592866")
WA_A = "https://wa.me/905333171146"
WA_B = "https://wa.me/905336592866"


def schema_graph(extra):
    base = [
        {
            "@type": "LocalBusiness",
            "@id": ORIGIN + "/#business",
            "name": "Antalya Modern Mermer & Granit",
            "image": ORIGIN + "/assets/img/og-cover.jpg",
            "url": ORIGIN + "/",
            "telephone": [PHONE_A[1], PHONE_B[1]],
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Yeşildere Mah. Gazi Bulvarı No: 590D",
                "addressLocality": "Muratpaşa",
                "addressRegion": "Antalya",
                "postalCode": "07310",
                "addressCountry": "TR",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": 36.8872, "longitude": 30.7368},
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                    "opens": "08:00",
                    "closes": "18:00",
                }
            ],
            "contactPoint": [
                {
                    "@type": "ContactPoint",
                    "telephone": PHONE_A[1],
                    "contactType": "customer service",
                    "areaServed": "TR-07",
                    "availableLanguage": ["Turkish"],
                },
                {
                    "@type": "ContactPoint",
                    "telephone": PHONE_B[1],
                    "contactType": "customer service",
                    "areaServed": "TR-07",
                    "availableLanguage": ["Turkish"],
                },
            ],
            "areaServed": [{"@type": "AdministrativeArea", "name": n} for n, *_ in DISTRICTS] + [
                {"@type": "AdministrativeArea", "name": "Antalya"}
            ],
            "sameAs": [
                "https://www.instagram.com/modernmermergranit07",
                "https://www.facebook.com/modernmermergranit07",
                "https://www.youtube.com/@modernmermergranit07",
            ],
        }
    ]
    return {"@context": "https://schema.org", "@graph": base + extra}


def faqs_html(items):
    blocks = []
    for i, (q, a) in enumerate(items, 1):
        blocks.append(
            f'<div class="faq-item"><button type="button" aria-expanded="false" id="s{i}">{q}</button><div class="answer" role="region">{a}</div></div>'
        )
    return '<div class="faq-list"><h2>Sık sorulanlar</h2>\n' + "\n".join(blocks) + "</div>"


def district_faqs(name, tip, extra, stone):
    return [
        (f"{name}’da ölçü randevusu ne zaman gelir?", f"{name} için ölçü, WhatsApp’tan yazdığınız gün veya ertesi sabah planlanır. {tip.capitalize()} işlerinde dolapçı ile aynı saate denk getirmeye çalışırız."),
        (f"{name} mutfağına hangi taş önerilir?", stone),
        (f"{name} montajı kaç günde biter?", f"Ölçü alındıktan sonra stoktaki plaka ile {name} işi genelde 3–6 günde kapanır. Ada tezgahı veya merdiven taşıması varsa bir gün eklenir."),
        (f"{name} sitelerinde asansör ve giriş izni?", f"{name} sitelerinde güvenlik kaydı ve asansör örtüsü gerekebilir. Plaka ölçüsünü kapı ve asansör boşluğuna göre atölyede parçalıyoruz."),
        (f"{name} keşfi ücretli mi?", f"Muratpaşa atölyesine yakın {name} keşfi için yol ücreti almıyoruz. Uzak mahallede ikinci keşif olursa önceden söyleriz."),
        (f"{name}’da evye deliği nerede açılır?", "Marka belli değilse deliği montaj gününe bırakırız. Yanlış delinmiş tezgahı kurtarmak, yeni plaka kesmekten pahalıya gelir."),
        (f"{name} mezar taşı da kesiliyor mu?", f"Evet. {name} mezarlıkları için baştaşı, çerçeve ve kapak Muratpaşa’da kesilir. İdare ölçü kâğıdı olmadan kazıya geçmiyoruz."),
    ]


def product_faqs(slug):
    data = {
        "mermer-tezgahlar": [
            ("Mermer tezgah leke tutar mı?", "Limon, sirke ve kırmızı şarap asitli. Mat cilalı mermerde iz, parlak ciladan geç çıkar. Sıvıyı aynı gün bezle alın; gece bekletmeyin."),
            ("Hangi mermer mutfağa uyar?", "Açık damarlı plakayı atölyede gün ışığında seçin. Ekran rengi yanıltır. Mutfakta mat cila, banyoda parlak daha sık istenir."),
            ("Mermer tezgah kaç günde takılır?", "Ölçüden sonra 2–5 iş günü. Evye ve ocak boşluğu atölyede açılır, montaj günü silikon ve ayak ayarı yapılır."),
            ("Kenar profili ne seçilir?", "Yarım bomba elin değdiği yerde yumuşak durur. Dik kenar düz kapaklı mutfakta daha az toz tutar. Numuneyi atölyede görün."),
            ("Mermer fiyatı nasıl çıkar?", "Metrekare, kenar işi, evye deliği ve fire ayrı yazılır. Peşin metre fiyatı plaka damarına göre değişir."),
        ],
        "porselen-tezgahlar": [
            ("Porselen tezgah çizilir mi?", "Sırlı yüzey bıçak izine mermerden dayanır. Yine de kesme tahtası kullanın; sır çatlamaz ama metal iz bırakabilir."),
            ("İnce porselen dolabı taşır mı?", "Evye altında destek çıtası ister. Montajda dolap gövdesini kontrol ederiz; zayıf gövdede takmayız."),
            ("Sıcak tencere konur mu?", "Kısa süre dayanır, silikon ve derz ısınır. Altlık kullanın. Dışarıda UV’siz seri solabilir."),
            ("Porselen mermere benzer mi?", "Damar desenli seriler mermere yakın durur, asidi geçirmez. Plakayı atölyede yan yana görün."),
            ("Porselen ne kadar sürede gelir?", "Stoktaki desen 3–6 gün. Sipariş plaka 10–20 günü bulur; tarihi ölçüden önce söyleriz."),
        ],
        "granit-yuzeyler": [
            ("Granit tezgah çizilir mi?", "Kuvars kristali mermerden serttir. Bıçak izi azdır; kesme tahtası taşı uzun yaşatır."),
            ("Koyu granit yağ izi gösterir mi?", "Parlak koyu taş parmak ve yağ izini daha çok gösterir. Mat veya taneli yüzey mutfakta daha az bakım ister."),
            ("Granit dış basamakta kullanılır mı?", "Don çatlağına dayanıklı cinsi seçiyoruz. İç tezgah ile aynı taş olmak zorunda değil."),
            ("Granit eviye kenarı nasıl biter?", "Su, eviye içine düşecek şekilde eğim verilir. Düz bırakılan kenar dolabı şişirir."),
            ("Granit ölçüden sonra kaç gün?", "Stokta varsa 3–5 gün. Kalın basamak ve merdiven işi ayrı kesim günü ister."),
        ],
        "cimstone-kuvars": [
            ("Çimstone leke tutar mı?", "Çay, kahve, zerdeçal aynı gün silinirse iz kalmaz. Gece bırakmayın; reçine gözenekleri yavaş dolar."),
            ("Kuvars balkona konur mu?", "Güneş gören yerde UV dayanımlı seri gerekir. İç mekân plakasını balkona kesmeyiz."),
            ("Derz neden az görünür?", "Tek parça plaka ve ince derz. L köşede görünmez birleşim atölyede şablona göre açılır."),
            ("Renk kartelası yeterli mi?", "Hayır. Kartela küçük; tam plakayı Gazi Bulvarı atölyesinde bakın. Ekran tonu yanıltır."),
            ("Çimstone fiyatı neye bağlı?", "Renk serisi, kalınlık, kenar ve evye. Fire, ada ve L köşede artar."),
        ],
        "antalya-mezar-modelleri": [
            ("Mezar taşı için ne gerekir?", "Mezarlık adı, parsel ve idarenin ölçü kâğıdı. Kâğıt yoksa kazıya başlamıyoruz."),
            ("Baştaşı yazısı nasıl onaylanır?", "Punto ve arma kâğıt çıktıda imzalanır. Kazıdan sonra harf düzeltmek taşı zayıflatır."),
            ("Baştaşı, çerçeve ve kapak aynı renk olur mu?", "Aynı ocaktan seçilirse fark azalır. Farklı partilerde damar kayar; plakaları yan yana gösteriyoruz."),
            ("Antalya mezarlıklarında yükseklik sınırı?", "İdare kâğıdındaki ölçüye keseriz. Kepez, Muratpaşa ve Döşemealtı mezarlıklarında kural kâğıda yazılır."),
            ("Mezar işi kaç günde teslim?", "Yazı onayı sonrası 5–10 gün. Montaj mezarlık çalışma saatine bağlıdır."),
        ],
    }
    return data[slug]


def faq_schema(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


def nav(active):
    def cls(key):
        return ' class="nav-link is-active"' if active == key else ' class="nav-link"'

    dlinks = "\n".join(
        f'<a href="/antalya-mermer-tezgah/{slug}/">{name}</a>' for name, slug, *_ in DISTRICTS
    )
    plinks = "\n".join(f'<a href="{href}">{title}</a>' for title, href, *_ in PRODUCTS)
    return f'''
    <nav class="nav" id="menu" aria-label="Ana menü">
      <ul class="nav-list">
        <li><a href="/"{cls("home")}>Ana Sayfa</a></li>
        <li><a href="/hakkimizda/"{cls("about")}>Hakkımızda</a></li>
        <li class="has-sub">
          <a href="/antalya-mermer-tezgah/"{cls("bol")}>Antalya Mermer Tezgah</a>
          <button type="button" class="sub-toggle" aria-expanded="false" aria-label="İlçe listesini aç">{ICO_CHEV}</button>
          <div class="sub">
            <a href="/antalya-mermer-tezgah/">Tüm ilçeler</a>
            {dlinks}
          </div>
        </li>
        <li class="has-sub">
          <a href="/urunlerimiz/"{cls("urun")}>Ürünlerimiz</a>
          <button type="button" class="sub-toggle" aria-expanded="false" aria-label="Ürün listesini aç">{ICO_CHEV}</button>
          <div class="sub">
            <a href="/urunlerimiz/">Tüm ürünler</a>
            {plinks}
          </div>
        </li>
        <li><a href="/iletisim/"{cls("iletisim")}>İletişim</a></li>
      </ul>
    </nav>'''


def page(path, title, desc, canonical, active, body, extra_schema=None, og_image="/assets/img/og-cover.jpg", faq=None, homepage=False):
    graph_extra = extra_schema or []
    if faq:
        graph_extra.append(faq_schema(faq))
    schema = json.dumps(schema_graph(graph_extra), ensure_ascii=False, indent=2)
    hero_anim = ""
    if homepage:
        hero_anim = f'''
  <section class="hero">
    <img class="hero-photo" src="/assets/img/hero/hero-mutfak-tezgah.jpg" width="1600" height="1200" alt="Antalya mutfağına döşenmiş damarlı mermer tezgah ve aynı taştan sırtlık">
    <div class="hero-shade"></div>
    <div class="hero-graphic">{MARBLE}</div>
    <div class="hero-dust" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
    <div class="hero-copy">
      <p class="kicker">Muratpaşa atölyesi</p>
      <h1>Mutfak tezgahını atölyede kesip evde bitiriyoruz</h1>
      <p class="lead">Yeşildere, Gazi Bulvarı 590D’deki tezgâhta plakayı görürsünüz. Ölçü evde alınır, evye ve ocak boşluğu atölyede açılır, montaj günü silikon ve ayak ayarı yerinde yapılır.</p>
      <div class="hero-actions">
        <a class="btn btn-pill" href="{WA_A}">{ICO_RAN} Ölçü yazın</a>
        <a class="btn btn-outline" href="tel:{PHONE_A[1]}">{ICO_PHONE} {PHONE_A[0]}</a>
      </div>
      <div class="hero-card">Muratpaşa Yeşildere’de kesilir. Antalya ilçelerine aynı ekip montaja gider.</div>
    </div>
    <div class="side-label">Modern Mermer 07</div>
  </section>'''

    html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="Antalya Modern Mermer & Granit">
  <meta name="geo.region" content="TR-07">
  <meta name="geo.placename" content="Muratpaşa, Antalya">
  <meta name="theme-color" content="#2a2118">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/assets/img/logo/logo-modern-mermer.png" type="image/png">
  <link rel="apple-touch-icon" href="/assets/img/logo/logo-modern-mermer.png">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:site_name" content="Antalya Modern Mermer & Granit">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{ORIGIN}{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{ORIGIN}{og_image}">
  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body>
  <a class="skip" href="#icerik">İçeriğe geç</a>
  <header class="site-header">
    <div class="header-motion">{MARBLE}</div>
    <div class="header-inner">
      <a class="brand" href="/">
        <img src="/assets/img/logo/logo-modern-mermer.png" width="232" height="271" alt="Modern Mermer ve Granit">
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu" aria-label="Menüyü aç">{ICO_MENU}</button>
      {nav(active)}
      <div class="header-actions">
        <a class="btn btn-outline" href="tel:{PHONE_A[1]}">{ICO_PHONE} Ara</a>
        <a class="btn btn-pill" href="{WA_A}">{ICO_RAN} Teklif</a>
      </div>
    </div>
  </header>
  {hero_anim}
  <main id="icerik">
  {body}
  </main>
  <div class="float-cta">
    <a class="wa" href="{WA_A}" aria-label="WhatsApp">{ICO_WA}</a>
    <a class="call" href="tel:{PHONE_A[1]}" aria-label="Telefon {PHONE_A[0]}">{ICO_PHONE}</a>
    <a class="call" href="tel:{PHONE_B[1]}" aria-label="Telefon {PHONE_B[0]}">{ICO_PHONE}</a>
  </div>
  <footer class="site-footer">
    <div class="foot-grid">
      <div>
        <h2>Antalya Modern Mermer &amp; Granit</h2>
        <p>Yeşildere Mah. Gazi Bulvarı No: 590D, Muratpaşa / Antalya</p>
        <p><a href="tel:{PHONE_A[1]}">{PHONE_A[0]}</a><br><a href="tel:{PHONE_B[1]}">{PHONE_B[0]}</a></p>
        <p>Pazartesi–Cumartesi 08:00–18:00</p>
      </div>
      <div>
        <h2>Sayfalar</h2>
        <p><a href="/hakkimizda/">Hakkımızda</a><br><a href="/urunlerimiz/">Ürünlerimiz</a><br><a href="/antalya-mermer-tezgah/">Antalya Mermer Tezgah</a><br><a href="/iletisim/">İletişim</a></p>
      </div>
      <div>
        <h2>Sosyal</h2>
        <p>
          <a href="https://www.instagram.com/modernmermergranit07">{ICO_IG} Instagram</a><br>
          <a href="https://www.facebook.com/modernmermergranit07">{ICO_FB} Facebook</a><br>
          <a href="https://www.youtube.com/@modernmermergranit07">{ICO_YT} YouTube</a>
        </p>
        <p class="credit">Atölye · Muratpaşa</p>
      </div>
    </div>
    <div class="legal">© <span id="yil">2026</span> Antalya Modern Mermer &amp; Granit</div>
  </footer>
  <script src="/site.js" defer></script>
</body>
</html>
'''
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(path)


HOME_FAQ = [
    ("Mermer tezgah kaç günde takılır?", "Muratpaşa ve Kepez’de ölçüden sonra 2–5 iş günü yeter. Alanya, Kaş, Kumluca gibi uzak ilçelerde yol günü eklenir; plaka atölyede bekliyorsa süre kısalır."),
    ("Keşif ücretli mi?", "Antalya şehir içi ölçü için ücret almıyoruz. Kaş–Kalkan ve Alanya Mahmutlar için yol payını iş başlamadan söyleriz."),
    ("Hangi taş leke tutmaz?", "Limon ve zeytinyağı için porselen veya çimstone daha bağışlayıcı. Mermer damarı güzel durur ama asidi aynı gün silmek gerekir."),
    ("Mezar taşı için ne gerekir?", "Mezarlık adı, parsel ve idarenin ölçü kâğıdı. Baştaşı yazısını kağıt üzerinde onayladıktan sonra kazıya geçiyoruz."),
]


def cards():
    html = []
    for title, href, img, text in PRODUCTS:
        html.append(
            f'<article class="card"><a href="{href}"><img src="{img}" width="800" height="600" alt="{title}, Antalya atölye işi"></a><div class="card-body"><h3>{title}</h3><p class="muted">{text}</p><a class="more" href="{href}">İncele</a></div></article>'
        )
    return "\n".join(html)


def write_all():
    home_body = f'''
    <section class="wrap">
      <div class="section-head">
        <p class="kicker">Ne kesiyoruz</p>
        <h2>Tezgah, sırtlık, ada ve mezar taşı aynı atölyede</h2>
        <p class="muted">Plakayı Gazi Bulvarı’ndaki tezgâhta görüp kenar profilini orada seçiyorsunuz. Aşağıdaki işler, sitede kullandığımız gerçek mutfak ve mezar fotoğrafları.</p>
      </div>
      <figure class="figure">
        <img src="/assets/img/urunler/mermer-tezgah-antalya.jpg" width="1200" height="900" alt="Ahşap dolap üzerine yeşil damarlı mermer tezgah, Aksu–Antalya mutfağı">
        <figcaption>Yeşil damarlı mermer tezgah, eviye ve ocak boşluğu atölyede açıldı.</figcaption>
      </figure>
      <div class="grid-3">{cards()}</div>
    </section>
    <hr class="hr">
    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>İş nasıl ilerliyor</h2>
          <p class="muted">Süre, taşın atölyede olup olmamasına bağlı. Stoktaki plaka ile şehir içi mutfak genelde aynı hafta kapanır.</p>
        </div>
        <div class="steps">
          <div class="step"><em>1</em><h3>WhatsApp veya çağrı</h3><p>Mutfak fotoğrafı, dolap ölçüsü ve ilçe adı yeterli. Aynı gün dönüş yapıyoruz.</p></div>
          <div class="step"><em>2</em><h3>Yerinde ölçü</h3><p>Lazerle köşe ve duvar payı alınır. Dolap henüz yoksa iskelet üzerine şablon çıkarılır.</p></div>
          <div class="step"><em>3</em><h3>Kesim</h3><p>Evye, ocak ve kenar (yarım bomba, dik kenar) atölyede işlenir. 2–4 gün.</p></div>
          <div class="step"><em>4</em><h3>Montaj</h3><p>Ayak ayarı, silikon ve derz aynı seferde. Artan parça isterseniz size bırakılır.</p></div>
        </div>
      </div>
    </section>
    <section class="wrap">
      <div class="grid-2">
        <div class="article">
          <h2>Atölye Muratpaşa Yeşildere’de</h2>
          <p>Gazi Bulvarı 590D, otobüs durağının birkaç adım ötesi. Plakayı gün ışığında görmek için öğleden önce gelin; damar yönü o saatte daha net okunuyor.</p>
          <p>Kepez, Konyaaltı, Aksu ve Döşemealtı için öğleden sonra montaj planlıyoruz. Alanya ve Kaş günleri haftalık takvime yazılıyor.</p>
          <p><a class="btn btn-pill" href="/hakkimizda">Atölyeyi tanıyın</a></p>
        </div>
        <figure class="figure">
          <img src="/assets/img/hero/hero-atolye.png" width="1200" height="800" alt="Antalya Modern Mermer Muratpaşa atölyesinde kesim tezgahı">
          <figcaption>Kesim tezgahı, Yeşildere atölyesi.</figcaption>
        </figure>
      </div>
    </section>
    <hr class="hr">
    <section>
      <div class="wrap">
        <h2>Hizmet verdiğimiz ilçeler</h2>
        <p class="muted">Her ilçe sayfasında yol süresi ve o bölgede sık gördüğümüz mutfak tipi var.</p>
        <div class="chip-list">
          {''.join(f'<a class="chip" href="/antalya-mermer-tezgah/{slug}/">{name}</a>' for name, slug, *_ in DISTRICTS)}
        </div>
      </div>
    </section>
    <section class="wrap">
      {faqs_html(HOME_FAQ)}
    </section>
    '''
    page(
        "index.html",
        "Antalya Mermer Tezgah | Modern Mermer & Granit",
        "Muratpaşa atölyesinde mermer, granit, çimstone ve porselen tezgah. Ücretsiz ölçü, kesim ve montaj. 0533 317 11 46.",
        ORIGIN + "/",
        "home",
        home_body,
        extra_schema=[{"@type": "WebSite", "url": ORIGIN + "/", "name": "Antalya Modern Mermer & Granit"}],
        faq=HOME_FAQ,
        homepage=True,
    )

    # anasayfa: same content, canonical home
    page(
        "anasayfa/index.html",
        "Ana Sayfa | Antalya Modern Mermer & Granit",
        "Muratpaşa atölyesinde mermer, granit, çimstone ve porselen tezgah. Ücretsiz ölçü, kesim ve montaj.",
        ORIGIN + "/",
        "home",
        home_body,
        faq=HOME_FAQ,
        homepage=True,
    )

    about = '''
    <header class="page-hero"><div class="header-motion">''' + MARBLE + '''</div>
      <div class="wrap wrap-sm">
        <p class="crumbs"><a href="/">Ana sayfa</a> / Hakkımızda</p>
        <h1>Taşı kesenler ile montaja gidenler aynı ekip</h1>
        <p class="lead">Atölye Muratpaşa Yeşildere’de, Gazi Bulvarı 590D. Tezgah siparişi de mezar taşı da buradan çıkar.</p>
      </div>
    </header>
    <section class="wrap article">
      <figure class="figure">
        <img src="/assets/img/atolye/atolye-iscilik.png" width="1400" height="900" alt="Atölyede mermer plaka işleme, Antalya Modern Mermer">
        <figcaption>Plaka işaretleme ve kesim, Yeşildere atölyesi.</figcaption>
      </figure>
      <p>İşi telefonla kapatmıyoruz. Önce dolabın fotoğrafına bakıyoruz; sonra evde lazerle ölçü alıyoruz. Köşe duvar 90 derece durmuyorsa şablon çıkıyor, plaka o şablona göre kesiliyor.</p>
      <p>Kenar profilini (dik, yarım bomba, damla) atölyede numune üzerinden seçiyorsunuz. Evye markası belli değilse deliği montaj gününe bırakıyoruz; yanlış delik açılmış tezgahı kurtarmak zor.</p>
      <p>Antalya’da yazın plaka güneşte bekletilmez, gölgede istiflenir. Kışın silikon için yüzeyin kuru olması gerekir; yağmurlu günde montajı kaydırırız.</p>
      <p>Mezar işinde idarenin kâğıdı yoksa kazıya başlamıyoruz. Harf punto ve arma yerleşimini kâğıt çıktıda imzalatıyoruz.</p>
    </section>
    '''
    page(
        "hakkimizda/index.html",
        "Hakkımızda | Antalya Modern Mermer Atölyesi",
        "Muratpaşa Yeşildere’de mermer, granit ve çimstone kesiyoruz. Ölçü, kenar profili ve montaj aynı ekipte.",
        ORIGIN + "/hakkimizda",
        "about",
        about,
        og_image="/assets/img/hero/hero-atolye.png",
    )

    contact_faq = [
        ("WhatsApp’ta ne yazmalıyım?", "İlçe, mutfak veya mezar, kabaca en-boy ve bir fotoğraf. Dönüş aynı gün içinde gelir."),
        ("Atölye pazar açık mı?", "Pazar kapalıyız. Pazartesi 08:00’de açılır."),
    ]
    contact = f'''
    <header class="page-hero"><div class="header-motion">{MARBLE}</div>
      <div class="wrap wrap-sm">
        <p class="crumbs"><a href="/">Ana sayfa</a> / İletişim</p>
        <h1>Ölçü ve teklif için yazın</h1>
        <p class="lead">Form WhatsApp’a düşer; sunucuda kayıt tutmuyoruz. İsterseniz doğrudan arayın.</p>
      </div>
    </header>
    <section class="wrap">
      <div class="grid-2">
        <form class="form" id="teklif-formu" action="#" method="post" novalidate>
          <label for="ad">Adınız</label>
          <input id="ad" name="ad" maxlength="80" autocomplete="name" required>
          <label for="telefon">Telefon</label>
          <input id="telefon" name="telefon" maxlength="18" autocomplete="tel" inputmode="tel" required>
          <label for="ilce">İlçe</label>
          <select id="ilce" name="ilce">
            {''.join(f'<option>{n}</option>' for n, *_ in DISTRICTS)}
          </select>
          <label for="mesaj">İşin tarifi</label>
          <textarea id="mesaj" name="mesaj" maxlength="400" required placeholder="Örn. Kepez 2. kat, L mutfak, çimstone bakıyoruz"></textarea>
          <button class="btn btn-pill" type="submit">{ICO_RAN} WhatsApp’tan gönder</button>
          <p class="note" id="form-durum">HTML etiketleri temizlenir. Sadece düz metin yazın.</p>
        </form>
        <div>
          <ul class="info-list">
            <li>{ICO_PIN}<span>Yeşildere Mah. Gazi Bulvarı No: 590D, Muratpaşa / Antalya</span></li>
            <li>{ICO_PHONE}<span><a href="tel:{PHONE_A[1]}">{PHONE_A[0]}</a></span></li>
            <li>{ICO_PHONE}<span><a href="tel:{PHONE_B[1]}">{PHONE_B[0]}</a></span></li>
            <li>{ICO_WA}<span><a href="{WA_A}">{PHONE_A[0]} WhatsApp</a></span></li>
            <li>{ICO_WA}<span><a href="{WA_B}">{PHONE_B[0]} WhatsApp</a></span></li>
            <li>{ICO_CLK}<span>Pazartesi–Cumartesi 08:00–18:00<br>Pazar kapalı</span></li>
          </ul>
          <p><a class="btn btn-pill" href="https://maps.google.com/?q=Gazi+Bulvarı+590D+Muratpaşa+Antalya">{ICO_PIN} Haritada aç</a></p>
          {faqs_html(contact_faq)}
        </div>
      </div>
    </section>
    '''
    page(
        "iletisim/index.html",
        "İletişim | Antalya Modern Mermer WhatsApp",
        "Yeşildere Gazi Bulvarı 590D, Muratpaşa. 0533 317 11 46 · 0533 659 28 66. Pazartesi–Cumartesi 08:00–18:00.",
        ORIGIN + "/iletisim",
        "iletisim",
        contact,
        faq=contact_faq,
    )

    dosemealti_mahalle = [
        "Çıplaklı", "Yeşilbayır", "Yeniköy", "Kırkavak", "Bademağacı",
        "Dağbeli", "Aşağıoba", "Çığlık", "Karaveliler", "Killik",
    ]
    tezgah_faq = [
        ("Antalya’da ölçü randevusu ne zaman gelir?", "WhatsApp’tan yazdığınız gün veya ertesi sabah planlanır. Döşemealtı, Kepez, Konyaaltı ve Aksu işleri çoğu kez aynı hafta kapanır."),
        ("Hangi ilçelere montaj gidiyor?", "Döşemealtı, Muratpaşa, Alanya, Kemer, Kumluca, Finike, Kaş–Kalkan, Manavgat, Serik, Aksu, Kepez ve Konyaaltı. Atölye Muratpaşa Yeşildere’de."),
        ("Döşemealtı villasına hangi taş uyar?", "Ada ve sırtlık için damarlı mermer; bahçe barbekü için granit; banyo ve açık mutfak için porselen veya çimstone."),
        ("Tezgah kaç günde takılır?", "Stoktaki plaka ile şehir içi 3–6 gün. Ada veya merdiven taşıması bir gün ekler. Alanya ve Kaş’ta yol günü ayrı yazılır."),
        ("Keşif ücretli mi?", "Şehir içi keşifte yol ücreti yok. Uzak mahallede ikinci keşif olursa önceden söyleriz."),
        ("Evye deliği nerede açılır?", "Marka belli değilse deliği montaj gününe bırakırız. Yanlış delinmiş tezgahı kurtarmak yeni plakadan pahalıya gelir."),
        ("Mezar taşı da kesiliyor mu?", "Evet. İlçe mezarlıkları için baştaşı, çerçeve ve kapak Muratpaşa’da kesilir. İdare ölçü kâğıdı olmadan kazıya geçmiyoruz."),
    ]
    district_index = f'''
    <header class="page-hero"><div class="header-motion">{MARBLE}</div>
      <div class="wrap wrap-sm">
        <p class="crumbs"><a href="/">Ana sayfa</a> / Antalya Mermer Tezgah</p>
        <h1>Antalya Mermer Tezgah</h1>
        <p class="lead">Muratpaşa atölyesinden on iki ilçeye ölçü, kesim ve montaj. Ada tezgahı, barbekü yüzeyi ve mezar taşı aynı tezgâhta çıkar.</p>
      </div>
    </header>
    <section class="wrap article">
      <figure class="figure">
        <img src="/assets/img/hero/hero-mutfak-tezgah.jpg" width="1600" height="1200" alt="Antalya mutfağına monte edilen damarlı mermer tezgah ve sırtlık">
        <figcaption>Tezgah ve sırtlık aynı plakadan; Antalya villa mutfağı örneği.</figcaption>
      </figure>
      <p>Gazi Bulvarı 590D’deki atölyeden Antalya’nın ilçelerine gidiyoruz. Plakayı gün ışığında seçiyorsunuz; ölçü evde, kesim Muratpaşa’da, montaj aynı ekipte. Limon ve yağ çok olan mutfakta porselen veya çimstone, damar isteyen yerde mermer, dış barbeküde granit konuşuyoruz.</p>
      <h2>Döşemealtı villa ve konut işleri</h2>
      <p>Döşemealtı’nda iş çoğu kez müstakil villa. Çıplaklı, Yeşilbayır ve Yeniköy hattında sabah ölçü daha rahat; montajı dolapçı ile aynı güne yazıyoruz. Geniş mutfak adası için mermer, bahçe barbekü için granit, banyo için porselen. İnşaat tozu açık mermerde iz bırakır; dış tezgahı granit veya porselen seçiyoruz.</p>
      <p>Bahçeli evlerde çimstone ve kuvars, aile kabristanında mermer veya granit mezar. Keşif için yol ücreti almıyoruz. Fiyat plaka, kenar ve evye deliğine göre ölçüden sonra yazılır. Ayrıntı <a href="/antalya-mermer-tezgah/dosemealti-mermer-tezgah">Döşemealtı mermer tezgah</a> sayfasında.</p>
      <div class="svc-grid">
        <article class="svc"><h3>Mermer tezgah</h3><p>Döşemealtı villalarına damarlı ada ve sırtlık. Plakayı atölyede gün ışığında seçin.</p></article>
        <article class="svc"><h3>Kuvars &amp; çimstone</h3><p>Yeniköy ve Yeşilbayır mutfaklarında çok istenen az derz yüzey.</p></article>
        <article class="svc"><h3>Porselen &amp; granit</h3><p>Dış barbekü ve iç tezgah. Tuz yok ama toz var; mat yüzey daha az leke gösterir.</p></article>
        <article class="svc"><h3>Mezar modelleri</h3><p>Döşemealtı mezarlıkları için baştaşı, çerçeve, kapak. İdare kâğıdı olmadan kazımıyoruz.</p></article>
      </div>
      <h2>Hizmet verdiğimiz ilçeler</h2>
      <p>Her ilçe sayfasında o bölgenin yol süresi, mutfak tipi ve taş önerisi var.</p>
      <div class="chip-list">{''.join(f'<a class="chip" href="/antalya-mermer-tezgah/{slug}/">{name} mermer tezgah</a>' for name, slug, *_ in DISTRICTS)}</div>
      <h2>Döşemealtı mahalleleri</h2>
      <p>Ölçü randevusuna mahalle adını yazmanız yeter. Sık geldiğimiz yerler:</p>
      <div class="chip-list">{''.join(f'<span class="chip">{m}</span>' for m in dosemealti_mahalle)}</div>
      {faqs_html(tezgah_faq)}
    </section>
    '''
    page(
        "antalya-mermer-tezgah/index.html",
        "Antalya Mermer Tezgah | İlçe İlçe Ölçü ve Montaj",
        "Antalya mermer tezgah: Döşemealtı villalarından Konyaaltı ve Alanya’ya ölçü, kesim, montaj. Muratpaşa atölyesi. 0533 317 11 46.",
        ORIGIN + "/antalya-mermer-tezgah",
        "bol",
        district_index,
        faq=tezgah_faq,
    )

    for name, slug, tip, extra, stone in DISTRICTS:
        faq = district_faqs(name, tip, extra, stone)
        body = f'''
        <header class="page-hero"><div class="header-motion">{MARBLE}</div>
          <div class="wrap wrap-sm">
            <p class="crumbs"><a href="/">Ana sayfa</a> / <a href="/antalya-mermer-tezgah">Antalya Mermer Tezgah</a> / {name}</p>
            <h1>{name} mermer tezgah ve montaj</h1>
            <p class="lead">Muratpaşa atölyesinden {name}’daki {tip} için ölçü alıp kesiyoruz.</p>
          </div>
        </header>
        <section class="wrap article">
          <figure class="figure">
            <img src="/assets/img/hero/hero-mutfak-tezgah.jpg" width="1600" height="1200" alt="{name} mutfağına uygun mermer tezgah montaj örneği">
            <figcaption>{name} işlerinde kullandığımız tezgah ve sırtlık birleşimi.</figcaption>
          </figure>
          <p>{extra}</p>
          <p>{stone}</p>
          <p>WhatsApp’a ilçe adı, kat numarası ve dolap fotoğrafı yeterli. {name} randevusunu atölye takvimine yazıp ölçüm günü arıyoruz. Montajda silikon rengi taşa göre seçilir; şeffaf her taşa yakışmaz.</p>
          <p>Artan parça varsa eviye altı veya balkon sehpası için bırakılabilir. İstemezseniz atölyeye geri alırız. <a href="/urunlerimiz">Ürünlerimiz</a> sayfasından taş cinsine bakabilirsiniz.</p>
          <p><a class="btn btn-pill" href="https://wa.me/905333171146?text={name}%20mermer%20tezgah%20olcu">{ICO_RAN} {name} için yazın</a></p>
          {faqs_html(faq)}
        </section>
        '''
        page(
            f"antalya-mermer-tezgah/{slug}/index.html",
            f"{name} Mermer Tezgah | Antalya Modern Mermer",
            f"{name} için mermer, granit ve çimstone tezgah. Muratpaşa atölyesinden ölçü ve montaj. 0533 317 11 46.",
            f"{ORIGIN}/antalya-mermer-tezgah/{slug}",
            "bol",
            body,
            faq=faq,
        )

    prod_faq = [
        ("Ürünlerimiz neleri kapsar?", "Beş başlık: mermer tezgahlar, porselen tezgahlar, granit yüzeyler, çimstone ve kuvars, Antalya mezar modelleri. Hepsi Muratpaşa’da kesilir."),
        ("Hangi tezgahı seçmeliyim?", "Limon ve yağ çok olan mutfakta porselen veya çimstone. Damar gören yerde mermeri atölyede plaka olarak bakın. Merdiven ve dış basamak için granit."),
        ("Mermer tezgah leke tutar mı?", "Limon, sirke ve kırmızı şarap asitli. Mat cilada iz parlak ciladan geç çıkar. Sıvıyı aynı gün bezle alın."),
        ("Porselen ile çimstone farkı nedir?", "Porselen ince sırlı plaka, evye altında destek ister. Çimstone-kuvars daha kalın durur, derz az görünür. İkisini atölyede yan yana koyuyoruz."),
        ("Granit dışarıda kullanılır mı?", "Don çatlağına dayanıklı cinsi seçiyoruz. İç tezgah ile aynı taş olmak zorunda değil."),
        ("Mezar modeli için ne gerekir?", "Mezarlık adı, parsel ve idarenin ölçü kâğıdı. Yazı punto kâğıt çıktıda imzalanır; kazıdan sonra harf düzeltmek taşı zayıflatır."),
        ("Fiyat listede yok mu?", "Plaka fire verdiği için metre fiyatı ölçüden sonra yazılır. WhatsApp’a dolap fotoğrafı atın, kalem kalem döneriz."),
        ("Numune nerede görülür?", "Gazi Bulvarı 590D atölyesinde. Küçük kesik varsa veririz; yoksa tam plakaya bakmanızı isteriz."),
    ]
    prod_index = f'''
    <header class="page-hero"><div class="header-motion">{MARBLE}</div>
      <div class="wrap wrap-sm">
        <p class="crumbs"><a href="/">Ana sayfa</a> / Ürünlerimiz</p>
        <h1>Ürünlerimiz</h1>
        <p class="lead">Mermer tezgahlar, porselen tezgahlar, granit yüzeyler, çimstone ve kuvars, Antalya mezar modelleri.</p>
      </div>
    </header>
    <section class="wrap">
      <p>Beş iş kolu Muratpaşa’da kesilir. Plakayı Gazi Bulvarı 590D’de görün; kartela ve ekran rengi yanıltır. Fiyat plaka, kenar profili ve evye deliğine göre ölçüden sonra yazılır.</p>
      <div class="chip-list">{''.join(f'<a class="chip" href="{href}">{title}</a>' for title, href, *_ in PRODUCTS)}</div>
      <div class="grid-3">{cards()}</div>
      <p>Montaj ilçesini <a href="/antalya-mermer-tezgah">Antalya mermer tezgah</a> sayfasından seçebilirsiniz.</p>
      {faqs_html(prod_faq)}
    </section>
    '''
    page(
        "urunlerimiz/index.html",
        "Ürünlerimiz | Mermer, Granit, Çimstone, Mezar",
        "Antalya atölyesinde mermer tezgahlar, porselen tezgahlar, granit yüzeyler, çimstone ve kuvars, mezar modelleri. 0533 317 11 46.",
        ORIGIN + "/urunlerimiz",
        "urun",
        prod_index,
        faq=prod_faq,
    )

    product_pages = {
        "mermer-tezgahlar": (
            "Mermer tezgahlar",
            "Antalya Mermer Tezgah | Damarlı Doğal Taş",
            "Mutfak ve banyo mermer tezgah, sırtlık ve ada. Muratpaşa’da kesim, evde montaj.",
            "/assets/img/urunler/mermer-tezgah-antalya.jpg",
            "/assets/img/hero/hero-mutfak-tezgah.jpg",
            [
                "Mermer, damarı her plakada farklı durduğu için numuneye bakıp işi kapatmayın; atölyedeki tam plakayı görün.",
                "Mat cila, parlak ciladan daha az leke gösterir. Limon, sirke ve kırmızı şarabı bekletmeden silin.",
                "Kenar yarım bomba ise elinizin değdiği yer yumuşak durur; dik kenar çağdaş mutfakta daha sık isteniyor.",
            ],
        ),
        "porselen-tezgahlar": (
            "Porselen tezgahlar",
            "Porselen Tezgah Antalya | İnce ve Sert Yüzey",
            "Porselen mutfak tezgahı Antalya. Leke tutmaz, ince plaka, mermer görünümü.",
            "/assets/img/urunler/porselen-tezgah-antalya.png",
            "/assets/img/urunler/porselen-tezgah-antalya.png",
            [
                "Porselen plaka ince olduğu için dolap evye bölgesinde destek çıtası ister. Bunu montajda kontrol ederiz.",
                "Sıcak tencereyi doğrudan koymayın; taş ısınır, silikon gevşeyebilir.",
                "Damar desenli seriler mermere yakın durur ama asit lekesi bırakmaz.",
            ],
        ),
        "granit-yuzeyler": (
            "Granit yüzeyler",
            "Granit Tezgah Antalya | Çizilmeye Dayanıklı Taş",
            "Antalya granit tezgah ve basamak. Koyu taneli taş yağ izini daha az gösterir.",
            "/assets/img/urunler/granit-tezgah-antalya.jpg",
            "/assets/img/urunler/granit-yuzey-detay.png",
            [
                "Granit bıçak izine mermerden daha dayanır. Yine de kesme tahtası taşı uzun yaşatır.",
                "Parlak granit ışığı yansıtır; mat granit parmak izini saklar.",
                "Dış basamak için don çatlağına dayanıklı cinsi seçiyoruz; iç tezgah ile aynı taş olmak zorunda değil.",
            ],
        ),
        "cimstone-kuvars": (
            "Çimstone ve kuvars",
            "Çimstone Kuvars Antalya | Az Derz Tezgah",
            "Çimstone ve kuvars tezgah Antalya. Tek parça görünüm, kolay silinen yüzey.",
            "/assets/img/urunler/cimstone-kuvars-antalya.jpg",
            "/assets/img/urunler/cimstone-kuvars-detay.png",
            [
                "Kuvars reçine içerir; dış mekânda güneş gören balkon için UV dayanımlı seri gerekir.",
                "Çay, kahve ve zerdeçal izini aynı gün silmek yeter. Gece boyunca bırakmayın.",
                "Renk kartelası atölyede; ekrandaki fotoğraf tonu yanıltır.",
            ],
        ),
        "antalya-mezar-modelleri": (
            "Antalya mezar modelleri",
            "Antalya Mezar Modelleri | Baştaşı ve Kapak",
            "Antalya mezar taşı, baştaşı ve çerçeve. Mezarlık ölçüsüne göre kesim.",
            "/assets/img/urunler/mezar-modelleri-antalya.jpg",
            "/assets/img/urunler/mezar-model-detay.png",
            [
                "Baştaşı, yan taş ve kapak aynı ocaktan seçilirse renk farkı azalır.",
                "Yazı punto ve arma kâğıt çıktıda imzalanır; kazıdan sonra düzeltme zordur.",
                "Mezarlık idaresinin yükseklik sınırı varsa ona göre keseriz. Kâğıdı işe başlamadan isteyin.",
            ],
        ),
    }

    for slug, (h1, title, desc, img1, img2, paras) in product_pages.items():
        faq = product_faqs(slug)
        body = f'''
        <header class="page-hero"><div class="header-motion">{MARBLE}</div>
          <div class="wrap wrap-sm">
            <p class="crumbs"><a href="/">Ana sayfa</a> / <a href="/urunlerimiz">Ürünlerimiz</a> / {h1}</p>
            <h1>{h1}</h1>
            <p class="lead">{paras[0]}</p>
          </div>
        </header>
        <section class="wrap article">
          <figure class="figure">
            <img src="{img1}" width="1200" height="900" alt="{h1}, Antalya Modern Mermer işi">
            <figcaption>{h1} — atölye ve saha fotoğrafı.</figcaption>
          </figure>
          <p>{paras[1]}</p>
          <p>{paras[2]}</p>
          <figure class="figure">
            <img src="{img2}" width="1200" height="900" alt="{h1} detay görünümü">
            <figcaption>Yüzey detayı, Antalya atölyesi.</figcaption>
          </figure>
          <p><a href="/antalya-mermer-tezgah">Antalya mermer tezgah</a> ilçe sayfalarından montaj bölgesini seçebilirsiniz.</p>
          <p><a class="btn btn-pill" href="/iletisim">{ICO_RAN} Bu taş için yazın</a></p>
          {faqs_html(faq)}
        </section>
        '''
        page(
            f"urunlerimiz/{slug}/index.html",
            title,
            desc,
            f"{ORIGIN}/urunlerimiz/{slug}",
            "urun",
            body,
            faq=faq,
            og_image=img1,
        )

    page(
        "404.html",
        "Sayfa bulunamadı | Antalya Modern Mermer",
        "Aradığınız sayfa taşınmış olabilir. Ana sayfadan tezgah ve iletişim sayfalarına geçin.",
        ORIGIN + "/404.html",
        "home",
        '''<section class="wrap article"><h1>Bu adres boş</h1><p>Menüden ana sayfa, ürünlerimiz veya iletişime dönebilirsiniz.</p>
        <p><a class="btn btn-pill" href="/">Ana sayfaya dön</a></p></section>''',
    )


if __name__ == "__main__":
    write_all()
