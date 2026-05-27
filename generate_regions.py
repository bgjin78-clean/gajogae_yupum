from pathlib import Path
import re
import shutil
from datetime import date

SITE_URL = "https://gajogae-yupum.netlify.app"
BRAND = "가족애유품정리"
PHONE = "010-9242-3895"

template_path = Path("index.html")
regions_path = Path("regions.txt")
output_dir = Path("regions")
CLEAN_REGIONS_FOLDER = True

WORD_MAP = {
    "경상남도": "gyeongnam", "경남": "gyeongnam",
    "창원시": "changwon", "의창구": "uichang", "성산구": "seongsan",
    "마산합포구": "masanhappo", "마산회원구": "masanhoewon", "진해구": "jinhae",
    "김해시": "gimhae", "진주시": "jinju", "양산시": "yangsan",
    "거제시": "geoje", "통영시": "tongyeong", "사천시": "sacheon", "밀양시": "miryang",
    "함안군": "haman", "창녕군": "changnyeong", "고성군": "goseong",
    "남해군": "namhae", "하동군": "hadong", "산청군": "sancheong",
    "함양군": "hamyang", "거창군": "geochang", "합천군": "hapcheon", "의령군": "uiryeong",
    "동읍": "dongeup", "북면": "bukmyeon", "대산면": "daesanmyeon",
    "팔룡동": "pallyongdong", "명곡동": "myeonggokdong", "봉림동": "bongnimdong",
    "용지동": "yongjidong", "반송동": "bansongdong", "중앙동": "jungangdong",
    "상남동": "sangnamdong", "사파동": "sapadong", "가음정동": "gaeumjeongdong",
    "성주동": "seongjudong", "웅남동": "ungnamdong",
    "구산면": "gusanmyeon", "진동면": "jindongmyeon", "진북면": "jinbukmyeon",
    "진전면": "jinjeonmyeon", "현동": "hyeondong", "가포동": "gapodong",
    "월영동": "woryeongdong", "문화동": "munhwadong", "반월중앙동": "banwol-jungangdong",
    "완월동": "wanwoldong", "자산동": "jasandong", "교방동": "gyobangdong",
    "오동동": "odongdong", "합포동": "happodong", "산호동": "sanhodong",
    "내서읍": "naeseoeup", "회원동": "hoewondong", "석전동": "seokjeondong",
    "회성동": "hoeseongdong", "양덕동": "yangdeokdong", "합성동": "hapseongdong",
    "구암동": "guamdong", "봉암동": "bongamdong",
    "충무동": "chungmudong", "여좌동": "yeojwadong", "태백동": "taebaekdong",
    "경화동": "gyeonghwadong", "병암동": "byeongamdong", "석동": "seokdong",
    "이동": "idong", "자은동": "jaeundong", "덕산동": "deoksandong",
    "풍호동": "punghodong", "웅천동": "ungcheondong", "웅동": "ungdong",
    "진영읍": "jinyoungeup", "주촌면": "juchonmyeon", "진례면": "jillyemyeon",
    "한림면": "hallimmyeon", "생림면": "saengnimmyeon", "상동면": "sangdongmyeon",
    "대동면": "daedongmyeon", "동상동": "dongsangdong", "회현동": "hoeheondong",
    "부원동": "buwondong", "내외동": "naeoe-dong", "북부동": "bukbudong",
    "칠산서부동": "chilsan-seobudong", "활천동": "hwalcheondong",
    "삼안동": "samandong", "불암동": "buramdong", "장유동": "jangyudong",
    "물금읍": "mulgeumeup", "동면": "dongmyeon", "원동면": "wondongmyeon",
    "상북면": "sangbukmyeon", "하북면": "habukmyeon", "양주동": "yangjudong",
    "삼성동": "samsungdong", "강서동": "gangseodong", "서창동": "seochangdong",
    "소주동": "sojudong", "평산동": "pyeongsandong", "덕계동": "deokgyedong",
}

CHO = ["g","kk","n","d","tt","r","m","b","pp","s","ss","","j","jj","ch","k","t","p","h"]
JUNG = ["a","ae","ya","yae","eo","e","yeo","ye","o","wa","wae","oe","yo","u","wo","we","wi","yu","eu","ui","i"]
JONG = ["","k","k","ks","n","nj","nh","t","l","lk","lm","lb","ls","lt","lp","lh","m","p","ps","t","t","ng","t","t","k","t","p","h"]

def romanize(text):
    result = []
    for ch in text:
        code = ord(ch)
        if 0xAC00 <= code <= 0xD7A3:
            s = code - 0xAC00
            result.append(CHO[s // 588] + JUNG[(s % 588) // 28] + JONG[s % 28])
        elif ch.isalnum():
            result.append(ch.lower())
        else:
            result.append("-")
    return "".join(result)

def make_slug(region, index):
    parts = []
    for word in re.split(r"\s+", region.strip()):
        if word in WORD_MAP:
            parts.append(WORD_MAP[word])
        else:
            matched = False
            for kr, en in [("특별시","si"), ("광역시","si"), ("시","si"), ("군","gun"), ("구","gu"), ("읍","eup"), ("면","myeon"), ("동","dong"), ("리","ri")]:
                if word.endswith(kr) and len(word) > len(kr):
                    parts.append(romanize(word[:-len(kr)]) + en)
                    matched = True
                    break
            if not matched:
                parts.append(romanize(word))
    slug = "-".join(parts)
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return f"{index:03d}-{slug}"

def read_regions():
    if not regions_path.exists():
        raise FileNotFoundError("regions.txt 파일을 찾을 수 없습니다.")
    return [line.strip() for line in regions_path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.strip().startswith("#")]

def replace_meta_name(html, name, content):
    pattern = rf'<meta[^>]+name=["\']{name}["\'][^>]*>'
    tag = f'<meta name="{name}" content="{content}">'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def replace_meta_property(html, prop, content):
    pattern = rf'<meta[^>]+property=["\']{prop}["\'][^>]*>'
    tag = f'<meta property="{prop}" content="{content}">'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def set_canonical(html, url):
    pattern = r'<link[^>]+rel=["\']canonical["\'][^>]*>|<link[^>]+href=["\'][^"\']+["\'][^>]+rel=["\']canonical["\'][^>]*>'
    tag = f'<link rel="canonical" href="{url}">'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, tag, html, count=1, flags=re.I)
    return html.replace("</head>", tag + "\n</head>", 1)

def region_content_block(region):
    return f"""
<section class="region-local-section" id="region-service">
  <div class="wrap">
    <div class="section-title">
      <h2>{region} 유품정리 상담 안내</h2>
      <p>{region} 지역 유품정리, 고독사청소, 특수청소, 빈집정리 상담과 방문 견적을 진행합니다.</p>
    </div>
    <div class="split">
      <div class="panel">
        <h3>{region} 유품정리가 필요한 경우</h3>
        <p>갑작스럽게 유품정리가 필요해진 경우 무엇부터 시작해야 할지 막막할 수 있습니다. {BRAND}는 {region} 지역 현장 상황에 맞춰 유품 분류, 중요 물품 확인, 폐기물 정리, 빈집정리까지 함께 도와드립니다.</p>
        <p>작업 중 통장, 도장, 계약서, 사진, 귀금속, 현금 등 중요한 물품은 별도로 확인 후 전달드리며, 현장 상태에 따라 고독사청소와 특수청소도 함께 진행 가능합니다.</p>
      </div>
      <div class="panel">
        <h3>{region} 주요 서비스</h3>
        <div class="keyword-box">
          <div>{region} 유품정리</div>
          <div>{region} 고독사청소</div>
          <div>{region} 특수청소</div>
          <div>{region} 빈집정리</div>
          <div>{region} 폐기물처리</div>
          <div>{region} 방문견적</div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="region-faq-section" id="region-faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{region} 유품정리 자주 묻는 질문</h2>
      <p>상담 전 많이 문의하시는 내용을 정리했습니다.</p>
    </div>
    <div class="faq">
      <details><summary>{region} 유품정리 비용은 어떻게 정해지나요?</summary><p>공간 크기, 짐의 양, 폐기물 처리량, 엘리베이터 유무, 차량 진입 가능 여부, 소독이나 탈취 필요 여부에 따라 달라집니다.</p></details>
      <details><summary>{region} 당일 상담이나 방문 견적이 가능한가요?</summary><p>현장 일정에 따라 가능 여부가 달라질 수 있습니다. 긴급한 경우 전화 상담으로 먼저 상황을 확인한 뒤 가능한 일정을 안내드립니다.</p></details>
      <details><summary>중요 물품은 따로 확인해주나요?</summary><p>통장, 도장, 사진, 계약서, 귀금속, 현금, 중요 서류 등은 작업 중 별도로 분류하여 확인을 요청드립니다.</p></details>
    </div>
  </div>
</section>
"""

def internal_links_block(current_index, items, count=12):
    total = len(items)
    if total <= 1:
        return ""
    selected = []
    for offset in range(1, 7):
        selected.append(items[(current_index + offset) % total])
    step = max(1, total // 6)
    for k in range(0, total, step):
        selected.append(items[k])
        if len(selected) >= count + 3:
            break
    clean = []
    seen = set()
    current_slug = items[current_index]["slug"]
    for item in selected:
        if item["slug"] == current_slug or item["slug"] in seen:
            continue
        seen.add(item["slug"])
        clean.append(item)
        if len(clean) >= count:
            break
    links = "\n".join([f'        <a href="/regions/{item["slug"]}.html">{item["name"]} 유품정리</a>' for item in clean])
    return f"""
<section class="near-region-links" id="near-regions">
  <div class="wrap">
    <div class="section-title">
      <h2>함께 확인하면 좋은 경남 유품정리 지역</h2>
      <p>가까운 지역의 유품정리, 고독사청소, 특수청소 상담 페이지도 함께 확인해보세요.</p>
    </div>
    <div class="regions">
{links}
    </div>
  </div>
</section>
"""

def json_ld(region, url):
    return f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{region} 유품정리",
  "provider": {{
    "@type": "LocalBusiness",
    "name": "{BRAND}",
    "telephone": "+82-10-9242-3895",
    "areaServed": "{region}"
  }},
  "serviceType": ["유품정리", "고독사청소", "특수청소", "빈집정리", "폐기물처리"],
  "url": "{url}",
  "description": "{region} 유품정리, 고독사청소, 특수청소, 빈집정리 상담과 방문 견적을 진행합니다."
}}
</script>
"""

def insert_before_process_or_faq(html, block):
    for marker in ['id="process"', '유품정리 진행 과정', '유품정리진행과정', 'id="faq"']:
        pos = html.find(marker)
        if pos != -1:
            start = html.rfind("<section", 0, pos)
            if start != -1:
                return html[:start] + block + "\n" + html[start:]
            return html[:pos] + block + "\n" + html[pos:]
    return html.replace("</body>", block + "\n</body>", 1)

def insert_near_region_links(html, block):
    for marker in ['id="contact"', 'class="final"', '<footer']:
        pos = html.find(marker)
        if pos != -1:
            start = html.rfind("<section", 0, pos)
            if marker != '<footer' and start != -1:
                return html[:start] + block + "\n" + html[start:]
            return html[:pos] + block + "\n" + html[pos:]
    return html.replace("</body>", block + "\n</body>", 1)

def make_page(region, slug, index, items):
    url = f"{SITE_URL}/regions/{slug}.html"
    html = template_path.read_text(encoding="utf-8")
    title = f"{region} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc = f"{region} 유품정리 전문 {BRAND}입니다. {region} 고독사청소, 특수청소, 빈집정리, 폐기물처리 상담과 방문 견적을 진행합니다."
    keywords = f"{region} 유품정리,{region} 유품정리 업체,{region} 고독사청소,{region} 특수청소,{region} 빈집정리,{region} 폐기물처리,{BRAND}"

    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)
    html = replace_meta_name(html, "description", desc)
    html = replace_meta_name(html, "keywords", keywords)
    html = set_canonical(html, url)
    html = replace_meta_property(html, "og:title", title)
    html = replace_meta_property(html, "og:description", desc)
    html = replace_meta_property(html, "og:url", url)
    html = replace_meta_name(html, "twitter:title", title)
    html = replace_meta_name(html, "twitter:description", desc)

    html = re.sub(r"<h1>.*?</h1>", f"<h1>{region} 유품정리 전문업체<br>{BRAND}</h1>", html, count=1, flags=re.S)
    html = re.sub(r"(<h1>.*?</h1>\s*)<p>.*?</p>", rf"\1<p>{region} 유품정리 · 고독사청소 · 특수청소 · 빈집정리 상담<br>고인의 물건을 정성스럽게 분류하고 중요한 물품은 별도 확인합니다.</p>", html, count=1, flags=re.S)

    html = insert_before_process_or_faq(html, region_content_block(region))
    html = insert_near_region_links(html, internal_links_block(index, items))
    html = html.replace("</head>", json_ld(region, url) + "\n</head>", 1)
    return html

def make_regions_index(items):
    links = "\n".join([f'<a href="/regions/{item["slug"]}.html">{item["name"]} 유품정리</a>' for item in items])
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>경남 유품정리 지역 전체 목록 | {BRAND}</title>
<meta name="description" content="경남 전지역 유품정리, 고독사청소, 특수청소, 빈집정리 상담 가능 지역 전체 목록입니다.">
<link rel="canonical" href="{SITE_URL}/regions/">
<style>
body{{margin:0;font-family:Apple SD Gothic Neo,Malgun Gothic,Arial,sans-serif;background:#fbf7ef;color:#172b3a;line-height:1.7}}
.wrap{{width:min(1120px,92%);margin:auto;padding:60px 0}}
h1{{font-size:40px;letter-spacing:-.06em}}
p{{color:#65717c}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:30px}}
a{{display:block;background:#fff;border:1px solid #e7e1d7;border-radius:14px;padding:14px 16px;color:#172b3a;text-decoration:none;font-weight:700}}
a:hover{{background:#172b3a;color:#fff}}
@media(max-width:800px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="wrap">
<h1>경남 유품정리 지역 전체 목록</h1>
<p>아래 지역을 선택하면 해당 지역 유품정리 상담 페이지로 이동합니다.</p>
<div class="grid">
{links}
</div>
</div>
</body>
</html>"""

def make_sitemap(items):
    today = date.today().isoformat()
    url_blocks = []
    url_blocks.append(f"""  <url>
    <loc>{SITE_URL}/regions/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>""")
    for item in items:
        url_blocks.append(f"""  <url>
    <loc>{SITE_URL}/regions/{item['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(url_blocks) + """
</urlset>
"""

def main():
    if not template_path.exists():
        raise FileNotFoundError("index.html 파일을 찾을 수 없습니다.")
    regions = read_regions()
    if CLEAN_REGIONS_FOLDER and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(exist_ok=True)

    items = []
    for i, region in enumerate(regions, start=1):
        items.append({"name": region, "slug": make_slug(region, i), "index": i})

    redirects = []
    for item in items:
        i = item["index"]
        region = item["name"]
        slug = item["slug"]
        old_slug = f"{i:03d}-" + re.sub(r"[^0-9a-zA-Z가-힣]+", "-", region).strip("-")
        redirects.append(f"/regions/{old_slug}.html  /regions/{slug}.html  301")
        html = make_page(region, slug, i - 1, items)
        (output_dir / f"{slug}.html").write_text(html, encoding="utf-8")

    (output_dir / "index.html").write_text(make_regions_index(items), encoding="utf-8")
    Path("sitemap-regions.xml").write_text(make_sitemap(items), encoding="utf-8")
    Path("_redirects").write_text("\n".join(redirects) + "\n", encoding="utf-8")

    print(f"완료: {len(items)}개 지역 페이지 생성")
    print("내부링크 자동화: 완료")
    print(f"지역 목록 페이지: {SITE_URL}/regions/")
    if items:
        print(f"예시 페이지: {SITE_URL}/regions/{items[0]['slug']}.html")

if __name__ == "__main__":
    main()
