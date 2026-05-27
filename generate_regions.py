from pathlib import Path
import re
from datetime import date

# ==========================================================
# 가족애유품정리 하위 지역 페이지 자동 생성기
# ----------------------------------------------------------
# 사용법
# 1. index.html : 원본 홈페이지 파일
# 2. regions.txt : 지역명 305개를 한 줄에 하나씩 입력
# 3. python generate_regions.py 실행
# 4. regions 폴더에 하위 지역 페이지 자동 생성
# 5. sitemap-regions.xml 자동 생성
# ==========================================================

SITE_URL = "https://gajogae-yupum.netlify.app/"   # 실제 도메인으로 변경하세요.
BRAND = "가족애유품정리"
PHONE = "010-9242-3895"

template_path = Path("index.html")
regions_path = Path("regions.txt")
output_dir = Path("regions")
output_dir.mkdir(exist_ok=True)

def read_regions():
    if not regions_path.exists():
        raise FileNotFoundError("regions.txt 파일이 없습니다.")
    regions = []
    for line in regions_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            regions.append(line)
    return regions

def make_slug(region, index):
    # 한글 파일명도 가능하지만, 서버 호환성을 위해 번호+지역명 방식 사용
    slug = re.sub(r"[^0-9a-zA-Z가-힣]+", "-", region).strip("-")
    return f"{index:03d}-{slug}"

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

def make_region_section(region):
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
        <p>
          갑작스럽게 유품정리가 필요해진 경우 무엇부터 시작해야 할지 막막할 수 있습니다.
          {BRAND}는 {region} 지역 현장 상황에 맞춰 유품 분류, 중요 물품 확인,
          폐기물 정리, 빈집정리까지 함께 도와드립니다.
        </p>
        <p>
          작업 중 통장, 도장, 계약서, 사진, 귀금속, 현금 등 중요한 물품은 별도로 확인 후 전달드리며,
          현장 상태에 따라 고독사청소와 특수청소도 함께 진행 가능합니다.
        </p>
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
"""

def make_region_faq(region):
    return f"""
<section class="region-faq-section" id="region-faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{region} 유품정리 자주 묻는 질문</h2>
      <p>상담 전 많이 문의하시는 내용을 정리했습니다.</p>
    </div>

    <div class="faq">
      <details>
        <summary>{region} 유품정리 비용은 어떻게 정해지나요?</summary>
        <p>공간 크기, 짐의 양, 폐기물 처리량, 엘리베이터 유무, 차량 진입 가능 여부, 소독이나 탈취 필요 여부에 따라 달라집니다.</p>
      </details>
      <details>
        <summary>{region} 당일 상담이나 방문 견적이 가능한가요?</summary>
        <p>현장 일정에 따라 가능 여부가 달라질 수 있습니다. 긴급한 경우 전화 상담으로 먼저 상황을 확인한 뒤 가능한 일정을 안내드립니다.</p>
      </details>
      <details>
        <summary>중요 물품은 따로 확인해주나요?</summary>
        <p>통장, 도장, 사진, 계약서, 귀금속, 현금, 중요 서류 등은 작업 중 별도로 분류하여 확인을 요청드립니다.</p>
      </details>
    </div>
  </div>
</section>
"""

def make_json_ld(region, url):
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
    markers = ['id="process"', '유품정리 진행 과정', '유품정리진행과정', 'id="faq"']
    for marker in markers:
        pos = html.find(marker)
        if pos != -1:
            section_start = html.rfind("<section", 0, pos)
            if section_start != -1:
                return html[:section_start] + block + "\n" + html[section_start:]
            return html[:pos] + block + "\n" + html[pos:]
    return html.replace("</body>", block + "\n</body>", 1)

def make_page(region, slug):
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

    html = re.sub(
        r"<h1>.*?</h1>",
        f"<h1>{region} 유품정리 전문업체<br>{BRAND}</h1>",
        html,
        count=1,
        flags=re.S
    )

    html = re.sub(
        r"(<h1>.*?</h1>\s*)<p>.*?</p>",
        rf"\1<p>{region} 유품정리 · 고독사청소 · 특수청소 · 빈집정리 상담<br>고인의 물건을 정성스럽게 분류하고 중요한 물품은 별도 확인합니다.</p>",
        html,
        count=1,
        flags=re.S
    )

    block = make_region_section(region) + "\n" + make_region_faq(region)
    html = insert_before_process_or_faq(html, block)
    html = html.replace("</head>", make_json_ld(region, url) + "\n</head>", 1)

    return html

def make_sitemap(items):
    today = date.today().isoformat()
    body = []
    for slug, region in items:
        body.append(f"""  <url>
    <loc>{SITE_URL}/regions/{slug}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(body) + """
</urlset>
"""

def main():
    regions = read_regions()
    created = []

    for i, region in enumerate(regions, start=1):
        slug = make_slug(region, i)
        html = make_page(region, slug)
        (output_dir / f"{slug}.html").write_text(html, encoding="utf-8")
        created.append((slug, region))

    Path("sitemap-regions.xml").write_text(make_sitemap(created), encoding="utf-8")

    print(f"완료: {len(created)}개 지역 페이지 생성")
    print("생성 폴더: regions")
    print("사이트맵: sitemap-regions.xml")

if __name__ == "__main__":
    main()
