
from pathlib import Path
import re
import shutil
from datetime import date

SITE_URL = "https://gajogae-yupum.com"
BRAND = "가족애유품정리"

INDEX_FILE = Path("index.html")
REGIONS_FILE = Path("regions.txt")
REGIONS_DIR = Path("regions")
SITEMAP_FILE = Path("sitemap-regions.xml")

CITY_PAGES = [
    ("창원", "창원시", "changwon", ["창원시", "창원"]),
    ("마산", "창원시 마산", "masan", ["마산", "마산합포구", "마산회원구"]),
    ("진해", "창원시 진해구", "jinhae", ["진해", "진해구"]),
    ("김해", "김해시", "gimhae", ["김해시", "김해"]),
    ("진주", "진주시", "jinju", ["진주시", "진주"]),
    ("양산", "양산시", "yangsan", ["양산시", "양산"]),
    ("거제", "거제시", "geoje", ["거제시", "거제"]),
    ("통영", "통영시", "tongyeong", ["통영시", "통영"]),
    ("사천", "사천시", "sacheon", ["사천시", "사천"]),
    ("밀양", "밀양시", "miryang", ["밀양시", "밀양"]),
    ("함안", "함안군", "haman", ["함안군", "함안"]),
    ("창녕", "창녕군", "changnyeong", ["창녕군", "창녕"]),
    ("고성", "고성군", "goseong", ["고성군", "고성"]),
    ("남해", "남해군", "namhae", ["남해군", "남해"]),
    ("하동", "하동군", "hadong", ["하동군", "하동"]),
    ("산청", "산청군", "sancheong", ["산청군", "산청"]),
    ("함양", "함양군", "hamyang", ["함양군", "함양"]),
    ("거창", "거창군", "geochang", ["거창군", "거창"]),
    ("합천", "합천군", "hapcheon", ["합천군", "합천"]),
    ("의령", "의령군", "uiryeong", ["의령군", "의령"]),
]

def backup(path):
    if path.exists():
        b = path.with_name(path.stem + ".backup" + path.suffix)
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
        if f.name == "index.html":
            continue
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if region in txt:
            return f.name
    return None

def make_child_links(keywords, all_regions):
    links = []
    for region in all_regions:
        if any(k in region for k in keywords):
            filename = find_existing_page(region)
            if filename:
                links.append(f'<a href="/regions/{filename}">{region} 유품정리</a>')
        if len(links) >= 40:
            break
    if not links:
        links.append('<a href="/regions/">경남 유품정리 전체 지역 보기</a>')
    return "\n".join(links)

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
    pat = r'<link[^>]+rel=["\']canonical["\'][^>]*>|<link[^>]+href=["\'][^"\']+["\'][^>]+rel=["\']canonical["\'][^>]*>'
    tag = f'<link rel="canonical" href="{url}">'
    if re.search(pat, html, flags=re.I):
        return re.sub(pat, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def city_content(city_name, city_full, slug, keywords, all_regions):
    child_links = ""
    return f"""
<section class="city-represent-section" id="city-service">
  <div class="wrap">
    <div class="section-title">
      <h2>{city_name} 유품정리 상담 안내</h2>
      <p>{city_name} 전지역 유품정리, 고독사청소, 특수청소, 빈집정리 상담과 방문 견적을 진행합니다.</p>
    </div>

    <div class="split">
      <div class="panel">
        <h3>{city_name} 유품정리가 필요한 경우</h3>
        <p>{city_name}에서 유품정리가 필요할 때는 단순히 물건을 치우는 것보다 중요한 물품을 확인하고, 보관할 물건과 정리할 물건을 차분하게 구분하는 과정이 중요합니다.</p>
        <p>{BRAND}는 통장, 도장, 계약서, 사진, 귀금속, 현금 등 중요한 물품을 별도로 확인하며, 현장 상황에 따라 빈집정리, 폐기물처리, 소독과 탈취가 필요한 작업도 함께 안내합니다.</p>
      </div>

      <div class="panel">
        <h3>{city_name} 주요 서비스</h3>
        <div class="keyword-box">
          <div>{city_name} 유품정리</div>
          <div>{city_name} 고독사청소</div>
          <div>{city_name} 특수청소</div>
          <div>{city_name} 빈집정리</div>
          <div>{city_name} 폐기물처리</div>
          <div>{city_name} 방문견적</div>
        </div>
      </div>
    </div>
  </div>
</section>


<section class="city-faq-section" id="city-faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{city_name} 유품정리 자주 묻는 질문</h2>
      <p>상담 전 많이 문의하시는 내용을 정리했습니다.</p>
    </div>
    <div class="faq">
      <details>
        <summary>{city_name} 유품정리 비용은 어떻게 정해지나요?</summary>
        <p>공간 크기, 짐의 양, 폐기물 처리량, 차량 진입 가능 여부, 소독이나 탈취 필요 여부에 따라 달라집니다.</p>
      </details>
      <details>
        <summary>{city_name} 방문 견적이 가능한가요?</summary>
        <p>현장 일정에 따라 방문 상담이 가능하며, 긴급한 경우 전화로 먼저 상황을 확인한 뒤 가능한 일정을 안내드립니다.</p>
      </details>
      <details>
        <summary>고독사청소나 특수청소도 함께 가능한가요?</summary>
        <p>일반 유품정리와 달리 소독, 탈취, 오염 정리 등이 필요할 수 있어 현장 상태를 확인한 뒤 작업 범위를 안내드립니다.</p>
      </details>
    </div>
  </div>
</section>
"""

def insert_city_content(html, block):
    markers = ['id="contact"', '상담접수', '유품정리 진행과정', '유품정리진행과정', 'id="process"']
    for marker in markers:
        pos = html.find(marker)
        if pos != -1:
            start = html.rfind("<section", 0, pos)
            if start != -1:
                return html[:start] + block + "\n" + html[start:]
    return html.replace("</body>", block + "\n</body>", 1)

def connect_index_city_links(html):
    for city_name, city_full, slug, keywords in CITY_PAGES:
        plain = f"{city_name} 유품정리"
        linked = f'<a href="/regions/{slug}.html">{city_name} 유품정리</a>'
        if linked in html:
            continue
        if plain in html:
            html = html.replace(plain, linked, 1)
    return html

def make_city_page_from_index(city_name, city_full, slug, keywords, all_regions):
    if not INDEX_FILE.exists():
        raise FileNotFoundError("index.html 파일이 없습니다.")

    html = INDEX_FILE.read_text(encoding="utf-8")
    url = f"{SITE_URL}/regions/{slug}.html"
    title = f"{city_name} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc = f"{city_name} 유품정리 전문 {BRAND}입니다. {city_name} 고독사청소, 특수청소, 빈집정리, 폐기물처리 상담과 방문 견적을 진행합니다."

    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)
    html = meta_name(html, "description", desc)
    html = meta_name(html, "keywords", f"{city_name} 유품정리,{city_name} 유품정리 업체,{city_name} 고독사청소,{city_name} 특수청소,{city_name} 빈집정리,{BRAND}")
    html = set_canonical(html, url)
    html = meta_prop(html, "og:title", title)
    html = meta_prop(html, "og:description", desc)
    html = meta_prop(html, "og:url", url)
    html = meta_name(html, "twitter:title", title)
    html = meta_name(html, "twitter:description", desc)

    html = re.sub(r"<h1>.*?</h1>", f"<h1>{city_name} 유품정리 전문업체<br>{BRAND}</h1>", html, count=1, flags=re.S)
    html = re.sub(
        r"(<h1>.*?</h1>\s*)<p>.*?</p>",
        rf"\1<p>{city_name} 유품정리 · 고독사청소 · 특수청소 · 빈집정리 상담<br>고인의 물건을 정성스럽게 분류하고 중요한 물품은 별도 확인합니다.</p>",
        html,
        count=1,
        flags=re.S
    )

    html = connect_index_city_links(html)
    html = insert_city_content(html, city_content(city_name, city_full, slug, keywords, all_regions))

    schema = f"""
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{city_name} 유품정리","provider":{{"@type":"LocalBusiness","name":"{BRAND}","telephone":"+82-10-9242-3895","areaServed":"{city_full}"}},"serviceType":["유품정리","고독사청소","특수청소","빈집정리","폐기물처리"],"url":"{url}","description":"{desc}"}}
</script>
"""
    html = html.replace("</head>", schema + "\n</head>", 1)
    return html

def create_city_pages():
    REGIONS_DIR.mkdir(exist_ok=True)
    all_regions = read_regions()
    for city_name, city_full, slug, keywords in CITY_PAGES:
        html = make_city_page_from_index(city_name, city_full, slug, keywords, all_regions)
        (REGIONS_DIR / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"시군 대표 페이지 {len(CITY_PAGES)}개 생성 완료")

def update_index_links():
    if not INDEX_FILE.exists():
        print("index.html 없음: 버튼 링크 연결 건너뜀")
        return
    backup(INDEX_FILE)
    html = INDEX_FILE.read_text(encoding="utf-8")
    new_html = connect_index_city_links(html)
    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print("index.html 지역 버튼 링크 연결 완료")

def update_sitemap():
    backup(SITEMAP_FILE)
    today = date.today().isoformat()

    if SITEMAP_FILE.exists():
        xml = SITEMAP_FILE.read_text(encoding="utf-8")
    else:
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'

    for city_name, city_full, slug, keywords in CITY_PAGES:
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
    create_city_pages()
    update_index_links()
    update_sitemap()
    print("완료")
    print(f"확인 예시: {SITE_URL}/regions/changwon.html")
    print("기존 index.html 스타일과 상담접수폼을 그대로 사용합니다.")

if __name__ == "__main__":
    main()
