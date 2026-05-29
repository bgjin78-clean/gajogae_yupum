from pathlib import Path
import shutil
from datetime import date

SITE_URL = "https://gajogae-yupum.netlify.app"
BRAND = "가족애유품정리"
PHONE = "010-9242-3895"

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
        backup_path = path.with_name(path.stem + ".backup" + path.suffix)
        if not backup_path.exists():
            shutil.copy2(path, backup_path)

def read_regions():
    if not REGIONS_FILE.exists():
        return []
    return [line.strip() for line in REGIONS_FILE.read_text(encoding="utf-8").splitlines() if line.strip() and not line.strip().startswith("#")]

def find_existing_page(region):
    if not REGIONS_DIR.exists():
        return None
    for file in sorted(REGIONS_DIR.glob("*.html")):
        if file.name == "index.html":
            continue
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if region in text:
            return file.name
    return None

def make_child_links(keywords, all_regions):
    links = []
    for region in all_regions:
        if any(keyword in region for keyword in keywords):
            filename = find_existing_page(region)
            if filename:
                links.append(f'<a href="/regions/{filename}">{region} 유품정리</a>')
        if len(links) >= 40:
            break
    if not links:
        links.append('<a href="/regions/">경남 유품정리 전체 지역 보기</a>')
    return "\n".join(links)

def make_page(city_name, city_full, slug, keywords, all_regions):
    url = f"{SITE_URL}/regions/{slug}.html"
    title = f"{city_name} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc = f"{city_name} 유품정리 전문 {BRAND}입니다. {city_name} 고독사청소, 특수청소, 빈집정리, 폐기물처리 상담과 방문 견적을 진행합니다."
    links = make_child_links(keywords, all_regions)

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{city_name} 유품정리,{city_name} 유품정리 업체,{city_name} 고독사청소,{city_name} 특수청소,{city_name} 빈집정리,{BRAND}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:Apple SD Gothic Neo,Malgun Gothic,Arial,sans-serif;background:#fbf7ef;color:#172b3a;line-height:1.75}}
a{{color:inherit;text-decoration:none}}
.wrap{{width:min(1120px,92%);margin:auto}}
.header{{background:#fff;border-bottom:1px solid #e7e1d7;position:sticky;top:0;z-index:10}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:18px 0}}
.logo{{font-weight:900;font-size:22px}}
.phone{{background:#172b3a;color:#fff;border-radius:999px;padding:12px 18px;font-weight:900}}
.hero{{background:linear-gradient(135deg,rgba(23,43,58,.94),rgba(35,93,114,.86));color:#fff;padding:86px 0}}
.hero h1{{font-size:48px;line-height:1.18;letter-spacing:-.07em;margin:0 0 18px}}
.hero p{{font-size:20px;color:rgba(255,255,255,.86);max-width:780px}}
.badge{{display:inline-block;background:rgba(216,170,90,.18);border:1px solid rgba(216,170,90,.5);border-radius:999px;padding:7px 13px;margin-bottom:16px;font-weight:900}}
.section{{padding:70px 0}}
.section h2{{font-size:36px;letter-spacing:-.06em;text-align:center;margin:0 0 14px}}
.lead{{text-align:center;color:#65717c;margin-bottom:30px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.card{{background:#fff;border:1px solid #e7e1d7;border-radius:22px;padding:24px;box-shadow:0 12px 30px rgba(23,43,58,.07)}}
.card h3{{margin:0 0 10px;color:#172b3a}}
.links{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:25px}}
.links a{{display:block;background:#fff;border:1px solid #e7e1d7;border-radius:999px;padding:12px 15px;text-align:center;font-weight:800}}
.links a:hover{{background:#172b3a;color:#fff}}
.cta{{background:#fff;padding:45px 0;border-top:1px solid #e7e1d7}}
.cta-box{{display:flex;justify-content:space-between;align-items:center;gap:18px;background:#f5efe3;border-radius:24px;padding:26px}}
.btn{{background:#d8aa5a;border-radius:999px;padding:14px 22px;font-weight:900}}
@media(max-width:820px){{.hero h1{{font-size:36px}}.grid,.links{{grid-template-columns:1fr}}.cta-box{{display:block}}.btn{{display:inline-block;margin-top:14px}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{city_name} 유품정리","provider":{{"@type":"LocalBusiness","name":"{BRAND}","telephone":"+82-10-9242-3895","areaServed":"{city_full}"}},"serviceType":["유품정리","고독사청소","특수청소","빈집정리","폐기물처리"],"url":"{url}","description":"{desc}"}}
</script>
</head>
<body>
<header class="header"><div class="wrap nav"><a href="/" class="logo">{BRAND}</a><a href="tel:01092423895" class="phone">{PHONE}</a></div></header>
<section class="hero"><div class="wrap"><span class="badge">{city_name} 전지역 상담 가능</span><h1>{city_name} 유품정리 업체<br>{BRAND}</h1><p>{city_name} 유품정리, 고독사청소, 특수청소, 빈집정리까지 현장 상황에 맞춰 차분하고 책임감 있게 진행합니다.</p></div></section>
<section class="section"><div class="wrap"><h2>{city_name} 유품정리가 필요할 때</h2><p class="lead">고인의 물건을 정리하는 일은 단순한 청소가 아니라 중요한 물품을 확인하고 공간을 정돈하는 과정입니다.</p><div class="grid"><div class="card"><h3>중요 물품 확인</h3><p>통장, 도장, 계약서, 사진, 귀금속, 현금 등 중요한 물품은 별도로 분류하여 확인을 요청드립니다.</p></div><div class="card"><h3>현장 맞춤 정리</h3><p>아파트, 단독주택, 빌라, 원룸 등 현장 구조와 물품 양에 맞춰 작업 순서를 정합니다.</p></div><div class="card"><h3>폐기물 처리와 정돈</h3><p>유품 분류 후 남은 폐기물 처리, 빈집정리, 필요 시 소독과 탈취까지 함께 안내합니다.</p></div></div></div></section>
<section class="section" style="background:#fff"><div class="wrap"><h2>{city_name} 세부 지역 유품정리 안내</h2><p class="lead">{city_name} 내 읍·면·동 상세 페이지로 이동할 수 있습니다.</p><div class="links">{links}</div></div></section>
<section class="section"><div class="wrap"><h2>{city_name} 유품정리 자주 묻는 질문</h2><div class="grid"><div class="card"><h3>{city_name} 유품정리 비용은 어떻게 정해지나요?</h3><p>공간 크기, 짐의 양, 폐기물 처리량, 차량 진입 가능 여부, 소독이나 탈취 필요 여부에 따라 달라집니다.</p></div><div class="card"><h3>방문 견적이 가능한가요?</h3><p>현장 일정에 따라 방문 상담이 가능하며, 긴급한 경우 전화로 먼저 상황을 확인합니다.</p></div><div class="card"><h3>고독사청소도 가능한가요?</h3><p>일반 유품정리와 달리 소독, 탈취, 오염 정리 등이 필요할 수 있어 현장 상태를 확인 후 안내드립니다.</p></div></div></div></section>
<section class="cta"><div class="wrap cta-box"><div><h2 style="text-align:left;margin:0 0 8px">{city_name} 유품정리 상담</h2><p style="margin:0;color:#65717c">상담을 통해 현장 상황과 필요한 정리 범위를 먼저 확인해드립니다.</p></div><a href="tel:01092423895" class="btn">전화 상담</a></div></section>
</body>
</html>"""
    return html

def create_city_pages():
    REGIONS_DIR.mkdir(exist_ok=True)
    all_regions = read_regions()
    for city_name, city_full, slug, keywords in CITY_PAGES:
        (REGIONS_DIR / f"{slug}.html").write_text(make_page(city_name, city_full, slug, keywords, all_regions), encoding="utf-8")
    print(f"시군 대표 페이지 {len(CITY_PAGES)}개 생성 완료")

def update_index_links():
    if not INDEX_FILE.exists():
        print("index.html 없음: 버튼 링크 연결 건너뜀")
        return

    backup(INDEX_FILE)
    html = INDEX_FILE.read_text(encoding="utf-8")
    changed = 0

    for city_name, city_full, slug, keywords in CITY_PAGES:
        plain = f"{city_name} 유품정리"
        linked = f'<a href="/regions/{slug}.html">{city_name} 유품정리</a>'

        if linked in html:
            continue

        # 버튼 안의 텍스트만 있는 경우 링크로 변환
        if plain in html:
            html = html.replace(plain, linked, 1)
            changed += 1

    INDEX_FILE.write_text(html, encoding="utf-8")
    print(f"index.html 지역 버튼 링크 연결 {changed}개 변경")

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

if __name__ == "__main__":
    main()
