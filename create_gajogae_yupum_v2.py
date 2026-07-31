from pathlib import Path
from datetime import date
import html
import random

SITE_URL = "https://www.gajogae-yupum.com"
BRAND = "가족애유품정리"
PHONE = "010-9242-3895"

PUBLIC_KEY = "JKsVOKPtnWHIr2BCV"
SERVICE_ID = "gajogae-yupum"
TEMPLATE_ID = "template_wwbariw"

REGIONS_DIR = Path("regions")

BACKLINKS = [
    ("가족애폐기물처리", "https://www.gajogae-waste.com/"),
    ("서울 가족애유품정리", "https://www.seoul.gajogae-yupum.com/"),
    ("경기 가족애유품정리", "https://www.gyeonggi.gajogae-yupum.com/"),
]

REGIONS = [
    ("경남", "gyeongnam", "경남", "경남 전지역 유품정리 대표 페이지"),
    ("창원", "changwon", "경남", "의창구와 성산구 중심의 아파트·주택 유품정리"),
    ("마산", "masan", "경남", "마산합포구와 마산회원구 중심의 오래된 주택 정리"),
    ("진해", "jinhae", "경남", "진해구 중심의 주택·아파트 유품정리"),
    ("김해", "gimhae", "경남", "장유, 율하, 진영 등 아파트와 주택 정리"),
    ("진주", "jinju", "경남", "도심 아파트와 외곽 주택 유품정리"),
    ("양산", "yangsan", "경남", "물금신도시와 구도심 주거지 유품정리"),
    ("거제", "geoje", "경남", "아파트와 원룸, 조선업 주거지 정리"),
    ("통영", "tongyeong", "경남", "해안가 주택과 습기·냄새 관리가 필요한 현장"),
    ("사천", "sacheon", "경남", "산업단지와 주거지가 함께 있는 지역"),
    ("밀양", "miryang", "경남", "농촌형 주택과 오래된 단독주택 정리"),
    ("함안", "haman", "경남", "농촌형 주거지와 오래된 주택 정리"),
    ("창녕", "changnyeong", "경남", "읍면 단위 주거지와 오래된 주택 정리"),
    ("고성", "goseong", "경남", "단독주택과 농촌형 주거지 정리"),
    ("남해", "namhae", "경남", "해안 지역 특성과 오래된 주택 정리"),
    ("하동", "hadong", "경남", "농촌형 주택과 외곽 주거지 정리"),
    ("산청", "sancheong", "경남", "단독주택과 농촌형 주거지 정리"),
    ("함양", "hamyang", "경남", "오래된 단독주택과 농촌형 주거지 정리"),
    ("거창", "geochang", "경남", "읍내 아파트와 외곽 단독주택 정리"),
    ("합천", "hapcheon", "경남", "농촌형 주택과 창고 정리가 함께 나오는 지역"),
    ("의령", "uiryeong", "경남", "단독주택과 오래된 주거지가 많은 지역"),

    ("부산", "busan", "부산", "부산 전지역 유품정리 대표 페이지"),
    ("부산 중구", "busan-junggu", "부산", "중구 도심형 주거지 유품정리"),
    ("부산 서구", "busan-seogu", "부산", "서구 오래된 주택과 아파트 유품정리"),
    ("부산 동구", "busan-donggu", "부산", "동구 도심 주거지 유품정리"),
    ("부산 영도구", "busan-yeongdo", "부산", "영도구 해안가 주택 유품정리"),
    ("부산 부산진구", "busan-busanjin", "부산", "부산진구 아파트·빌라 유품정리"),
    ("부산 동래구", "busan-dongnae", "부산", "동래구 주택과 아파트 유품정리"),
    ("부산 남구", "busan-namgu", "부산", "남구 주거지 유품정리"),
    ("부산 북구", "busan-bukgu", "부산", "북구 아파트와 주택 유품정리"),
    ("부산 해운대구", "busan-haeundae", "부산", "해운대구 아파트 유품정리"),
    ("부산 사하구", "busan-saha", "부산", "사하구 주택·아파트 유품정리"),
    ("부산 금정구", "busan-geumjeong", "부산", "금정구 단독주택과 아파트 유품정리"),
    ("부산 강서구", "busan-gangseo", "부산", "강서구 외곽 주택 유품정리"),
    ("부산 연제구", "busan-yeonje", "부산", "연제구 도심형 유품정리"),
    ("부산 수영구", "busan-suyeong", "부산", "수영구 아파트 중심 유품정리"),
    ("부산 사상구", "busan-sasang", "부산", "사상구 주택과 상가주택 유품정리"),
    ("부산 기장군", "busan-gijang", "부산", "기장군 주택과 외곽 지역 유품정리"),

    ("울산", "ulsan", "울산", "울산 전지역 유품정리 대표 페이지"),
    ("울산 중구", "ulsan-junggu", "울산", "중구 도심 주거지 유품정리"),
    ("울산 남구", "ulsan-namgu", "울산", "남구 아파트와 주택 유품정리"),
    ("울산 동구", "ulsan-donggu", "울산", "동구 주거지 유품정리"),
    ("울산 북구", "ulsan-bukgu", "울산", "북구 아파트·단독주택 유품정리"),
    ("울산 울주군", "ulsan-ulju", "울산", "울주군 외곽 주택과 농촌형 주거지 유품정리"),
]


def esc(text):
    return html.escape(str(text))


def css():
    return """
<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Arial,'Noto Sans KR',sans-serif;color:#1f1f1f;background:#faf8f3;line-height:1.75}
a{text-decoration:none;color:inherit}
img{max-width:100%;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
header{background:#fff;border-bottom:1px solid #eee;position:sticky;top:0;z-index:20}
.nav{display:flex;justify-content:space-between;align-items:center;padding:14px 0}
.logo{font-weight:900;font-size:22px;color:#163552}
nav a{margin-left:18px;font-weight:800;font-size:15px}
.hero{background:linear-gradient(rgba(0,0,0,.54),rgba(0,0,0,.62)),url('/images/main/main-banner.png') center/cover no-repeat;color:#fff;padding:96px 0;text-align:center}
.hero h1{font-size:46px;line-height:1.22;margin:18px 0}
.hero p{font-size:19px;max-width:850px;margin:0 auto}
.badge{display:inline-block;background:#d8b36a;color:#111;padding:7px 15px;border-radius:999px;font-weight:900}
.btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:28px}
.btn{display:inline-block;padding:15px 24px;border-radius:13px;font-weight:900}
.primary{background:#d8b36a;color:#111}
.secondary{background:#fff;color:#111}
.dark{background:#163552;color:#fff}
section{padding:72px 0}
.section-title{text-align:center;margin-bottom:36px}
.section-title h2{font-size:32px;margin:0 0 10px;color:#1b2f43}
.section-title p{margin:0;color:#666}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.card{background:#fff;border:1px solid #eee;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(0,0,0,.05)}
.card h3{margin-top:0;color:#163552}
.card strong{color:#9a6b1f}
.price{background:#fff}
.price-box{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.price-card{background:#fff;border:1px solid #e7decf;border-radius:20px;padding:26px}
.price-card h3{margin-top:0;color:#163552}
.price-num{font-size:30px;font-weight:900;color:#9a6b1f;margin:12px 0}
.seo{background:#fff}
.seo h2{font-size:31px;color:#163552}
.seo h3{margin-top:34px;color:#163552}
.seo ul{background:#faf8f3;border-radius:14px;padding:22px 30px}
.photo-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.photo{background:#ddd;border-radius:18px;overflow:hidden;min-height:190px}
.photo img{width:100%;height:230px;object-fit:cover}
.case-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.case{background:#fff;border:1px solid #eee;border-radius:20px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.05)}
.case img{height:220px;width:100%;object-fit:cover}
.case div{padding:22px}
.review{background:#f1eadc}
.review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.review-card{background:#fff;border-radius:18px;padding:24px;border:1px solid #eadfcb}
.step{display:flex;gap:16px;background:#fff;border:1px solid #eee;border-radius:18px;padding:22px;margin-bottom:14px}
.num{width:44px;height:44px;border-radius:50%;background:#163552;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;flex-shrink:0}
.regions{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
.regions a{display:block;background:#fff;border:1px solid #ddd;border-radius:12px;padding:13px;text-align:center;font-weight:800}
.form-section{background:#163552;color:#fff}
.form-box{background:#fff;color:#222;border-radius:20px;padding:26px;max-width:760px;margin:0 auto}
.form-box input,.form-box select,.form-box textarea{width:100%;padding:14px;margin:8px 0 14px;border:1px solid #ddd;border-radius:10px;font-size:16px}
.form-box button{width:100%;padding:16px;background:#d8b36a;border:0;border-radius:12px;font-size:18px;font-weight:900;cursor:pointer}
.faq details{background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;margin-bottom:12px}
.faq summary{font-weight:900;cursor:pointer}
.related{background:#fff}
.backlinks{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.backlinks a{background:#163552;color:#fff;padding:13px 18px;border-radius:12px;font-weight:900}
footer{background:#111;color:#ccc;text-align:center;padding:30px 0;font-size:14px}
@media(max-width:700px){
.hero{padding:74px 0}
.hero h1{font-size:32px}
.nav{flex-direction:column;gap:10px}
nav a{margin:0 8px}
section{padding:56px 0}
}
</style>
"""


def head(title, desc, url):
    return f"""<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/images/main/favicon.png">
<meta property="og:locale" content="ko_KR">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/images/main/main-banner.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE_URL}/images/main/main-banner.png">
{css()}
</head>"""

def local_business_schema(region_name, url):
    return f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{BRAND}",
  "url": "{url}",
  "telephone": "{PHONE}",
  "areaServed": "{region_name}",
  "description": "{region_name} 유품정리, 고독사청소, 특수청소, 빈집정리 상담을 진행합니다.",
  "image": "{SITE_URL}/images/main/main-banner.png",
  "priceRange": "상담 후 안내",
  "address": {{
    "@type": "PostalAddress",
    "addressCountry": "KR",
    "addressRegion": "{region_name}"
  }},
  "makesOffer": {{
    "@type": "Offer",
    "itemOffered": {{
      "@type": "Service",
      "name": "{region_name} 유품정리",
      "serviceType": "유품정리, 고독사청소, 특수청소, 빈집정리"
    }}
  }}
}}
</script>
'''

def header():
    return f"""
<header>
  <div class="wrap nav">
    <a class="logo" href="/">{BRAND}</a>
    <nav>
      <a href="/#service">서비스</a>
      <a href="/#price">비용안내</a>
      <a href="/#photos">작업사진</a>
      <a href="/#regions">지역</a>
      <a href="/#contact">상담접수</a>
    </nav>
  </div>
</header>
"""


def footer():
    return f"""
<footer>
  <div class="wrap">
    <p>{BRAND} · 유품정리 · 고독사청소 · 특수청소 · 빈집정리</p>
    <p>상담전화 {PHONE}</p>
  </div>
</footer>
"""


def backlink_section():
    links = "\n".join([f'<a href="{url}" target="_blank" rel="noopener">{label}</a>' for label, url in BACKLINKS])
    return f"""
<section class="related" id="related">
  <div class="wrap">
    <div class="section-title">
      <h2>관련 서비스</h2>
      <p>필요한 정리 유형에 맞춰 관련 페이지도 함께 확인하실 수 있습니다.</p>
    </div>
    <div class="backlinks">
      {links}
    </div>
  </div>
</section>
"""
def form_section(region):
    return f"""
<section class="form-section" id="contact">
  <div class="wrap">
    <div class="section-title">
      <h2>유품정리 상담접수</h2>
      <p>확인 후 빠르게 연락드리겠습니다.</p>
    </div>

    <form class="form-box request-form-box">
      <input type="text" name="이름" placeholder="이름" required>
      <input type="tel" name="연락처" placeholder="연락처" required>
      <input type="text" name="주소" placeholder="주소 또는 지역명" value="{esc(region)}">

      <select name="서비스">
        <option value="유품정리">유품정리</option>
        <option value="고독사청소">고독사청소</option>
        <option value="특수청소">특수청소</option>
        <option value="빈집정리">빈집정리</option>
      </select>

      <textarea name="내용" rows="5" placeholder="상담 내용을 입력해주세요"></textarea>

      <button type="submit">상담 접수하기</button>
    </form>
  </div>
</section>
"""


def email_script():
    return f"""
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

<script>
(function(){{
  emailjs.init("{PUBLIC_KEY}");

  document.addEventListener("DOMContentLoaded", function () {{

    document.querySelectorAll(".request-form-box").forEach(function(form){{

      form.addEventListener("submit", function(e){{
        e.preventDefault();

        const btn = form.querySelector("button[type='submit']");
        const originalText = btn.textContent;

        btn.disabled = true;
        btn.textContent = "접수 중입니다...";

        const params = {{
          title: "[가족애유품정리] 상담접수",

          site_name: "가족애유품정리",

          name:
            form.querySelector('[name="이름"]')?.value || "",

          email:
            "bg.jin78@gmail.com",

          message:
            "접수 사이트: 가족애유품정리\\n\\n" +

            "이름: " +
            (form.querySelector('[name="이름"]')?.value || "") +
            "\\n\\n" +

            "연락처: " +
            (form.querySelector('[name="연락처"]')?.value || "") +
            "\\n\\n" +

            "주소: " +
            (form.querySelector('[name="주소"]')?.value || "") +
            "\\n\\n" +

            "요청 서비스: " +
            (form.querySelector('[name="서비스"]')?.value || "") +
            "\\n\\n" +

            "상담 내용:\\n" +
            (form.querySelector('[name="내용"]')?.value || "") +
            "\\n\\n" +

            "접수 페이지:\\n" +
            window.location.href
        }};

        emailjs.send(
          "{SERVICE_ID}",
          "{TEMPLATE_ID}",
          params
        )
        .then(function(){{
          alert("상담 접수가 완료되었습니다.");
          form.reset();
        }})
        .catch(function(error){{
          console.error(error);
          alert("전송 중 오류가 발생했습니다.");
        }})
        .finally(function(){{
          btn.disabled = false;
          btn.textContent = originalText;
        }});
      }});
    }});
  }});
}})();
</script>
"""

def image_set(seed_text):
    random.seed(seed_text)

    # 전·후는 같은 번호(같은 현장)끼리 짝을 맞춤
    pairs = random.sample(range(1, 101), 4)
    process = random.sample(range(1, 26), 2)

    return {
        "before": [f"/images/cases/before-{n:03d}.jpg" for n in pairs],
        "after": [f"/images/cases/after-{n:03d}.jpg" for n in pairs],
        "process": [f"/images/main/process-{n:02d}.jpg" for n in process],
    }

def photo_section(region_name="유품정리"):
    imgs = image_set(region_name)

    return f"""
<section id="photos">
  <div class="wrap">

    <div class="section-title">
      <h2>{region_name} 작업사진</h2>
      <p>현장 상황에 따라 작업 전·중·후 모습이 달라질 수 있습니다.</p>
    </div>

    <div class="photo-grid">
      <div class="photo"><img src="{imgs["before"][0]}" alt="{region_name} 유품정리 전 사진"></div>
      <div class="photo"><img src="{imgs["after"][0]}" alt="{region_name} 유품정리 후 사진"></div>
      <div class="photo"><img src="{imgs["before"][1]}" alt="{region_name} 유품정리 전 현장"></div>
      <div class="photo"><img src="{imgs["after"][1]}" alt="{region_name} 유품정리 정리 후"></div>
      <div class="photo"><img src="{imgs["process"][0]}" alt="{region_name} 유품정리 작업중"></div>
      <div class="photo"><img src="{imgs["process"][1]}" alt="{region_name} 유품정리 분류 작업"></div>
      <div class="photo"><img src="{imgs["before"][2]}" alt="{region_name} 고독사청소 전"></div>
      <div class="photo"><img src="{imgs["after"][2]}" alt="{region_name} 고독사청소 완료"></div>
    </div>

  </div>
</section>
"""

def case_section(region_name):
    imgs = image_set(region_name + "case")

    cases = [
        ("아파트 유품정리", imgs["before"][0], f"{region_name} 아파트 현장에서 보관 물품과 정리 물품을 구분한 뒤 폐기물 반출과 마무리 정리를 진행했습니다."),
        ("원룸 유품정리", imgs["before"][1], f"{region_name} 원룸 현장에서 생활용품, 의류, 소형가전 등을 분류하고 필요한 물품은 별도로 확인했습니다."),
        ("단독주택 유품정리", imgs["process"][0], f"{region_name} 단독주택에서는 방, 거실, 창고, 마당까지 확인하며 정리 범위를 나누어 진행했습니다."),
        ("고독사청소", imgs["process"][1], f"{region_name} 고독사청소 현장은 냄새와 오염 여부를 확인한 뒤 정리, 소독, 탈취 범위를 안내했습니다."),
        ("특수청소", imgs["after"][2], f"{region_name} 특수청소는 일반 청소로 해결하기 어려운 오염과 방치 흔적을 현장 상태에 맞춰 정리했습니다."),
        ("빈집정리", imgs["after"][3], f"{region_name} 빈집정리는 상속, 매매, 임대 준비 과정에서 남은 물품과 폐기물을 정리하는 방식으로 진행됩니다."),
    ]

    cards = ""

    for title, img, desc in cases:
        cards += f"""
      <div class="case">
        <img src="{img}" alt="{region_name} {title}">
        <div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </div>
"""

    return f"""
<section>
  <div class="wrap">

    <div class="section-title">
      <h2>{region_name} 유품정리 작업사례</h2>
      <p>현장 유형별로 자주 접수되는 작업 사례입니다.</p>
    </div>

    <div class="case-grid">
      {cards}
    </div>

  </div>
</section>
"""

REGION_REVIEWS = {
    "산청": [
        ("산청 유품정리", "산청 외곽 단독주택 유품정리를 맡겼습니다. 보관할 물품과 정리할 물품을 꼼꼼히 구분해 주셔서 안심이 됐습니다."),
        ("산청 고독사청소", "산청에서 고독사청소가 급했는데, 냄새와 오염 상태를 먼저 확인해 주시고 정리·소독까지 차분히 진행해 주셨습니다."),
        ("농촌형 주택 정리", "산청 농촌형 주택이라 방과 창고가 많았는데, 범위를 나눠 정리해 주셔서 부담이 줄었습니다."),
        ("친절한 안내", "산청까지 오셔서 현장 상황을 직접 보신 뒤 일정과 비용을 솔직하게 설명해 주셨습니다."),
    ],
    "함양": [
        ("함양 유품정리", "함양 오래된 단독주택 유품정리를 진행했습니다. 중요한 서류와 사진까지 따로 챙겨 주셔서 감사했습니다."),
        ("함양 고독사청소", "함양 고독사청소 문의 후 바로 상담받았고, 정리와 탈취 과정을 단계별로 안내해 주셔서 안심하고 맡겼습니다."),
        ("신속한 일정 조율", "함양 외곽이라 걱정했는데, 방문 일정 조율이 빨랐고 작업도 깔끔하게 마무리됐습니다."),
        ("세심한 분류", "함양 유품정리 중 남겨둘 물건과 버릴 물건을 가족 의견에 맞춰 정리해 주셨습니다."),
    ],
    "거창": [
        ("거창 유품정리", "거창 읍내 아파트 유품정리를 맡겼습니다. 가구 반출부터 마무리 청소까지 한 번에 진행되어 만족했습니다."),
        ("거창 고독사청소", "거창에서 고독사청소가 필요했는데, 오염 범위를 먼저 설명해주시고 특수청소까지 꼼꼼히 해주셨습니다."),
        ("단독주택 정리", "거창 외곽 단독주택이라 마당과 창고까지 있었는데, 유품정리 범위를 나눠 차질 없이 진행됐습니다."),
        ("부담 없는 상담", "거창 유품정리 비용과 작업 순서를 미리 안내받아 가족끼리 상의하기 수월했습니다."),
    ],
    "합천": [
        ("합천 유품정리", "합천 농촌형 주택 유품정리를 진행했습니다. 방과 창고에 쌓인 물품을 체계적으로 정리해 주셨습니다."),
        ("합천 고독사청소", "합천 고독사청소 현장에서 냄새 관리와 소독까지 신경 써 주셔서 이후 공간이 훨씬 나아졌습니다."),
        ("창고 정리 포함", "합천 유품정리 때 본채뿐 아니라 창고 정리까지 함께 맡길 수 있어 큰 도움이 됐습니다."),
        ("빠른 대응", "합천에서 급하게 고독사청소를 문의했는데, 상담부터 현장 진행까지 빠르게 도와주셨습니다."),
    ],
}


def review_section(region_name=None):
    reviews = REGION_REVIEWS.get(region_name) or [
        ("친절한 상담", "급하게 문의드렸는데 일정 조율과 설명을 자세히 해주셨습니다."),
        ("깔끔한 정리", "보관 물품을 따로 정리해 주셔서 큰 도움이 되었습니다."),
        ("신속한 진행", "예상보다 빠르게 정리가 완료되어 만족했습니다."),
    ]

    cards = "\n".join(
        f"""      <div class="review-card">
        <h3>{esc(title)}</h3>
        <p>{esc(body)}</p>
      </div>"""
        for title, body in reviews
    )

    return f"""
<section class="review">

  <div class="wrap">

    <div class="section-title">
      <h2>고객 후기</h2>
      <p>상담과 작업 후 남겨주신 후기 일부입니다.</p>
    </div>

    <div class="review-grid">

{cards}

    </div>

  </div>

</section>
"""
def service_section():
    return """
<section id="service">
  <div class="wrap">
    <div class="section-title">
      <h2>주요 서비스</h2>
      <p>상황에 맞는 정리와 청소 범위를 안내합니다.</p>
    </div>

    <div class="grid">
      <div class="card">
        <h3>유품정리</h3>
        <p>고인의 생활 물품을 확인하고 보관 물품과 정리 물품을 구분합니다.</p>
      </div>

      <div class="card">
        <h3>고독사청소</h3>
        <p>냄새, 오염, 장기 방치 흔적이 있는 현장을 확인하고 정리합니다.</p>
      </div>

      <div class="card">
        <h3>특수청소</h3>
        <p>일반 청소로 어려운 오염과 악취, 방치 공간을 정리합니다.</p>
      </div>

      <div class="card">
        <h3>빈집정리</h3>
        <p>상속, 매매, 임대 전후 남은 물품과 폐기물을 정리합니다.</p>
      </div>
    </div>
  </div>
</section>
"""


def price_section(region_name="경남·부산·울산"):
    return f"""
<section class="price" id="price">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 비용 안내</h2>
      <p>현장 상황에 따라 작업 범위와 비용이 달라질 수 있습니다.</p>
    </div>

    <div class="price-box">
      <div class="price-card">
        <h3>기본 유품정리</h3>
        <div class="price-num">방문 상담 후 안내</div>
        <p>보관 물품 분류, 폐기물 정리, 공간 정리를 중심으로 진행합니다.</p>
      </div>

      <div class="price-card">
        <h3>고독사청소 포함</h3>
        <div class="price-num">현장 상태별 안내</div>
        <p>냄새, 오염, 소독, 탈취가 필요한 경우 작업 범위가 달라집니다.</p>
      </div>

      <div class="price-card">
        <h3>빈집정리·특수청소</h3>
        <div class="price-num">물량 기준 산정</div>
        <p>가구, 가전, 생활폐기물, 창고 정리 여부에 따라 상담 후 안내합니다.</p>
      </div>
    </div>
  </div>
</section>
"""


def price_factor_section(region_name="경남·부산·울산"):
    return f"""
<section>
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 비용에 영향을 주는 요소</h2>
      <p>같은 평수라도 현장 조건에 따라 작업 시간과 인력이 달라집니다.</p>
    </div>

    <div class="grid">
      <div class="card">
        <h3>물품과 폐기물 양</h3>
        <p>장롱, 냉장고, 침대, 생활용품, 창고 물품이 많을수록 작업 범위가 커집니다.</p>
      </div>

      <div class="card">
        <h3>반출 동선</h3>
        <p>엘리베이터 유무, 계단 작업, 차량 진입 가능 여부가 작업 시간에 영향을 줍니다.</p>
      </div>

      <div class="card">
        <h3>오염·냄새 여부</h3>
        <p>고독사청소나 특수청소가 필요한 경우 소독과 탈취 작업이 추가될 수 있습니다.</p>
      </div>

      <div class="card">
        <h3>보관 물품 분류</h3>
        <p>통장, 도장, 서류, 사진, 귀금속 등 확인할 물품이 많으면 분류 시간이 필요합니다.</p>
      </div>
    </div>
  </div>
</section>
"""


def seo_section(region_name, feature):
    return f"""
<section class="seo">
  <div class="wrap">
    <h2>{region_name} 유품정리, 현장마다 달라지는 이유</h2>

    <p>{region_name} 유품정리는 단순히 집 안의 물건을 치우는 일이 아닙니다. 고인의 생활 흔적이 남아 있는 공간에서 중요한 물품을 확인하고, 가족이 보관할 물건과 정리할 물건을 구분하는 과정이 먼저 필요합니다.</p>

    <p>{feature}입니다. 같은 {region_name} 지역이라도 아파트, 빌라, 단독주택, 원룸, 상가주택 등 현장 형태에 따라 작업 방식과 시간이 달라질 수 있습니다.</p>

    <h3>{region_name} 유품정리 전 먼저 확인하는 것</h3>

    <ul>
      <li>통장, 도장, 계약서 등 중요 서류</li>
      <li>사진, 앨범, 편지 등 추억 물품</li>
      <li>귀금속, 현금, 보관 물품</li>
      <li>폐기물 양과 반출 동선</li>
      <li>냄새, 오염, 특수청소 필요 여부</li>
    </ul>

    <h3>{region_name} 고독사청소와 특수청소가 필요한 경우</h3>

    <p>장기간 방치된 공간이나 냄새, 오염이 남아 있는 현장은 일반 유품정리만으로 마무리되지 않을 수 있습니다. 이런 경우 현장 상태를 확인한 뒤 소독, 탈취, 특수청소 범위를 함께 안내합니다.</p>

    <h3>{region_name} 유품정리 상담 전 준비하면 좋은 내용</h3>

    <p>주소, 주거 형태, 층수, 엘리베이터 유무, 정리할 물품의 대략적인 양, 보관해야 할 물품 여부를 미리 알려주시면 상담이 더 정확해집니다.</p>
  </div>
</section>
"""


def process_section(region_name):
    return f"""
<section class="process">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 진행과정</h2>
      <p>상담부터 마무리 확인까지 순서대로 진행합니다.</p>
    </div>

    <div class="step">
      <div class="num">1</div>
      <div>
        <h3>상담 접수</h3>
        <p>주소, 주거 형태, 정리 범위, 일정 등을 확인합니다.</p>
      </div>
    </div>

    <div class="step">
      <div class="num">2</div>
      <div>
        <h3>현장 확인</h3>
        <p>사진 또는 방문 확인을 통해 물품 양과 작업 범위를 파악합니다.</p>
      </div>
    </div>

    <div class="step">
      <div class="num">3</div>
      <div>
        <h3>중요 물품 분류</h3>
        <p>서류, 사진, 귀중품 등 보관 물품을 먼저 확인합니다.</p>
      </div>
    </div>

    <div class="step">
      <div class="num">4</div>
      <div>
        <h3>정리 및 처리</h3>
        <p>보관 물품과 폐기 물품을 구분하고 현장에 맞춰 처리합니다.</p>
      </div>
    </div>

    <div class="step">
      <div class="num">5</div>
      <div>
        <h3>마무리 확인</h3>
        <p>작업 완료 후 요청사항과 현장 상태를 최종 확인합니다.</p>
      </div>
    </div>
  </div>
</section>
"""

FAQ_PATTERNS = {
    "부산": [
        ("부산 유품정리 비용은 어떻게 정해지나요?", "아파트, 빌라, 주택 구조와 엘리베이터 사용 여부, 폐기물 양에 따라 달라집니다."),
        ("부산 구도심 주택도 가능한가요?", "골목길이나 계단 작업이 필요한 현장도 상담 후 진행 가능합니다."),
        ("부산 고독사청소도 함께 가능한가요?", "냄새, 오염, 장기 방치 흔적이 있는 경우 특수청소와 함께 안내합니다."),
    ],
    "울산": [
        ("울산 유품정리 비용은 어떻게 정해지나요?", "아파트, 단독주택, 외곽 주거지 여부와 물품 양에 따라 달라집니다."),
        ("울산 울주군 외곽 지역도 가능한가요?", "울주군 외곽 주택과 농촌형 주거지도 상담 가능합니다."),
        ("울산 특수청소도 가능한가요?", "오염, 냄새, 방치 흔적이 있는 현장은 현장 확인 후 진행 범위를 안내합니다."),
    ],
    "경남": [
        ("경남 유품정리 비용은 어떻게 정해지나요?", "지역, 주거 형태, 물품 양, 반출 동선, 소독 필요 여부에 따라 달라집니다."),
        ("경남 시군 외곽도 가능한가요?", "시내뿐 아니라 읍면 단위 주택과 외곽 지역도 상담 가능합니다."),
        ("고독사청소와 유품정리를 같이 할 수 있나요?", "현장 상태에 따라 유품정리, 고독사청소, 특수청소를 함께 안내합니다."),
    ],
}

def faq_section(region_name):
    if "부산" in region_name:
        faqs = FAQ_PATTERNS["부산"]
    elif "울산" in region_name:
        faqs = FAQ_PATTERNS["울산"]
    else:
        faqs = FAQ_PATTERNS["경남"]

    items = ""

    for i, (q, a) in enumerate(faqs):
        open_attr = " open" if i == 0 else ""
        items += f"""
    <details{open_attr}>
      <summary>{q}</summary>
      <p>{a}</p>
    </details>
"""

    items += """
    <details>
      <summary>중요 물품은 따로 확인하나요?</summary>
      <p>통장, 도장, 계약서, 사진, 귀금속 등은 작업 중 별도로 확인합니다.</p>
    </details>

    <details>
      <summary>당일 상담도 가능한가요?</summary>
      <p>일정에 따라 당일 상담이 가능하며, 현장 사진을 보내주시면 보다 빠른 안내가 가능합니다.</p>
    </details>
"""

    return f"""
<section class="faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 자주 묻는 질문</h2>
    </div>
    {items}
  </div>
</section>
"""
def faq_section_fixed(region_name):
    if "부산" in region_name:
        faqs = FAQ_PATTERNS["부산"]
    elif "울산" in region_name:
        faqs = FAQ_PATTERNS["울산"]
    else:
        faqs = FAQ_PATTERNS["경남"]

    items = ""

    for i, (q, a) in enumerate(faqs):
        open_attr = " open" if i == 0 else ""
        items += f"""
    <details{open_attr}>
      <summary>{q}</summary>
      <p>{a}</p>
    </details>
"""

    items += """
    <details>
      <summary>중요 물품은 따로 확인하나요?</summary>
      <p>통장, 도장, 계약서, 사진, 귀금속 등은 작업 중 별도로 확인합니다.</p>
    </details>

    <details>
      <summary>당일 상담도 가능한가요?</summary>
      <p>일정에 따라 당일 상담이 가능하며, 현장 사진을 보내주시면 빠르게 안내 가능합니다.</p>
    </details>
"""

    return f"""
<section class="faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 자주 묻는 질문</h2>
    </div>
    {items}
  </div>
</section>
"""

def faq_schema(region_name):
    if "부산" in region_name:
        faqs = FAQ_PATTERNS["부산"]
    elif "울산" in region_name:
        faqs = FAQ_PATTERNS["울산"]
    else:
        faqs = FAQ_PATTERNS["경남"]

    faqs = faqs + [
        ("중요 물품은 따로 확인하나요?", "통장, 도장, 계약서, 사진, 귀금속 등은 작업 중 별도로 확인합니다."),
        ("당일 상담도 가능한가요?", "일정에 따라 당일 상담이 가능하며, 현장 사진을 보내주시면 보다 빠른 안내가 가능합니다."),
    ]

    items = []
    for q, a in faqs:
        items.append(f'''{{
          "@type": "Question",
          "name": "{esc(q)}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{esc(a)}"
          }}
        }}''')

    return f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {",".join(items)}
  ]
}}
</script>
'''

    return f"""
<section class="faq">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 자주 묻는 질문</h2>
    </div>
    {items}
  </div>
</section>
"""


def child_links_for(slug):
    if slug == "busan":
        children = [r for r in REGIONS if r[1].startswith("busan-")]
        title = "부산 세부 지역 유품정리 바로가기"
    elif slug == "ulsan":
        children = [r for r in REGIONS if r[1].startswith("ulsan-")]
        title = "울산 세부 지역 유품정리 바로가기"
    else:
        return ""

    links = "\n".join(
        f'<a href="/regions/{child_slug}.html">{child_name} 유품정리</a>'
        for child_name, child_slug, _, _ in children
    )

    return f"""
<section>
  <div class="wrap">
    <div class="section-title">
      <h2>{title}</h2>
      <p>구·군별 유품정리 상담 페이지를 확인할 수 있습니다.</p>
    </div>
    <div class="regions">
      {links}
    </div>
  </div>
</section>
"""


def parent_links_for(slug):
    links = ['<a href="/">가족애유품정리 메인으로 가기</a>']

    if slug.startswith("busan-"):
        links.append('<a href="/regions/busan.html">부산 유품정리 대표페이지</a>')
    elif slug.startswith("ulsan-"):
        links.append('<a href="/regions/ulsan.html">울산 유품정리 대표페이지</a>')

    links.append('<a href="/#regions">전체 지역 보기</a>')

    return "\n".join(links)

NEARBY_MAP = {
    "changwon": ["gimhae", "haman", "changnyeong", "masan", "jinhae"],
    "masan": ["changwon", "jinhae", "haman", "goseong"],
    "jinhae": ["changwon", "masan", "gimhae"],
    "gimhae": ["changwon", "yangsan", "miryang", "busan"],
    "yangsan": ["gimhae", "busan", "ulsan", "miryang"],
    "jinju": ["sacheon", "sancheong", "hadong", "goseong"],
    "geoje": ["tongyeong", "goseong", "busan"],
    "tongyeong": ["geoje", "goseong", "sacheon"],
    "sacheon": ["jinju", "goseong", "hadong"],
    "miryang": ["gimhae", "yangsan", "changnyeong"],
    "busan": ["gimhae", "yangsan", "ulsan", "geoje"],
    "ulsan": ["yangsan", "busan", "gyeongnam"],
}

def nearby_links_for(slug):
    region_dict = {region_slug: region_name for region_name, region_slug, _, _ in REGIONS}

    nearby = NEARBY_MAP.get(slug, [])

    if slug.startswith("busan-"):
        nearby = ["busan", "gimhae", "yangsan", "ulsan"]
    elif slug.startswith("ulsan-"):
        nearby = ["ulsan", "yangsan", "busan"]

    if not nearby:
        nearby = ["changwon", "gimhae", "jinju", "yangsan"]

    links = ""

    for nearby_slug in nearby:
        if nearby_slug in region_dict:
            links += f'<a href="/regions/{nearby_slug}.html">{region_dict[nearby_slug]} 유품정리</a>\n'

    if not links:
        return ""

    return f"""
<section>
  <div class="wrap">
    <div class="section-title">
      <h2>함께 보는 인근 지역</h2>
      <p>가까운 지역의 유품정리 상담 페이지도 함께 확인할 수 있습니다.</p>
    </div>
    <div class="regions">
      {links}
    </div>
  </div>
</section>
"""

def region_links(regions=None):
    items = regions or REGIONS
    return "\n".join(
        f'<a href="/regions/{slug}.html">{name} 유품정리</a>'
        for name, slug, _, _ in items
    )


def region_section():
    return f"""
<section id="regions">
  <div class="wrap">
    <div class="section-title">
      <h2>경남·부산·울산 지역별 유품정리 바로가기</h2>
      <p>대표 지역 페이지와 세부 구·군 페이지를 확인할 수 있습니다.</p>
    </div>

    <div class="regions">
      {region_links()}
    </div>
  </div>
</section>
"""


def hero_section(title, subtitle, badge):
    return f"""
<section class="hero">
  <div class="wrap">
    <span class="badge">{badge}</span>
    <h1>{title}</h1>
    <p>{subtitle}</p>

    <div class="btns">
      <a class="btn primary" href="#contact">상담접수</a>
      <a class="btn secondary" href="tel:{PHONE.replace('-', '')}">{PHONE}</a>
    </div>
  </div>
</section>
"""


def make_index():
    title = f"{BRAND} | 경남 부산 울산 유품정리 고독사청소 특수청소"
    desc = f"{BRAND}는 경남, 부산, 울산 전지역 유품정리, 고독사청소, 특수청소, 빈집정리 상담을 진행합니다."
    url = SITE_URL + "/"

    return f"""<!DOCTYPE html>
<html lang="ko">
{head(title, desc, url)}
<body>
{header()}
<main>
{hero_section("유품정리, 가족의 마음으로 정리합니다", "고인의 물품을 정성스럽게 확인하고, 보관할 물건과 정리할 물건을 구분합니다. 고독사청소, 특수청소, 빈집정리까지 현장 상황에 맞춰 안내합니다.", "경남 · 부산 · 울산 상담 가능")}
{service_section()}
{price_section()}
{price_factor_section()}
{seo_section("경남·부산·울산", "아파트, 빌라, 단독주택, 원룸, 농촌형 주택 등 다양한 현장이 존재하는 지역")}
{process_section("경남·부산·울산")}
{photo_section("경남·부산·울산")}
{case_section("경남·부산·울산")}
{review_section()}
{region_section()}
{faq_section_fixed("경남·부산·울산")}
{backlink_section()}
{form_section("경남 부산 울산")}
</main>
{footer()}
{local_business_schema("경남·부산·울산", url)}
{email_script()}
</body>
</html>
"""


def make_region_page(name, slug, group, feature):
    title = f"{name} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc = f"{name} 유품정리 전문 {BRAND}. {name} 지역 유품정리, 고독사청소, 특수청소, 빈집정리 상담을 진행합니다."
    url = f"{SITE_URL}/regions/{slug}.html"

    return f"""<!DOCTYPE html>
<html lang="ko">
{head(title, desc, url)}
<body>
{header()}
<main>
{hero_section(f"{name} 유품정리<br>{BRAND}", f"{name} 유품정리, 고독사청소, 특수청소, 빈집정리 상담을 진행합니다. 중요한 물품 분류부터 폐기물 처리, 공간 정리까지 현장 상황에 맞춰 안내합니다.", f"{group} 지역 상담 가능")}
{service_section()}
{price_section(name)}
{price_factor_section(name)}
{seo_section(name, feature)}
{process_section(name)}
{photo_section(name)}
{case_section(name)}
{review_section(name)}
{child_links_for(slug)}
{nearby_links_for(slug)}
<section>
  <div class="wrap">
    <div class="section-title">
      <h2>다른 지역도 함께 보기</h2>
    </div>
    <div class="regions">
      {parent_links_for(slug)}
    </div>
  </div>
</section>
{faq_section_fixed(name)}
{backlink_section()}
{form_section(name)}
</main>
{footer()}
{local_business_schema(name, url)}
{email_script()}
</body>
</html>
"""


def make_sitemap():
    today = date.today().isoformat()

    urls = [("/", "1.0")]
    urls += [(f"/regions/{slug}.html", "0.9") for _, slug, _, _ in REGIONS]

    items = []

    for path, priority in urls:
        items.append(f"""  <url>
    <loc>{SITE_URL}{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(items)
        + "\n</urlset>\n"
    )


def make_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def main():
    REGIONS_DIR.mkdir(exist_ok=True)

    Path("index.html").write_text(make_index(), encoding="utf-8")

    for name, slug, group, feature in REGIONS:
        path = REGIONS_DIR / f"{slug}.html"
        path.write_text(
            make_region_page(name, slug, group, feature),
            encoding="utf-8"
        )
        print("생성:", path)

    Path("sitemap.xml").write_text(make_sitemap(), encoding="utf-8")
    Path("robots.txt").write_text(make_robots(), encoding="utf-8")

    print("완료")
    print(f"총 {len(REGIONS)}개 지역 페이지 생성")
    print(f"확인: {SITE_URL}")


if __name__ == "__main__":
    main()