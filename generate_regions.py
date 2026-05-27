from pathlib import Path
import re
from datetime import date
import shutil

SITE_URL = "https://gajogae-yupum.netlify.app"
BRAND = "가족애유품정리"
template_path = Path("index.html")
regions_path = Path("regions.txt")
output_dir = Path("regions")
CLEAN_REGIONS_FOLDER = True

WORD_MAP = {
    "경상남도":"gyeongnam","경남":"gyeongnam",
    "창원시":"changwon","의창구":"uichang","성산구":"seongsan","마산합포구":"masanhappo","마산회원구":"masanhoewon","진해구":"jinhae",
    "김해시":"gimhae","진주시":"jinju","양산시":"yangsan","거제시":"geoje","통영시":"tongyeong","사천시":"sacheon","밀양시":"miryang",
    "함안군":"haman","창녕군":"changnyeong","고성군":"goseong","남해군":"namhae","하동군":"hadong","산청군":"sancheong","함양군":"hamyang","거창군":"geochang","합천군":"hapcheon","의령군":"uiryeong",
    "동읍":"dongeup","북면":"bukmyeon","대산면":"daesanmyeon","팔룡동":"pallyongdong","명곡동":"myeonggokdong","봉림동":"bongnimdong",
    "용지동":"yongjidong","반송동":"bansongdong","중앙동":"jungangdong","상남동":"sangnamdong","사파동":"sapadong","가음정동":"gaeumjeongdong","성주동":"seongjudong","웅남동":"ungnamdong",
    "구산면":"gusanmyeon","진동면":"jindongmyeon","진북면":"jinbukmyeon","진전면":"jinjeonmyeon","현동":"hyeondong","가포동":"gapodong","월영동":"woryeongdong","문화동":"munhwadong","완월동":"wanwoldong","자산동":"jasandong","교방동":"gyobangdong","오동동":"odongdong","합포동":"happodong","산호동":"sanhodong",
    "내서읍":"naeseoeup","회원동":"hoewondong","석전동":"seokjeondong","회성동":"hoeseongdong","양덕동":"yangdeokdong","합성동":"hapseongdong","구암동":"guamdong","봉암동":"bongamdong",
    "충무동":"chungmudong","여좌동":"yeojwadong","태백동":"taebaekdong","경화동":"gyeonghwadong","병암동":"byeongamdong","석동":"seokdong","이동":"idong","자은동":"jaeundong","덕산동":"deoksandong","풍호동":"punghodong","웅천동":"ungcheondong","웅동":"ungdong",
    "진영읍":"jinyoungeup","주촌면":"juchonmyeon","진례면":"jillyemyeon","한림면":"hallimmyeon","생림면":"saengnimmyeon","상동면":"sangdongmyeon","대동면":"daedongmyeon","동상동":"dongsangdong","회현동":"hoeheondong","부원동":"buwondong","내외동":"naeoe-dong","북부동":"bukbudong","활천동":"hwalcheondong","삼안동":"samandong","불암동":"buramdong","장유동":"jangyudong",
    "물금읍":"mulgeumeup","원동면":"wondongmyeon","상북면":"sangbukmyeon","하북면":"habukmyeon","양주동":"yangjudong","삼성동":"samsungdong","강서동":"gangseodong","서창동":"seochangdong","소주동":"sojudong","평산동":"pyeongsandong","덕계동":"deokgyedong",
}

CHO=["g","kk","n","d","tt","r","m","b","pp","s","ss","","j","jj","ch","k","t","p","h"]
JUNG=["a","ae","ya","yae","eo","e","yeo","ye","o","wa","wae","oe","yo","u","wo","we","wi","yu","eu","ui","i"]
JONG=["","k","k","ks","n","nj","nh","t","l","lk","lm","lb","ls","lt","lp","lh","m","p","ps","t","t","ng","t","t","k","t","p","h"]

def romanize(text):
    out=[]
    for ch in text:
        code=ord(ch)
        if 0xAC00 <= code <= 0xD7A3:
            s=code-0xAC00
            out.append(CHO[s//588]+JUNG[(s%588)//28]+JONG[s%28])
        elif ch.isalnum():
            out.append(ch.lower())
        else:
            out.append("-")
    return "".join(out)

def make_slug(region, index):
    result=[]
    for p in re.split(r"\s+", region.strip()):
        if p in WORD_MAP:
            result.append(WORD_MAP[p])
        else:
            done=False
            for kr,en in [("시","si"),("군","gun"),("구","gu"),("읍","eup"),("면","myeon"),("동","dong"),("리","ri")]:
                if p.endswith(kr) and len(p)>len(kr):
                    result.append(romanize(p[:-len(kr)])+en)
                    done=True
                    break
            if not done:
                result.append(romanize(p))
    slug="-".join(result)
    slug=re.sub(r"[^a-z0-9-]+","-",slug.lower())
    slug=re.sub(r"-+","-",slug).strip("-")
    return f"{index:03d}-{slug}"

def read_regions():
    return [x.strip() for x in regions_path.read_text(encoding="utf-8").splitlines() if x.strip() and not x.strip().startswith("#")]

def meta_name(html,name,content):
    pat=rf'<meta[^>]+name=["\']{name}["\'][^>]*>'
    tag=f'<meta name="{name}" content="{content}">'
    return re.sub(pat,tag,html,1,flags=re.I) if re.search(pat,html,re.I) else html.replace("</head>",tag+"\n</head>",1)

def meta_prop(html,prop,content):
    pat=rf'<meta[^>]+property=["\']{prop}["\'][^>]*>'
    tag=f'<meta property="{prop}" content="{content}">'
    return re.sub(pat,tag,html,1,flags=re.I) if re.search(pat,html,re.I) else html.replace("</head>",tag+"\n</head>",1)

def canonical(html,url):
    pat=r'<link[^>]+rel=["\']canonical["\'][^>]*>|<link[^>]+href=["\'][^"\']+["\'][^>]+rel=["\']canonical["\'][^>]*>'
    tag=f'<link rel="canonical" href="{url}">'
    return re.sub(pat,tag,html,1,flags=re.I) if re.search(pat,html,re.I) else html.replace("</head>",tag+"\n</head>",1)

def region_block(region):
    return f'''
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
          <div>{region} 유품정리</div><div>{region} 고독사청소</div><div>{region} 특수청소</div>
          <div>{region} 빈집정리</div><div>{region} 폐기물처리</div><div>{region} 방문견적</div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="region-faq-section" id="region-faq">
  <div class="wrap">
    <div class="section-title"><h2>{region} 유품정리 자주 묻는 질문</h2><p>상담 전 많이 문의하시는 내용을 정리했습니다.</p></div>
    <div class="faq">
      <details><summary>{region} 유품정리 비용은 어떻게 정해지나요?</summary><p>공간 크기, 짐의 양, 폐기물 처리량, 엘리베이터 유무, 차량 진입 가능 여부, 소독이나 탈취 필요 여부에 따라 달라집니다.</p></details>
      <details><summary>{region} 당일 상담이나 방문 견적이 가능한가요?</summary><p>현장 일정에 따라 가능 여부가 달라질 수 있습니다. 긴급한 경우 전화 상담으로 먼저 상황을 확인한 뒤 가능한 일정을 안내드립니다.</p></details>
      <details><summary>중요 물품은 따로 확인해주나요?</summary><p>통장, 도장, 사진, 계약서, 귀금속, 현금, 중요 서류 등은 작업 중 별도로 분류하여 확인을 요청드립니다.</p></details>
    </div>
  </div>
</section>
'''

def json_ld(region,url):
    return '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service","name":"' + region + ' 유품정리","provider":{"@type":"LocalBusiness","name":"' + BRAND + '","telephone":"+82-10-9242-3895","areaServed":"' + region + '"},"serviceType":["유품정리","고독사청소","특수청소","빈집정리","폐기물처리"],"url":"' + url + '","description":"' + region + ' 유품정리, 고독사청소, 특수청소, 빈집정리 상담과 방문 견적을 진행합니다."}</script>'

def insert_block(html,block):
    for marker in ['id="process"','유품정리 진행 과정','유품정리진행과정','id="faq"']:
        pos=html.find(marker)
        if pos!=-1:
            start=html.rfind("<section",0,pos)
            return html[:start]+block+"\n"+html[start:] if start!=-1 else html[:pos]+block+"\n"+html[pos:]
    return html.replace("</body>",block+"\n</body>",1)

def make_page(region,slug):
    url=f"{SITE_URL}/regions/{slug}.html"
    html=template_path.read_text(encoding="utf-8")
    title=f"{region} 유품정리 업체 {BRAND} | 고독사청소 특수청소 빈집정리"
    desc=f"{region} 유품정리 전문 {BRAND}입니다. {region} 고독사청소, 특수청소, 빈집정리, 폐기물처리 상담과 방문 견적을 진행합니다."
    keywords=f"{region} 유품정리,{region} 유품정리 업체,{region} 고독사청소,{region} 특수청소,{region} 빈집정리,{region} 폐기물처리,{BRAND}"
    html=re.sub(r"<title>.*?</title>",f"<title>{title}</title>",html,1,flags=re.S)
    html=meta_name(html,"description",desc)
    html=meta_name(html,"keywords",keywords)
    html=canonical(html,url)
    html=meta_prop(html,"og:title",title)
    html=meta_prop(html,"og:description",desc)
    html=meta_prop(html,"og:url",url)
    html=meta_name(html,"twitter:title",title)
    html=meta_name(html,"twitter:description",desc)
    html=re.sub(r"<h1>.*?</h1>",f"<h1>{region} 유품정리 전문업체<br>{BRAND}</h1>",html,1,flags=re.S)
    html=re.sub(r"(<h1>.*?</h1>\s*)<p>.*?</p>",rf"\1<p>{region} 유품정리 · 고독사청소 · 특수청소 · 빈집정리 상담<br>고인의 물건을 정성스럽게 분류하고 중요한 물품은 별도 확인합니다.</p>",html,1,flags=re.S)
    html=insert_block(html,region_block(region))
    html=html.replace("</head>",json_ld(region,url)+"\n</head>",1)
    return html

def make_sitemap(items):
    today=date.today().isoformat()
    body=[]
    for slug,_ in items:
        body.append("  <url>\n    <loc>" + SITE_URL + "/regions/" + slug + ".html</loc>\n    <lastmod>" + today + "</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(body) + "\n</urlset>\n"

def main():
    if CLEAN_REGIONS_FOLDER and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(exist_ok=True)
    regions=read_regions()
    created=[]
    redirects=[]
    for i,region in enumerate(regions,1):
        new_slug=make_slug(region,i)
        old_slug=f"{i:03d}-"+re.sub(r"[^0-9a-zA-Z가-힣]+","-",region).strip("-")
        redirects.append(f"/regions/{old_slug}.html  /regions/{new_slug}.html  301")
        (output_dir/f"{new_slug}.html").write_text(make_page(region,new_slug),encoding="utf-8")
        created.append((new_slug,region))
    Path("sitemap-regions.xml").write_text(make_sitemap(created),encoding="utf-8")
    Path("_redirects").write_text("\n".join(redirects)+"\n",encoding="utf-8")
    print(f"완료: {len(created)}개 영문 URL 지역 페이지 생성")
    if created:
        print(f"예시: {SITE_URL}/regions/{created[0][0]}.html")

if __name__=="__main__":
    main()
