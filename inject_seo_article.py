from pathlib import Path
import re

REGIONS_DIR = Path("regions")

START = "<!-- SEO_ARTICLE_START -->"
END = "<!-- SEO_ARTICLE_END -->"

def get_region_name(html):
    match = re.search(r"<h1>(.*?)</h1>", html, re.S)
    if not match:
        return "경남 유품정리"
    text = re.sub(r"<.*?>", "", match.group(1))
    return text.strip()

def make_article(region_name):
    return f"""
<h2>{region_name} 현장에서 확인해야 할 부분</h2>

<p>{region_name}는 단순히 짐을 정리하는 작업으로만 보기 어렵습니다. 현장에 따라 유품 분류, 폐기물 처리, 냄새 관리, 청소 범위가 모두 달라질 수 있습니다.</p>

<p>특히 오래된 주택이나 장기간 비워진 공간은 겉으로 보기보다 내부 상태가 좋지 않은 경우가 있습니다. 서랍 안쪽, 장롱 뒤, 베란다 쪽에 습기나 곰팡이가 남아 있는 경우도 있습니다.</p>

<h3>{region_name} 작업 전 자주 확인하는 것</h3>

<ul>
  <li>중요 서류, 통장, 도장, 귀중품 분류 여부</li>
  <li>폐기물 양과 반출 동선</li>
  <li>엘리베이터 사용 가능 여부</li>
  <li>냄새 제거와 소독 작업 필요 여부</li>
  <li>유족이 직접 확인해야 할 물품 여부</li>
</ul>

<p>현장에서 가족분들이 가장 많이 놀라는 부분은 생각보다 버릴 물건이 많다는 점입니다. 작은 방 하나라고 해도 생활용품, 가구, 의류, 서류가 함께 나오면 작업 시간이 길어질 수 있습니다.</p>

<h3>일반 청소와 다른 점</h3>

<p>유품정리는 일반 청소처럼 보이는 부분만 정리하고 끝나는 일이 아닙니다. 고인의 물건을 확인하고, 남겨야 할 것과 처리해야 할 것을 구분하는 과정이 먼저입니다.</p>

<p>상황에 따라 고독사청소, 특수청소, 빈집정리, 폐기물처리까지 함께 진행해야 할 수 있습니다. 그래서 현장 확인 후 작업 범위를 정하는 것이 가장 안전합니다.</p>

<p>인근 지역 사례도 함께 참고하면 작업 범위나 비용을 비교하는 데 도움이 될 수 있습니다.</p>
"""

for file_path in REGIONS_DIR.glob("*.html"):
    if file_path.name.endswith(".backup"):
        continue

    html = file_path.read_text(encoding="utf-8")

    if START not in html or END not in html:
        print(f"마커 없음: {file_path.name}")
        continue

    region_name = get_region_name(html)
    article = make_article(region_name)

    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.S
    )

    replacement = f"{START}\n{article}\n{END}"

    html = pattern.sub(replacement, html)

    file_path.write_text(html, encoding="utf-8")
    print(f"본문 삽입 완료: {file_path.name} - {region_name}")