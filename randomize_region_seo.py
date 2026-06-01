from pathlib import Path
import re
import random

REGIONS = Path("regions")

title_patterns = [
    "{r} 유품정리 상담 안내",
    "{r} 유품정리 비용과 작업 범위",
    "{r} 고독사청소 특수청소 안내",
    "{r} 빈집정리 폐기물처리 상담",
    "{r} 유품정리 전문 작업 정보",
    "{r} 유품정리 전 확인사항",
]

desc_patterns = [
    "{r} 유품정리 상담과 방문 견적 안내.",
    "{r} 고독사청소 특수청소 빈집정리 가능.",
    "{r} 폐기물처리와 유품정리 작업 안내.",
    "{r} 현장 상황에 맞는 정리 서비스 제공.",
    "{r} 장기 방치 공간 정리 상담 가능.",
]

area_features = {
    "동읍":"단독주택 비중이 높은 지역입니다.",
    "북면":"전원주택과 창고 정리 의뢰가 많은 지역입니다.",
    "대산면":"농촌형 주거지역 특성이 있습니다.",
    "장유":"아파트 중심의 신도시 지역입니다.",
    "덕산동":"원룸과 소형 주거시설이 많은 지역입니다.",
}
def get_feature(name):
    for key, value in area_features.items():
        if key in name:
            return value

    return "주거 형태가 다양한 지역입니다."
def make_article(region):
    feature = get_feature(region)

    return f"""
<h2>{region} 유품정리 현장 이야기</h2>

<p>{feature}</p>

<p>{region}에서는 유품정리, 빈집정리, 고독사청소 문의가 꾸준히 발생합니다.</p>

<p>현장마다 짐의 양과 상태가 달라 작업 범위도 달라질 수 있습니다.</p>

<h3>작업 전 확인 사항</h3>

<ul>
<li>귀중품 분류</li>
<li>폐기물 처리 계획</li>
<li>소독 필요 여부</li>
<li>반출 동선 확인</li>
</ul>

<p>인근 지역 사례도 함께 참고하면 작업 범위나 비용을 비교하는 데 도움이 될 수 있습니다.</p>
"""

# ===========================
# 실제 HTML 파일 수정
# ===========================

for file_path in REGIONS.glob("*.html"):

    html = file_path.read_text(encoding="utf-8")

    # 파일명에서 지역명 추출
    match = re.search(r"<h1>(.*?)</h1>", html, re.S)

    if match:
        region_name = re.sub(r"<.*?>", "", match.group(1)).strip()
    else:
        region_name = file_path.stem

    # title 변경
    new_title = random.choice(title_patterns).format(r=region_name)

    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{new_title}</title>",
        html,
        flags=re.S
    )

    # description 변경
    new_desc = random.choice(desc_patterns).format(r=region_name)

    html = re.sub(
        r'<meta[^>]*name="description"[^>]*content="[^"]*"[^>]*>',
        f'<meta name="description" content="{new_desc}">',
        html,
        flags=re.S
    )

    # SEO 본문 교체
    article = make_article(region_name)

    html = re.sub(
        r'<!-- SEO_ARTICLE_START -->.*?<!-- SEO_ARTICLE_END -->',
        f'<!-- SEO_ARTICLE_START -->\n{article}\n<!-- SEO_ARTICLE_END -->',
        html,
        flags=re.S
    )

    file_path.write_text(html, encoding="utf-8")

    print("수정 완료:", file_path.name)

print("\n모든 지역 페이지 SEO 랜덤화 완료")