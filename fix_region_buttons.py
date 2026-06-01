
from pathlib import Path
import shutil

CITY_LINKS = [
    ("창원", "changwon"),
    ("마산", "masan"),
    ("진해", "jinhae"),
    ("김해", "gimhae"),
    ("진주", "jinju"),
    ("양산", "yangsan"),
    ("거제", "geoje"),
    ("통영", "tongyeong"),
    ("사천", "sacheon"),
    ("밀양", "miryang"),
    ("함안", "haman"),
    ("창녕", "changnyeong"),
    ("고성", "goseong"),
    ("남해", "namhae"),
    ("하동", "hadong"),
    ("산청", "sancheong"),
    ("함양", "hamyang"),
    ("거창", "geochang"),
    ("합천", "hapcheon"),
    ("의령", "uiryeong"),
]

TARGET_TITLE = "경남 전지역 유품정리 출장 가능"

def backup(path):
    backup_path = path.with_suffix(path.suffix + ".buttonfix.backup")
    if not backup_path.exists():
        shutil.copy2(path, backup_path)

def city_section_html():
    links = []
    for name, slug in CITY_LINKS:
        links.append(f'        <a href="/regions/{slug}.html">{name} 유품정리</a>')
    links_html = "\\n".join(links)

    return f'''<section class="service-area" id="areas">
  <div class="wrap">
    <div class="section-title">
      <h2>{TARGET_TITLE}</h2>
    </div>
    <div class="regions">
{links_html}
    </div>
  </div>
</section>'''

def find_section_bounds(html):
    title_pos = html.find(TARGET_TITLE)
    if title_pos == -1:
        return None

    start = html.rfind("<section", 0, title_pos)
    if start == -1:
        return None

    next_section = html.find("<section", title_pos + len(TARGET_TITLE))
    if next_section != -1:
        return start, next_section

    end_body = html.find("</body>", title_pos)
    if end_body != -1:
        return start, end_body

    return None

def fix_file(path):
    html = path.read_text(encoding="utf-8", errors="ignore")
    bounds = find_section_bounds(html)
    if not bounds:
        return False

    start, end = bounds
    backup(path)
    fixed = html[:start] + city_section_html() + "\\n\\n" + html[end:]
    path.write_text(fixed, encoding="utf-8")
    return True

def main():
    files = [Path("index.html")]
    regions_dir = Path("regions")
    if regions_dir.exists():
        files.extend(sorted(regions_dir.glob("*.html")))

    changed = []
    for path in files:
        if path.exists():
            if fix_file(path):
                changed.append(str(path))

    print(f"수정 완료: {len(changed)}개 파일")
    for item in changed[:30]:
        print("-", item)
    if len(changed) > 30:
        print(f"...외 {len(changed) - 30}개")

    print("")
    print("다음 명령어로 확인하세요:")
    print("git status")
    print("")
    print("확인할 주소:")
    print("https://gajogae-yupum.com/")
    print("https://gajogae-yupum.com/regions/changwon.html")

if __name__ == "__main__":
    main()
