
from pathlib import Path
import re
import shutil
from datetime import date

SITE_URL = "https://gajogae-yupum.netlify.app"
BRAND = "가족애유품정리"
INDEX_FILE = Path("index.html")
REGIONS_FILE = Path("regions.txt")
REGIONS_DIR = Path("regions")
SITEMAP_FILE = Path("sitemap-regions.xml")

CITY_PAGES = [
    ("창원", "창원시", "changwon", ["창원시", "창원"], "의창구, 성산구, 마산합포구, 마산회원구, 진해구"),
    ("마산", "창원시 마산", "masan", ["마산", "마산합포구", "마산회원구"], "마산합포구, 마산회원구, 내서읍, 월영동, 합성동"),
    ("진해", "창원시 진해구", "jinhae", ["진해", "진해구"], "석동, 이동, 자은동, 웅천동, 풍호동"),
    ("김해", "김해시", "gimhae", ["김해시", "김해"], "장유동, 내외동, 북부동, 삼안동, 진영읍"),
    ("진주", "진주시", "jinju", ["진주시", "진주"], "평거동, 충무공동, 상평동, 중앙동, 가호동"),
    ("양산", "양산시", "yangsan", ["양산시", "양산"], "물금읍, 동면, 서창동, 평산동, 덕계동"),
    ("거제", "거제시", "geoje", ["거제시", "거제"], "고현동, 장평동, 옥포동, 아주동, 상문동"),
    ("통영", "통영시", "tongyeong", ["통영시", "통영"], "무전동, 광도면, 정량동, 북신동, 도천동"),
    ("사천", "사천시", "sacheon", ["사천시", "사천"], "사천읍, 정동면, 벌리동, 향촌동, 용현면"),
    ("밀양", "밀양시", "miryang", ["밀양시", "밀양"], "삼문동, 내이동, 가곡동, 하남읍, 부북면"),
    ("함안", "함안군", "haman", ["함안군", "함안"], "가야읍, 칠원읍, 군북면, 대산면, 칠서면"),
    ("창녕", "창녕군", "changnyeong", ["창녕군", "창녕"], "창녕읍, 남지읍, 영산면, 부곡면, 대합면"),
    ("고성", "고성군", "goseong", ["고성군", "고성"], "고성읍, 회화면, 거류면, 동해면, 하이면"),
    ("남해", "남해군", "namhae", ["남해군", "남해"], "남해읍, 이동면, 삼동면, 창선면, 미조면"),
    ("하동", "하동군", "hadong", ["하동군", "하동"], "하동읍, 진교면, 금남면, 악양면, 화개면"),
    ("산청", "산청군", "sancheong", ["산청군", "산청"], "산청읍, 신안면, 단성면, 시천면, 생초면"),
    ("함양", "함양군", "hamyang", ["함양군", "함양"], "함양읍, 안의면, 수동면, 마천면, 지곡면"),
    ("거창", "거창군", "geochang", ["거창군", "거창"], "거창읍, 가조면, 웅양면, 남상면, 마리면"),
    ("합천", "합천군", "hapcheon", ["합천군", "합천"], "합천읍, 가야면, 초계면, 삼가면, 대병면"),
    ("의령", "의령군", "uiryeong", ["의령군", "의령"], "의령읍, 부림면, 정곡면, 지정면, 화정면"),
]

def backup(path):
    if path.exists():
        b = path.with_name(path.stem + ".seo_pro_backup" + path.suffix)
        if not b.exists():
            shutil.copy2(path, b)

def read_regions():
    if not REGIONS_FILE.exists():
        return []
    return [x.strip() for x in REGIONS_FILE.read_text(encoding="utf-8").splitlines() if x.strip() and not x.strip().startswith("#")]

def find_existing_page(region):
    if not REGIONS_DIR.exists():
        return None
    for f in sorted(REGIONS_DIR.glob("*.html")):
        if f.name == "index.html" or "backup" in f.name:
            continue
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if region in txt:
            return f.name
    return None

def child_section(keywords, all_regions):
    links = []
    for region in all_regions:
        if any(k in region for k in keywords):
            filename = find_existing_page(region)
            if filename:
                links.append(f'<a href="/regions/{filename}">{region} 유품정리</a>')
        if len(links) >= 20:
            break
    if not links:
        return ""
    links_html = "\n".join(links)
    return f"""
<section class="city-child-links near-region-links" id="city-child-regions">
  <div class="wrap">
    <div class="section-title">
      <h2>세부 지역 유품정리 바로가기</h2>
      <p>읍·면·동 상세 페이지도 함께 확인할 수 있습니다.</p>
    </div>
    <div class="regions">
{links_html}
    </div>
  </div>
</section>
"""

def meta_name(html, name, content):
    pat = rf'<meta[^>]+name=["\']{name}["\'][^>]*>'
    tag = f'<meta name="{name}" content="{content}">'
    if re.search(pat, html, flags=re.I):
        return re.sub(pat, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def meta_prop(html, prop, content):
    pat = rf'<meta[^>]+property=["\']{prop}["\'][^>]*>'
    tag = f'<meta property="{prop}" content="{content}">'
    if re.search(pat, html, flags=re.I):
        return re.sub(pat, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def set_canonical(html, url):
    tag = f'<link rel="canonical" href="{url}">'
    if 'rel="canonical"' in html:
        html = re.sub(r'<link[^>]+rel=["\']canonical["\'][^>]*>', tag, html, count=1, flags=re.I)
        html = re.sub(r'<link[^>]+href=["\'][^"\']+["\'][^>]+rel=["\']canonical["\'][^>]*>', tag, html, count=1, flags=re.I)
        return html
    return html.replace("</head>", tag + "\n</head>", 1)

def seo_block(city, full, slug, keywords, areas, all_regions):
    detail = child_section(keywords, all_regions)
    return f"""
<section class="city-seo-story" id="city-story">
  <div class="wrap">
    <div class="section-title">
      <h2>{city} 유품정리 실제 상담이 많은 이유</h2>
      <p>{city} 전지역 유품정리, 고독사청소, 특수청소, 빈집정리까지 현장 상황에 맞춰 안내합니다.</p>
    </div>

    <div class="panel">
      <h3>{city} 유품정리는 단순한 청소와 다릅니다</h3>
      <p>{city}에서 유품정리를 문의하시는 분들은 대부분 갑작스러운 상황에서 연락을 주십니다. 가족이 직접 정리하기에는 마음의 부담이 크고, 물건의 양이 많거나 폐기물 처리 방법을 몰라 어디서부터 시작해야 할지 막막한 경우가 많습니다. 유품정리는 단순히 집 안의 짐을 치우는 일이 아니라 고인의 생활 흔적을 정성스럽게 확인하고, 유족에게 필요한 물품을 놓치지 않도록 분류하는 과정입니다.</p>
      <p>{BRAND}는 {city} 현장에서 통장, 도장, 계약서, 사진, 귀금속, 현금, 중요 서류처럼 확인이 필요한 물품을 먼저 살펴봅니다. 정리 과정에서 보관해야 할 물건과 폐기해야 할 물건을 나누고, 유족이 직접 확인해야 하는 물품은 별도로 구분합니다.</p>
      <p>{city} 지역은 {areas} 등 다양한 생활권으로 나뉘어 있어 아파트, 빌라, 단독주택, 원룸, 상가주택 등 현장 형태도 다양합니다. 엘리베이터 사용 가능 여부, 차량 진입 가능 여부, 폐기물 반출 거리, 공동주택 관리 규정 등에 따라 작업 방식과 시간이 달라질 수 있습니다.</p>
    </div>

    <div class="split">
      <div class="panel">
        <h3>{city} 유품정리 진행 과정</h3>
        <p>상담이 접수되면 먼저 주소, 주거 형태, 정리할 공간, 짐의 양, 보관 물품 여부를 확인합니다. 이후 현장에 맞춰 작업 인원과 차량, 폐기물 처리 범위를 정리하고 유족과 일정 조율을 진행합니다.</p>
        <p>작업 당일에는 중요한 물품을 우선 확인한 뒤 방, 거실, 주방, 창고, 베란다 순서로 분류합니다. 폐기물은 가능한 품목과 별도 처리가 필요한 품목을 구분하고, 정리 후에는 공간 상태를 확인하며 마무리합니다.</p>
      </div>

      <div class="panel">
        <h3>{city} 고독사청소·특수청소가 필요한 경우</h3>
        <p>현장에 냄새, 오염, 장기간 방치 흔적이 있다면 일반 유품정리만으로는 부족할 수 있습니다. 이 경우 오염 부위 확인, 폐기물 분류, 소독, 탈취, 필요한 경우 특수청소 절차를 함께 안내합니다.</p>
        <p>고독사청소는 유족에게 심리적으로 큰 부담이 될 수 있기 때문에 현장 노출을 최소화하고, 필요한 설명만 차분하게 전달하는 것이 중요합니다.</p>
      </div>
    </div>

    <div class="panel">
      <h3>{city} 유품정리 비용을 결정하는 요소</h3>
      <p>{city} 유품정리 비용은 단순히 평수만으로 정해지지 않습니다. 짐의 양, 폐기물 처리량, 가구와 가전의 크기, 엘리베이터 유무, 사다리차 필요 여부, 차량 진입 가능 여부, 소독과 탈취 필요 여부에 따라 달라집니다. 같은 평수라도 장기간 방치된 집과 정리된 집은 작업 범위가 크게 다를 수 있습니다.</p>
      <p>정확한 비용을 확인하려면 현장 사진이나 간단한 영상, 주소, 정리할 공간 범위를 알려주시는 것이 좋습니다. 상담 단계에서 가능한 범위와 예상 작업 절차를 먼저 안내드리고, 필요할 경우 방문 견적을 통해 실제 작업 범위를 확인합니다.</p>
    </div>
  </div>
</section>
{detail}
"""

def insert_before_contact(html, block):
    if 'class="city-seo-story"' in html:
        return html
    for marker in ['id="contact"', '상담접수', 'id="faq"', '유품정리 자주 묻는 질문']:
        pos = html.find(marker)
        if pos != -1:
            start = html.rfind("<section", 0, pos)
            if start != -1:
                return html[:start] + block + "\n" + html[start:]
    return html.replace("</body>", block + "\n</body>", 1)

def connect_links(html):
    for city, full, slug, keywords, areas in CITY_PAGES:
        plain = f"{city} 유품정리"
        linked = f'<a href="/regions/{slug}.html">{city} 유품정리</a>'
        if linked not in html and plain in html:
            html = html.replace(plain, linked, 1)
    return html

def make_page(city, full, slug, keywords, areas, all_regions):
    html = INDEX_FILE.read_text(encoding="utf-8")
    url = f"{SITE_URL}/regions/{slug}.html"
    title = f"{city} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc = f"{city} 유품정리 전문 {BRAND}입니다. {city} 고독사청소, 특수청소, 빈집정리, 폐기물처리 상담과 방문 견적을 진행합니다."

    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)
    html = meta_name(html, "description", desc)
    html = meta_name(html, "keywords", f"{city} 유품정리,{city} 유품정리 업체,{city} 고독사청소,{city} 특수청소,{city} 빈집정리,{BRAND}")
    html = set_canonical(html, url)
    html = meta_prop(html, "og:title", title)
    html = meta_prop(html, "og:description", desc)
    html = meta_prop(html, "og:url", url)
    html = meta_name(html, "twitter:title", title)
    html = meta_name(html, "twitter:description", desc)

    html = re.sub(r"<h1>.*?</h1>", f"<h1>{city} 유품정리 전문업체<br>{BRAND}</h1>", html, count=1, flags=re.S)
    html = connect_links(html)
    html = insert_before_contact(html, seo_block(city, full, slug, keywords, areas, all_regions))

    schema = f"""
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{city} 유품정리","provider":{{"@type":"LocalBusiness","name":"{BRAND}","telephone":"+82-10-9242-3895","areaServed":"{full}"}},"serviceType":["유품정리","고독사청소","특수청소","빈집정리","폐기물처리"],"url":"{url}","description":"{desc}"}}
</script>
"""
    if f'"url":"{url}"' not in html:
        html = html.replace("</head>", schema + "\n</head>", 1)
    return html

def create_pages():
    if not INDEX_FILE.exists():
        raise FileNotFoundError("index.html 파일이 없습니다.")
    REGIONS_DIR.mkdir(exist_ok=True)
    all_regions = read_regions()
    for city, full, slug, keywords, areas in CITY_PAGES:
        (REGIONS_DIR / f"{slug}.html").write_text(make_page(city, full, slug, keywords, areas, all_regions), encoding="utf-8")
    print(f"시군 대표 페이지 SEO 강화 완료: {len(CITY_PAGES)}개")

def update_sitemap():
    backup(SITEMAP_FILE)
    today = date.today().isoformat()
    if SITEMAP_FILE.exists():
        xml = SITEMAP_FILE.read_text(encoding="utf-8")
    else:
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
    for city, full, slug, keywords, areas in CITY_PAGES:
        loc = f"{SITE_URL}/regions/{slug}.html"
        if loc in xml:
            continue
        block = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
"""
        xml = xml.replace("</urlset>", block + "</urlset>")
    SITEMAP_FILE.write_text(xml, encoding="utf-8")
    print("sitemap-regions.xml 반영 완료")

def main():
    create_pages()
    update_sitemap()
    print("완료")
    print(f"확인 예시: {SITE_URL}/regions/changwon.html")

if __name__ == "__main__":
    main()
