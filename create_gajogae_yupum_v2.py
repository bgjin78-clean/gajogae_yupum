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

# 지역별 고유 문맥 — SEO·FAQ·후기·히어로 차별화용
REGION_COPY = {
    "경남": {
        "note": "경남은 창원·김해·진주 같은 도심과 읍면 단위 농촌형 주택이 한 권역에 함께 있어, 같은 상담이라도 현장 접근성과 폐기물 반출 방식이 크게 달라질 수 있습니다.",
        "tip": "시군 경계를 넘는 이동이 잦은 편이니, 희망 일정과 현장 주소를 함께 남겨 주시면 방문 동선을 맞춰 안내드립니다.",
        "housing": "도심 아파트와 외곽 단독주택",
        "focus": "시군별 이동 거리와 반출 동선",
        "faq": ("경남 여러 시군을 한 번에 상담할 수 있나요?", "가능합니다. 현장 위치와 일정을 알려주시면 권역별로 조율해 안내드립니다."),
    },
    "창원": {
        "note": "창원은 의창·성산 대단지 아파트와 구도심 주택이 공존해, 엘리베이터 예약·주차 규정·가구 반출 동선을 먼저 확인하는 상담이 중요합니다.",
        "tip": "단지 관리실 규정과 엘리베이터 사용 가능 시간을 미리 확인하시면 작업 일정 조율이 수월합니다.",
        "housing": "대단지 아파트와 구도심 주택",
        "focus": "엘리베이터·주차·관리 규정",
        "faq": ("창원 아파트 단지도 유품정리가 가능한가요?", "가능합니다. 관리 규정과 엘리베이터 사용 시간을 확인한 뒤 일정을 잡습니다."),
    },
    "마산": {
        "note": "마산합포·회원 일대는 오래된 주택과 골목형 주거지가 많아, 차량 진입과 계단 운반 여부를 초기에 파악하는 것이 좋습니다.",
        "tip": "골목 폭과 주차 가능 위치를 사진으로 보내주시면 인력·차량 구성을 더 정확히 안내할 수 있습니다.",
        "housing": "오래된 주택과 골목형 주거지",
        "focus": "좁은 골목과 계단 운반",
        "faq": ("마산 골목집도 작업이 가능한가요?", "가능합니다. 골목 폭과 계단 여부를 확인한 뒤 운반 방식을 안내드립니다."),
    },
    "진해": {
        "note": "진해는 주택·아파트가 섞인 주거지 특성이 있어, 층수와 엘리베이터 유무에 따라 작업 시간과 인력이 달라질 수 있습니다.",
        "tip": "층수와 엘리베이터 여부, 폐기물 양을 함께 알려주시면 예상 범위를 빠르게 안내드립니다.",
        "housing": "주택과 아파트가 섞인 주거지",
        "focus": "층수와 엘리베이터 여부",
        "faq": ("진해 주택 유품정리도 가능한가요?", "가능합니다. 주택 구조와 마당·창고 유무를 확인한 뒤 정리 범위를 나눕니다."),
    },
    "김해": {
        "note": "김해는 장유·율하·진영 등 신도시형 아파트와 기존 주택이 함께 있어, 단지 규정과 외곽 주택 반출 조건을 구분해서 보는 것이 좋습니다.",
        "tip": "장유·율하 대단지는 관리실 협조 시간이 중요하니, 가능 시간대를 함께 남겨 주세요.",
        "housing": "신도시 아파트와 기존 주택",
        "focus": "대단지 관리 규정과 외곽 반출",
        "faq": ("김해 장유·율하 아파트도 상담 가능한가요?", "가능합니다. 단지 규정과 엘리베이터 사용 시간을 확인 후 안내드립니다."),
    },
    "진주": {
        "note": "진주는 도심 아파트와 외곽 주택이 함께 분포해, 시내 현장과 외곽 현장의 이동·반출 방식이 달라질 수 있습니다.",
        "tip": "외곽 주택은 창고·마당 물품이 많은 경우가 있어 정리 범위를 나눠 상담합니다.",
        "housing": "도심 아파트와 외곽 주택",
        "focus": "시내·외곽 이동과 창고 물량",
        "faq": ("진주 외곽 주택도 방문하나요?", "가능합니다. 외곽 위치와 물품 양을 알려주시면 일정과 차량을 맞춰 안내합니다."),
    },
    "양산": {
        "note": "양산은 물금신도시 아파트와 구도심 주거지가 함께 있어, 신축 단지 규정과 구도심 운반 동선을 각각 확인하는 상담이 필요합니다.",
        "tip": "물금 대단지는 엘리베이터·주차, 구도심은 골목·계단 여부를 우선 확인합니다.",
        "housing": "물금신도시와 구도심 주거지",
        "focus": "신도시 단지 규정과 구도심 동선",
        "faq": ("양산 물금신도시도 유품정리 하나요?", "가능합니다. 단지 규정과 희망 일정을 확인한 뒤 작업을 진행합니다."),
    },
    "거제": {
        "note": "거제는 아파트·원룸과 조선업 관련 주거지가 섞여 있어, 원룸형 소형 현장부터 가구가 많은 아파트까지 규모별 안내가 필요합니다.",
        "tip": "원룸·오피스텔은 물량이 적어도 반출 동선이 중요하니, 건물 구조를 함께 알려 주세요.",
        "housing": "아파트·원룸과 산업 주거지",
        "focus": "소형 원룸부터 아파트까지 규모 차이",
        "faq": ("거제 원룸 유품정리도 가능한가요?", "가능합니다. 소형 공간도 분류·반출·마무리까지 안내드립니다."),
    },
    "통영": {
        "note": "통영은 해안가 주택 비율이 높아 습기·냄새·장기 방치 흔적이 함께 발견되는 경우가 있어, 유품정리와 특수청소 범위를 함께 보는 상담이 많습니다.",
        "tip": "습기·냄새 여부를 사진으로 공유해 주시면 소독·탈취 필요 여부를 미리 안내할 수 있습니다.",
        "housing": "해안가 주택과 습기 관리가 필요한 공간",
        "focus": "습기·냄새와 해안 주거지 특성",
        "faq": ("통영 해안가 주택 습기·냄새도 봐주시나요?", "현장 상태를 확인한 뒤 정리와 함께 소독·탈취 필요 범위를 안내합니다."),
    },
    "사천": {
        "note": "사천은 산업단지와 주거지가 인접해, 생활 공간 정리와 함께 창고·잔짐 처리가 필요한 현장이 자주 접수됩니다.",
        "tip": "생활공간과 창고를 구분해 정리 범위를 정해 주시면 비용·일정 안내가 더 정확해집니다.",
        "housing": "산업단지 인근 주거지와 창고형 공간",
        "focus": "주거 공간과 창고 잔짐",
        "faq": ("사천에서 창고 정리도 함께 가능한가요?", "가능합니다. 주거 공간과 창고 범위를 나눠 상담드립니다."),
    },
    "밀양": {
        "note": "밀양은 농촌형 주택과 오래된 단독주택이 많아, 방·창고·마당으로 물품이 분산된 현장을 구역별로 나누어 진행하는 경우가 많습니다.",
        "tip": "창고·마당 포함 여부를 미리 말씀해 주시면 작업 범위와 차량을 맞춰 안내합니다.",
        "housing": "농촌형 주택과 오래된 단독주택",
        "focus": "방·창고·마당으로 분산된 물품",
        "faq": ("밀양 농촌형 주택 창고도 정리하나요?", "가능합니다. 본채와 창고·마당을 구분해 정리 범위를 안내드립니다."),
    },
    "함안": {
        "note": "함안은 읍면 단위 주거지와 오래된 주택이 많아, 방문 일정과 폐기물 반출 차량 진입 가능 여부를 함께 확인하는 것이 중요합니다.",
        "tip": "차량 진입이 어려운 길은 미리 알려 주시면 운반 방식을 조정해 드립니다.",
        "housing": "읍면 주거지와 오래된 주택",
        "focus": "방문 일정과 차량 진입",
        "faq": ("함안 읍면 지역도 방문하나요?", "가능합니다. 위치와 도로 상황을 확인한 뒤 일정을 조율합니다."),
    },
    "창녕": {
        "note": "창녕은 읍면 단위 오래된 주택이 많아, 장기 보관 물품과 생활폐기물이 섞여 있는 현장을 분류 중심으로 진행하는 상담이 많습니다.",
        "tip": "보관할 서류·사진과 폐기할 가구를 구분해 두시면 현장 작업이 더 빨라집니다.",
        "housing": "읍면 단위 오래된 주택",
        "focus": "장기 보관 물품 분류",
        "faq": ("창녕에서 오래된 가구 폐기도 가능한가요?", "가능합니다. 유품 분류 후 폐기물처리 범위까지 함께 안내드립니다."),
    },
    "고성": {
        "note": "고성은 단독주택과 농촌형 주거지 비중이 높아, 외곽 이동과 넓은 공간의 물품 분산을 고려한 일정 조율이 필요합니다.",
        "tip": "외곽 현장은 이동 시간을 고려해 오전·오후 희망 시간을 함께 남겨 주세요.",
        "housing": "단독주택과 농촌형 주거지",
        "focus": "외곽 이동과 넓은 공간 정리",
        "faq": ("고성 외곽 단독주택도 가능한가요?", "가능합니다. 이동 거리와 물품 양을 확인한 뒤 일정을 안내드립니다."),
    },
    "남해": {
        "note": "남해는 해안 지역 특성과 오래된 주택이 겹치는 현장이 있어, 습기·냄새 확인과 함께 유품 분류를 진행하는 경우가 많습니다.",
        "tip": "섬·해안가 접근이 필요한 경우 방문 가능 요일을 미리 상담해 주세요.",
        "housing": "해안 지역 오래된 주택",
        "focus": "해안 접근성과 습기·냄새",
        "faq": ("남해 해안가 주택도 방문하나요?", "가능합니다. 접근 경로와 일정을 확인한 뒤 안내드립니다."),
    },
    "하동": {
        "note": "하동은 농촌형 주택과 외곽 주거지가 많아, 폐기물 반출 동선과 작업 구역을 나눠 진행하는 상담이 중요합니다.",
        "tip": "본채·창고·텃밭 창고 등 정리할 공간을 목록으로 남겨 주시면 범위 산정이 수월합니다.",
        "housing": "농촌형 주택과 외곽 주거지",
        "focus": "구역별 정리와 반출 동선",
        "faq": ("하동에서 여러 동 건물을 같이 정리할 수 있나요?", "가능합니다. 건물·창고별 범위를 나눠 일정과 비용을 안내드립니다."),
    },
    "산청": {
        "note": "산청은 단독주택과 농촌형 주거지가 많아, 외곽 방문과 창고 물량 확인이 상담 단계에서 특히 중요합니다.",
        "tip": "산간·외곽 주소는 찾아오는 길 정보를 함께 남겨 주시면 일정 조율에 도움이 됩니다.",
        "housing": "단독주택과 농촌형 주거지",
        "focus": "외곽 방문과 창고 물량",
        "faq": ("산청 산간 외곽도 가능한가요?", "가능합니다. 위치와 도로 상태를 확인한 뒤 방문 일정을 안내드립니다."),
    },
    "함양": {
        "note": "함양은 오래된 단독주택 현장이 많아, 서류·사진 등 보관품 분류와 낡은 가구 반출을 함께 진행하는 경우가 많습니다.",
        "tip": "남겨야 할 서류·유품 목록을 가족과 미리 정해 두시면 현장 분류가 더 정확해집니다.",
        "housing": "오래된 단독주택",
        "focus": "보관품 분류와 낡은 가구 반출",
        "faq": ("함양에서 중요한 서류만 먼저 찾아줄 수 있나요?", "가능합니다. 상담 시 확인이 필요한 물품을 말씀해 주시면 우선 분류합니다."),
    },
    "거창": {
        "note": "거창은 읍내 아파트와 외곽 단독주택이 함께 있어, 단지형 현장과 주택형 현장의 작업 방식을 구분해 안내합니다.",
        "tip": "읍내·외곽 여부에 따라 이동 시간이 달라지니 주소를 정확히 남겨 주세요.",
        "housing": "읍내 아파트와 외곽 단독주택",
        "focus": "읍내·외곽 현장 유형 구분",
        "faq": ("거창 읍내와 외곽 비용이 다른가요?", "기본 안내 금액은 같되, 이동·물량·반출 조건에 따라 현장별로 달라질 수 있습니다."),
    },
    "합천": {
        "note": "합천은 농촌형 주택과 창고 정리가 함께 나오는 현장이 많아, 본채와 부속 공간의 범위를 나눠 상담하는 것이 좋습니다.",
        "tip": "창고 포함 여부와 대형 가구 유무를 알려주시면 차량 구성을 맞춰 드립니다.",
        "housing": "농촌형 주택과 창고형 공간",
        "focus": "본채·창고 동시 정리",
        "faq": ("합천에서 본채와 창고를 하루에 하나요?", "물량과 동선에 따라 다르며, 상담 시 예상 일정을 안내드립니다."),
    },
    "의령": {
        "note": "의령은 단독주택과 오래된 주거지가 많아, 장기 방치 물품 정리와 폐기물 반출을 함께 상담하는 경우가 많습니다.",
        "tip": "장기간 비워둔 집이면 냄새·습기 여부도 함께 알려 주세요.",
        "housing": "단독주택과 오래된 주거지",
        "focus": "장기 방치 물품과 반출",
        "faq": ("의령에서 오래 비워둔 집도 정리하나요?", "가능합니다. 방치 기간과 오염 여부를 확인한 뒤 유품정리·특수청소 범위를 안내합니다."),
    },
    "부산": {
        "note": "부산은 구도심 주택부터 해안·산복 도로 주거지, 대단지 아파트까지 유형이 다양해 구별 현장 조건을 먼저 확인하는 상담이 중요합니다.",
        "tip": "구·동 주소와 엘리베이터·주차 가능 여부를 함께 남겨 주시면 일정 안내가 빨라집니다.",
        "housing": "구도심 주택과 대단지 아파트",
        "focus": "구별 지형·주차·엘리베이터",
        "faq": ("부산 전 구 유품정리 상담이 가능한가요?", "가능합니다. 중구부터 기장군까지 현장 위치에 맞춰 안내드립니다."),
    },
    "부산 중구": {
        "note": "부산 중구는 도심형 주거지와 오래된 건물이 섞여 있어, 좁은 진입로와 주차 제한을 고려한 작업 계획이 필요합니다.",
        "tip": "주차 가능 여부와 건물 출입 동선을 미리 알려 주시면 인력 배치에 도움이 됩니다.",
        "housing": "도심형 오래된 주거지",
        "focus": "좁은 진입로와 주차 제한",
        "faq": ("부산 중구 주차 제한 지역도 가능한가요?", "가능합니다. 주차·하차 위치를 확인한 뒤 운반 계획을 세웁니다."),
    },
    "부산 서구": {
        "note": "부산 서구는 오래된 주택과 아파트가 함께 있어, 경사·계단 구간이 있는 현장의 운반 방식을 상담 단계에서 확인합니다.",
        "tip": "계단만 있는 건물인지 엘리베이터 가능인지 알려 주시면 예상 시간이 더 정확해집니다.",
        "housing": "오래된 주택과 아파트",
        "focus": "경사·계단 운반",
        "faq": ("부산 서구 계단만 있는 집도 되나요?", "가능합니다. 층수와 물품 양을 확인한 뒤 인력과 시간을 안내드립니다."),
    },
    "부산 동구": {
        "note": "부산 동구는 도심 주거지 특성이 강해, 짧은 일정 조율과 함께 중요 물품 분류를 우선하는 상담이 많습니다.",
        "tip": "급하신 경우 현장 사진을 먼저 보내주시면 당일·빠른 일정 가능 여부를 안내드립니다.",
        "housing": "도심 주거지",
        "focus": "빠른 일정과 중요 물품 분류",
        "faq": ("부산 동구에서 당일 상담이 가능한가요?", "예약 상황에 따라 가능하며, 사진과 주소를 주시면 빠르게 확인합니다."),
    },
    "부산 영도구": {
        "note": "부산 영도구는 해안가 주택 비율이 높아 습기·냄새 관리가 필요한 현장과 일반 유품정리가 함께 접수됩니다.",
        "tip": "다리·이동 시간을 고려해 희망 시간대를 넓게 남겨 주시면 일정 조율이 수월합니다.",
        "housing": "해안가 주택",
        "focus": "해안 주거지 습기·이동 동선",
        "faq": ("부산 영도구 해안가 주택도 방문하나요?", "가능합니다. 접근 경로와 현장 상태를 확인한 뒤 안내드립니다."),
    },
    "부산 부산진구": {
        "note": "부산 부산진구는 아파트·빌라 밀집 지역이 많아, 관리실 협조와 엘리베이터 사용 시간을 맞추는 작업이 많습니다.",
        "tip": "단지명이 있으면 함께 남겨 주세요. 관리 규정 확인에 도움이 됩니다.",
        "housing": "아파트·빌라 밀집 주거지",
        "focus": "관리실 협조와 엘리베이터",
        "faq": ("부산진구 빌라 유품정리도 하나요?", "가능합니다. 층수·엘리베이터·주차 여부를 확인 후 진행합니다."),
    },
    "부산 동래구": {
        "note": "부산 동래구는 주택과 아파트가 고르게 분포해, 단독주택 마당·창고와 아파트 반출 규정을 구분해 상담합니다.",
        "tip": "주택이면 마당·창고 포함 여부, 아파트면 엘리베이터 가능 여부를 알려 주세요.",
        "housing": "주택과 아파트",
        "focus": "주택 창고와 아파트 반출 규정",
        "faq": ("동래구 단독주택 마당 정리도 포함되나요?", "요청 시 포함 가능하며, 상담 때 범위를 명확히 정해 드립니다."),
    },
    "부산 남구": {
        "note": "부산 남구는 주거 밀집도가 높아 주차와 하차 동선이 작업 시간에 영향을 주는 경우가 많습니다.",
        "tip": "가능하면 하차 가능한 위치나 임시 주차 여부를 함께 알려 주세요.",
        "housing": "주거 밀집 아파트·주택",
        "focus": "주차·하차 동선",
        "faq": ("남구에서 주차 공간이 부족해도 가능한가요?", "가능합니다. 하차 지점을 확인한 뒤 운반 계획을 안내드립니다."),
    },
    "부산 북구": {
        "note": "부산 북구는 아파트와 주택이 함께 있어, 단지형 정리와 주택형 분류 작업이 모두 자주 진행됩니다.",
        "tip": "가구 양이 많으면 미리 말씀해 주시면 차량 대수 안내가 정확해집니다.",
        "housing": "아파트와 주택",
        "focus": "가구 물량과 차량 구성",
        "faq": ("북구에서 대형 가구가 많아도 되나요?", "가능합니다. 물량에 따라 인력과 차량을 조율해 안내드립니다."),
    },
    "부산 해운대구": {
        "note": "부산 해운대구는 고층·대단지 아파트 현장이 많아, 엘리베이터 예약과 관리 규정을 맞춘 일정 잡기가 핵심입니다.",
        "tip": "고층 단지는 엘리베이터 사용 가능 시간을 관리실에 먼저 확인해 주시면 좋습니다.",
        "housing": "고층·대단지 아파트",
        "focus": "엘리베이터 예약과 단지 규정",
        "faq": ("해운대 고층 아파트도 유품정리 가능한가요?", "가능합니다. 엘리베이터·관리 규정을 확인한 뒤 일정을 진행합니다."),
    },
    "부산 사하구": {
        "note": "부산 사하구는 주택·아파트가 넓게 분포해 현장마다 반출 동선 차이가 크므로, 주소 확인 후 맞춤 안내가 필요합니다.",
        "tip": "사진과 함께 층수·엘리베이터 여부를 남겨 주시면 빠른 견적 안내가 가능합니다.",
        "housing": "주택·아파트 혼합 주거지",
        "focus": "현장별 반출 동선 차이",
        "faq": ("사하구 당일 견적 상담도 되나요?", "현장 사진과 주소를 주시면 당일 안내 가능 여부를 확인해 드립니다."),
    },
    "부산 금정구": {
        "note": "부산 금정구는 단독주택과 아파트가 함께 있어, 구릉·경사 지형의 운반 난이도를 상담 시 함께 확인합니다.",
        "tip": "경사로나 계단이 길면 미리 알려 주세요. 인력 배치에 반영합니다.",
        "housing": "단독주택과 아파트",
        "focus": "구릉·경사 지형 운반",
        "faq": ("금정구 경사 많은 주택도 가능한가요?", "가능합니다. 동선과 물량을 확인한 뒤 작업 방식을 안내드립니다."),
    },
    "부산 강서구": {
        "note": "부산 강서구는 외곽 주택과 산업·주거 혼재 지역이 있어, 이동 거리와 창고형 잔짐 여부를 함께 보는 상담이 많습니다.",
        "tip": "외곽 현장은 희망 날짜를 2~3개 남겨 주시면 일정 맞추기가 수월합니다.",
        "housing": "외곽 주택과 창고형 공간",
        "focus": "외곽 이동과 잔짐·창고",
        "faq": ("강서구 외곽도 방문하나요?", "가능합니다. 위치와 물품 양을 확인한 뒤 일정을 조율합니다."),
    },
    "부산 연제구": {
        "note": "부산 연제구는 도심형 주거지 특성이 있어, 짧은 동선 안에서도 중요 물품 확인과 폐기물 분류를 꼼꼼히 진행합니다.",
        "tip": "직장·가족 일정에 맞춰 저녁·주말 희망 여부를 알려 주세요.",
        "housing": "도심형 아파트·빌라",
        "focus": "도심 일정 조율과 분류 중심 작업",
        "faq": ("연제구 주말 작업도 가능한가요?", "예약 상황에 따라 가능하며, 희망 요일을 남겨 주시면 확인해 드립니다."),
    },
    "부산 수영구": {
        "note": "부산 수영구는 아파트 중심 주거지가 많아, 단지 규정에 맞춘 유품정리와 생활폐기물 반출 상담이 주를 이룹니다.",
        "tip": "단지 내 폐기물 배출 규칙이 있으면 미리 공유해 주세요.",
        "housing": "아파트 중심 주거지",
        "focus": "단지 규정과 생활폐기물 반출",
        "faq": ("수영구 아파트 폐기물 규정에 맞춰 진행하나요?", "네. 관리 규정을 확인한 뒤 반출 방식을 맞춰 진행합니다."),
    },
    "부산 사상구": {
        "note": "부산 사상구는 주택과 상가주택이 섞여 있어, 주거 공간과 상가·창고 공간을 구분해 정리 범위를 잡는 상담이 필요합니다.",
        "tip": "상가와 주택이 한 건물이면 정리할 층을 명확히 알려 주세요.",
        "housing": "주택과 상가주택",
        "focus": "주거·상가 공간 구분 정리",
        "faq": ("사상구 상가주택도 유품정리 되나요?", "가능합니다. 주거·상가 구역을 나눠 범위를 안내드립니다."),
    },
    "부산 기장군": {
        "note": "부산 기장군은 주택과 외곽 지역이 넓어, 시내 구와 달리 이동 시간과 차량 진입 조건을 더 자세히 확인합니다.",
        "tip": "외곽·신규 택지 여부와 진입로 상태를 알려 주시면 일정 산정에 도움이 됩니다.",
        "housing": "주택과 외곽 주거지",
        "focus": "외곽 이동과 차량 진입",
        "faq": ("기장군 외곽 신규 주택도 가능한가요?", "가능합니다. 위치와 진입 조건을 확인한 뒤 안내드립니다."),
    },
    "울산": {
        "note": "울산은 남구·중구 아파트 밀집지와 울주군 외곽 주택이 한 도시에 있어, 구·군별 현장 조건에 맞춘 안내가 필요합니다.",
        "tip": "구·군과 동 주소를 정확히 남겨 주시면 이동 동선을 고려해 일정을 잡습니다.",
        "housing": "아파트 밀집지와 외곽 주택",
        "focus": "구·군별 현장 조건",
        "faq": ("울산 전 구·군 상담이 가능한가요?", "가능합니다. 중·남·동·북구와 울주군까지 안내드립니다."),
    },
    "울산 중구": {
        "note": "울산 중구는 도심 주거지 중심으로, 아파트·주택의 중요 물품 분류와 빠른 일정 조율 요청이 많은 편입니다.",
        "tip": "급하신 일정은 희망일과 대체일을 함께 남겨 주세요.",
        "housing": "도심 아파트·주택",
        "focus": "도심 일정과 중요 물품 분류",
        "faq": ("울산 중구에서 빠른 일정 가능한가요?", "예약 상황에 따라 가능하며, 주소를 주시면 가능한 날을 안내드립니다."),
    },
    "울산 남구": {
        "note": "울산 남구는 아파트와 주택이 고르게 있어, 단지 규정 확인과 주택형 반출 동선 확인이 모두 자주 이뤄집니다.",
        "tip": "아파트면 단지명, 주택이면 주차 가능 여부를 함께 알려 주세요.",
        "housing": "아파트와 주택",
        "focus": "단지 규정과 주택 반출",
        "faq": ("울산 남구 아파트 단지 규정도 맞춰주나요?", "네. 관리실 규정과 엘리베이터 시간을 확인한 뒤 진행합니다."),
    },
    "울산 동구": {
        "note": "울산 동구는 주거지와 산업 인프라가 가까운 특성이 있어, 생활 공간 정리와 잔짐·폐기물 처리를 함께 상담하는 경우가 많습니다.",
        "tip": "폐기물 양이 많으면 1톤 기준 예상 대수를 미리 안내드릴 수 있습니다.",
        "housing": "주거지와 산업 인접 지역",
        "focus": "생활 정리와 폐기물 물량",
        "faq": ("울산 동구에서 폐기물처리만 따로 가능한가요?", "유품정리와 함께 또는 범위에 따라 폐기물처리 상담이 가능합니다."),
    },
    "울산 북구": {
        "note": "울산 북구는 아파트·단독주택이 함께 분포해, 신축 단지와 기존 주택의 작업 방식을 구분해 안내합니다.",
        "tip": "신축 단지는 입주·관리 규정이 엄격할 수 있으니 가능 시간을 확인해 주세요.",
        "housing": "아파트·단독주택",
        "focus": "신축 단지와 기존 주택 구분",
        "faq": ("울산 북구 신축 아파트도 되나요?", "가능합니다. 단지 규정을 확인한 뒤 일정을 조율합니다."),
    },
    "울산 울주군": {
        "note": "울산 울주군은 외곽 주택과 농촌형 주거지가 많아, 이동 거리와 창고·마당 정리 범위를 상담 초기에 확정하는 것이 중요합니다.",
        "tip": "읍·면 단위 주소와 차량 진입 가능 여부를 알려 주시면 일정 산정이 정확해집니다.",
        "housing": "외곽 주택과 농촌형 주거지",
        "focus": "외곽 이동과 창고·마당",
        "faq": ("울주군 농촌형 주택 창고도 정리하나요?", "가능합니다. 본채와 창고 범위를 나눠 안내드립니다."),
    },
}


def esc(text):
    return html.escape(str(text))


def region_rng(*parts):
    return random.Random("|".join(str(p) for p in parts))


def region_info(region_name):
    return REGION_COPY.get(
        region_name,
        {
            "note": f"{region_name}은(는) 주거 형태와 현장 조건에 따라 유품정리 범위가 달라질 수 있어, 주소와 공간 특성을 먼저 확인합니다.",
            "tip": "주소, 주거 형태, 물품 양, 희망 일정을 남겨 주시면 맞춤 안내드립니다.",
            "housing": "아파트·주택 등 다양한 주거 형태",
            "focus": "현장 구조와 물품 양",
            "faq": (f"{region_name}에서도 상담 가능한가요?", "가능합니다. 현장 위치를 알려주시면 일정을 안내드립니다."),
        },
    )


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
.price{background:#f7f2e8}
.price-box{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.price-card{background:#fff;border:1px solid #e7decf;border-radius:20px;padding:26px;box-shadow:0 10px 24px rgba(65,45,28,.06)}
.price-card.featured{background:#f3ebe0;border-color:#dcc9a8}
.price-label{display:inline-block;background:#f7f2e8;border-radius:999px;padding:5px 11px;font-size:13px;font-weight:900;color:#9a6b1f;margin-bottom:8px}
.price-card.featured .price-label{background:#fff}
.price-card h3{margin:0;color:#163552;font-size:15px;font-weight:800}
.price-num{font-size:30px;font-weight:900;color:#163552;margin:12px 0;letter-spacing:-.04em}
.price-card p{margin:0;color:#666;font-size:15px;line-height:1.6}
.price-notice{margin-top:18px;background:#fff;border:1px solid #e7decf;border-radius:14px;padding:16px 20px;color:#666;font-weight:700;text-align:center}
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
  "priceRange": "유품정리 25만원부터, 고독사청소 80만원부터, 폐기물처리 1톤 기준 25만원부터",
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
    info = region_info(region_name) if region_name in REGION_COPY else None
    rng = region_rng(region_name, "photos")
    lead = rng.choice([
        f"{region_name} 현장 상황에 따라 작업 전·중·후 모습이 달라질 수 있습니다.",
        f"{info['housing']} 기준으로 본 {region_name} 작업 사진입니다." if info else f"{region_name} 작업 전·중·후 사진입니다.",
        f"{region_name} 유품정리·고독사청소 과정의 참고 사진입니다.",
    ])

    return f"""
<section id="photos">
  <div class="wrap">

    <div class="section-title">
      <h2>{region_name} 작업사진</h2>
      <p>{lead}</p>
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


SERVICE_REVIEWS = [
    (
        "쓰레기집청소",
        "쓰레기가 가득 쌓인 원룸을 맡겼는데, 분류부터 반출까지 하루 만에 정리됐습니다.",
    ),
    (
        "쓰레기집청소",
        "장기간 방치된 집이라 냄새가 심했는데, 정리 후 공간이 완전히 달라졌습니다.",
    ),
    (
        "쓰레기집청소",
        "쓰레기집 청소 범위와 비용을 미리 설명해 주셔서 부담 없이 진행했습니다.",
    ),
    (
        "쓰레기집청소",
        "쌓인 생활쓰레기와 가구를 구분해 처리해 주셔서 이후 관리가 수월해졌습니다.",
    ),
    (
        "쓰레기집청소",
        "이웃 민원 때문에 급히 문의했는데, 빠르게 일정을 잡아 주셨습니다.",
    ),
    (
        "이사폐기물처리",
        "이사 후 남은 가구와 박스를 당일 처리해 주셔서 입주 일정에 맞췄습니다.",
    ),
    (
        "이사폐기물처리",
        "대형 폐기물 반출이 필요했는데, 1톤 기준으로 명확히 안내해 주셨습니다.",
    ),
    (
        "이사폐기물처리",
        "이사 잔짐과 생활폐기물을 한 번에 처리해 주셔서 편했습니다.",
    ),
    (
        "이사폐기물처리",
        "계단 작업이 필요한데도 안전하게 반출해 주셨습니다.",
    ),
    (
        "이사폐기물처리",
        "이사 폐기물 양을 사진으로 보내니 예상 비용을 바로 안내받았습니다.",
    ),
]


def service_reviews_for(region_name=None):
    if not region_name:
        return list(SERVICE_REVIEWS)
    return [(f"{region_name} {title}", body) for title, body in SERVICE_REVIEWS]

def case_section(region_name):
    imgs = image_set(region_name + "case")
    info = region_info(region_name)
    rng = region_rng(region_name, "cases")

    case_pools = [
        (
            "아파트 유품정리",
            imgs["before"][0],
            [
                f"{region_name} 아파트에서는 {info['focus']}를 먼저 확인한 뒤, 보관 물품과 정리 물품을 구분해 폐기물 반출까지 진행했습니다.",
                f"{region_name} 대단지·일반 아파트 현장에서 관리 동선을 맞추고, 가구와 생활용품을 나눠 마무리 정리했습니다.",
                f"{info['housing']} 특성을 반영해 {region_name} 아파트 유품정리를 층수·엘리베이터 조건에 맞춰 진행했습니다.",
            ],
        ),
        (
            "원룸·소형 공간 정리",
            imgs["before"][1],
            [
                f"{region_name} 원룸·오피스텔에서는 의류·소형가전·생활용품을 빠르게 분류하고 필요한 물품만 따로 확인했습니다.",
                f"공간이 좁은 {region_name} 현장에서도 반출 동선을 확보한 뒤 유품정리와 잔짐 처리를 함께 진행했습니다.",
                f"{region_name} 소형 주거는 물량이 적더라도 중요 서류와 보관품을 우선 구분해 정리했습니다.",
            ],
        ),
        (
            "단독주택 유품정리",
            imgs["process"][0],
            [
                f"{region_name} 단독주택에서는 방·거실·창고를 구역으로 나눠 {info['housing']}에 맞는 순서로 정리했습니다.",
                f"{region_name} 주택 현장은 마당·창고 물품까지 확인해 본채와 부속 공간의 범위를 구분해 진행했습니다.",
                f"오래된 가구와 생활폐기물이 섞인 {region_name} 주택에서 보관품 분류를 우선한 뒤 반출을 진행했습니다.",
            ],
        ),
        (
            "고독사청소",
            imgs["process"][1],
            [
                f"{region_name} 고독사청소 현장은 냄새·오염 여부를 먼저 확인한 뒤 정리·소독·탈취 범위를 안내했습니다.",
                f"{region_name}에서 장기 방치 흔적이 있는 공간은 일반 유품정리와 구분해 특수청소 필요성을 함께 설명드렸습니다.",
                f"위생·악취 이슈가 있는 {region_name} 현장은 작업 순서를 나눠 안전하게 마무리했습니다.",
            ],
        ),
        (
            "특수청소",
            imgs["after"][2],
            [
                f"{region_name} 특수청소는 일반 청소로 어려운 오염과 방치 흔적을 현장 상태에 맞춰 정리했습니다.",
                f"{info['focus']}가 겹친 {region_name} 오염 현장은 확인 후 소독·탈취 범위를 명확히 안내했습니다.",
                f"{region_name} 방치 공간은 오염 범위를 구획한 뒤 유품 분류와 특수청소를 병행했습니다.",
            ],
        ),
        (
            "빈집정리",
            imgs["after"][3],
            [
                f"{region_name} 빈집정리는 상속·매매·임대 준비에 맞춰 남은 물품과 폐기물을 정리하는 방식으로 진행했습니다.",
                f"오래 비워둔 {region_name} 공간은 습기·냄새 여부를 확인하며 빈집정리와 필요 시 특수청소를 안내했습니다.",
                f"{region_name} 빈집은 {info['housing']} 특성에 맞춰 구역을 나눈 뒤 잔짐과 가구를 처리했습니다.",
            ],
        ),
    ]

    cards = ""
    for title, img, descs in case_pools:
        desc = rng.choice(descs)
        cards += f"""
      <div class="case">
        <img src="{img}" alt="{region_name} {title}">
        <div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </div>
"""

    leads = [
        f"{region_name}에서 자주 접수되는 현장 유형별 사례입니다.",
        f"{info['housing']} 중심으로 본 {region_name} 작업 사례입니다.",
        f"{region_name} 상담 시 참고하기 좋은 유형별 정리 사례입니다.",
    ]

    return f"""
<section>
  <div class="wrap">

    <div class="section-title">
      <h2>{region_name} 유품정리 작업사례</h2>
      <p>{rng.choice(leads)}</p>
    </div>

    <div class="case-grid">
      {cards}
    </div>

  </div>
</section>
"""


def build_reviews(region_name):
    if region_name in REGION_REVIEWS:
        base = REGION_REVIEWS[region_name]
    else:
        info = region_info(region_name)
        rng = region_rng(region_name, "reviews")
        templates = [
            (
                f"{region_name} 유품정리",
                f"{region_name} {info['housing']} 유품정리를 맡겼습니다. {info['focus']}까지 확인해 주셔서 진행이 수월했습니다.",
                f"{region_name}에서 유품정리를 진행했습니다. 보관할 물건과 정리할 물건을 구분해 주셔서 안심이 됐습니다.",
                f"{region_name} 유품정리 상담부터 마무리까지 설명이 명확해 가족 모두가 만족했습니다.",
            ),
            (
                f"{region_name} 고독사청소",
                f"{region_name} 고독사청소가 급했는데, 냄새와 오염 상태를 먼저 확인해 주시고 정리·소독까지 차분히 진행해 주셨습니다.",
                f"{region_name}에서 고독사청소를 문의했고, 특수청소 필요 범위를 솔직하게 안내받아 맡길 수 있었습니다.",
                f"{region_name} 고독사청소 후에도 공간이 한결 나아져 감사했습니다.",
            ),
            (
                f"{info['housing']} 정리",
                f"{region_name}은 {info['housing']}이라 {info['focus']}가 걱정이었는데, 현장에 맞춰 일정을 잡아 주셨습니다.",
                f"{region_name} 특성상 {info['focus']}가 중요했는데, 작업 전에 동선까지 확인해 주셔서 좋았습니다.",
                f"{region_name} {info['housing']} 정리 범위를 나눠 진행해 주셔서 부담이 줄었습니다.",
            ),
            (
                "상담·일정 안내",
                f"{region_name}까지 방문해 현장 상황을 보신 뒤 비용과 일정을 명확히 설명해 주셨습니다. {info['tip']}",
                f"{region_name} 유품정리 비용(기본 안내 금액)과 추가 가능 범위를 미리 들을 수 있어 상의가 편했습니다.",
                f"{region_name} 상담 응대가 빨라 급한데도 일정 조율이 가능했습니다.",
            ),
        ]
        base = []
        for title, *bodies in templates:
            base.append((title, rng.choice(bodies)))
        base = base[:4]

    return base + service_reviews_for(region_name)


def review_section(region_name=None):
    name = region_name or "경남·부산·울산"
    reviews = build_reviews(region_name) if region_name else [
        ("친절한 상담", "급하게 문의드렸는데 일정 조율과 설명을 자세히 해주셨습니다."),
        ("깔끔한 정리", "보관 물품을 따로 정리해 주셔서 큰 도움이 되었습니다."),
        ("신속한 진행", "예상보다 빠르게 정리가 완료되어 만족했습니다."),
        ("맞춤 안내", "경남·부산·울산 현장 특성에 맞춰 작업 범위를 설명해 주셨습니다."),
    ] + list(SERVICE_REVIEWS)

    cards = "\n".join(
        f"""      <div class="review-card">
        <h3>{esc(title)}</h3>
        <p>{esc(body)}</p>
      </div>"""
        for title, body in reviews
    )

    lead = (
        f"{name} 상담·작업 후 남겨주신 후기 일부입니다."
        if region_name
        else "상담과 작업 후 남겨주신 후기 일부입니다."
    )

    return f"""
<section class="review">

  <div class="wrap">

    <div class="section-title">
      <h2>{name} 고객 후기</h2>
      <p>{lead}</p>
    </div>

    <div class="review-grid">

{cards}

    </div>

  </div>

</section>
"""


def service_section(region_name=None):
    info = region_info(region_name) if region_name else None
    rng = region_rng(region_name or "main", "service")

    if info:
        yupum = rng.choice([
            f"{region_name} 현장에서 고인의 생활 물품을 확인하고 보관·정리 기준을 가족과 맞춰 진행합니다.",
            f"{info['housing']} 특성에 맞춰 {region_name} 유품을 분류하고 필요한 물품을 따로 확인합니다.",
            f"{region_name} 유품정리는 {info['focus']}를 고려해 작업 순서와 범위를 안내합니다.",
        ])
        godok = rng.choice([
            f"{region_name} 고독사청소는 냄새·오염·장기 방치 흔적을 확인한 뒤 정리 범위를 안내합니다.",
            f"위생 이슈가 있는 {region_name} 공간은 일반 정리와 구분해 소독·탈취 필요 여부를 설명드립니다.",
            f"{region_name}에서 방치 기간이 긴 현장은 고독사청소·특수청소 가능 범위를 함께 상담합니다.",
        ])
        special = rng.choice([
            f"일반 청소로 어려운 {region_name} 오염·악취 공간은 특수청소로 구분해 안내합니다.",
            f"{region_name} 특수청소는 현장 상태를 본 뒤 작업 범위와 일정을 나눠 설명드립니다.",
            f"{info['focus']}와 오염이 겹친 경우 특수청소 필요성을 명확히 안내합니다.",
        ])
        empty = rng.choice([
            f"{region_name} 빈집정리는 상속·매매·임대 전후 남은 물품과 폐기물을 정리합니다.",
            f"오래 비워둔 {region_name} 공간은 습기·잔짐 여부를 확인하며 빈집정리를 진행합니다.",
            f"{info['housing']} 빈집은 구역을 나눠 잔짐과 가구를 처리합니다.",
        ])
        title = f"{region_name} 주요 서비스"
        lead = f"{region_name} 상황에 맞는 정리·청소 범위를 안내합니다."
    else:
        yupum = "고인의 생활 물품을 확인하고 보관 물품과 정리 물품을 구분합니다."
        godok = "냄새, 오염, 장기 방치 흔적이 있는 현장을 확인하고 정리합니다."
        special = "일반 청소로 어려운 오염과 악취, 방치 공간을 정리합니다."
        empty = "상속, 매매, 임대 전후 남은 물품과 폐기물을 정리합니다."
        title = "주요 서비스"
        lead = "상황에 맞는 정리와 청소 범위를 안내합니다."

    return f"""
<section id="service">
  <div class="wrap">
    <div class="section-title">
      <h2>{title}</h2>
      <p>{lead}</p>
    </div>

    <div class="grid">
      <div class="card">
        <h3>유품정리</h3>
        <p>{yupum}</p>
      </div>

      <div class="card">
        <h3>고독사청소</h3>
        <p>{godok}</p>
      </div>

      <div class="card">
        <h3>특수청소</h3>
        <p>{special}</p>
      </div>

      <div class="card">
        <h3>빈집정리</h3>
        <p>{empty}</p>
      </div>
    </div>
  </div>
</section>
"""


def price_section(region_name="경남·부산·울산"):
    info = region_info(region_name) if region_name in REGION_COPY else None
    rng = region_rng(region_name, "price")
    leads = [
        "표시 금액은 기본 안내 금액이며, 정확한 비용은 현장 확인 후 작업 범위에 따라 안내드립니다.",
        f"{region_name} 기준 기본 안내 금액이며, 현장 확인 후 작업 범위에 따라 최종 안내드립니다.",
        "아래 금액은 시작 안내가이며, 물품 양·동선·특수청소 여부에 따라 달라질 수 있습니다.",
    ]
    notices = [
        "현장 구조와 물품 양에 따라 비용이 달라질 수 있습니다.",
        f"{region_name} 현장의 {info['focus'] if info else '구조·물량'}에 따라 비용이 달라질 수 있습니다.",
        "정확한 견적은 주소와 현장 사진 확인 후 안내드립니다.",
    ]
    return f"""
<section class="price" id="price">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 비용 안내</h2>
      <p>{rng.choice(leads)}</p>
    </div>

    <div class="price-box">
      <div class="price-card">
        <span class="price-label">유품정리</span>
        <div class="price-num">25만원부터</div>
        <p>중요 물품 확인, 생활용품 분류, 폐기물 분류, 공간 정리 상담</p>
      </div>

      <div class="price-card featured">
        <span class="price-label">고독사청소</span>
        <div class="price-num">80만원부터</div>
        <p>오염 범위 확인, 악취·위생 문제, 특수청소 필요 여부에 따라 안내</p>
      </div>

      <div class="price-card">
        <span class="price-label">폐기물처리</span>
        <div class="price-num">25만원부터</div>
        <p>1톤 1대 기준. 폐기물 양, 운반 거리, 층수에 따라 변동 가능</p>
      </div>
    </div>
    <div class="price-notice">{rng.choice(notices)}</div>
  </div>
</section>
"""


def price_factor_section(region_name="경남·부산·울산"):
    info = region_info(region_name) if region_name in REGION_COPY else {
        "housing": "다양한 주거 형태",
        "focus": "현장 조건",
        "tip": "주소와 물품 양을 알려주시면 안내가 정확해집니다.",
    }
    rng = region_rng(region_name, "factors")
    cards = [
        ("물품과 폐기물 양", rng.choice([
            f"{region_name} 현장은 장롱·냉장고·침대·생활용품·창고 물품이 많을수록 작업 범위가 커집니다.",
            f"보관품과 폐기품 비율에 따라 {region_name} 작업 시간과 인력이 달라집니다.",
            f"{info['housing']}에서는 가구·잔짐 양이 비용과 일정에 큰 영향을 줍니다.",
        ])),
        ("반출 동선", rng.choice([
            f"엘리베이터 유무, 계단 작업, 차량 진입 가능 여부가 {region_name} 작업 시간에 영향을 줍니다.",
            f"{info['focus']}와 연결된 반출 동선을 {region_name} 상담 단계에서 확인합니다.",
            f"주차·하차 위치가 제한되면 {region_name} 운반 방식을 조정해 안내합니다.",
        ])),
        ("오염·냄새 여부", rng.choice([
            f"고독사청소나 특수청소가 필요하면 {region_name} 소독·탈취 작업이 추가될 수 있습니다.",
            f"장기 방치·습기·악취가 있으면 일반 유품정리와 범위를 구분해 안내합니다.",
            f"{region_name} 현장 위생 상태에 따라 특수청소 포함 여부를 설명드립니다.",
        ])),
        ("보관 물품 분류", rng.choice([
            f"통장·도장·서류·사진·귀금속 등 확인 물품이 많으면 {region_name} 분류 시간이 필요합니다.",
            f"가족이 남길 물건을 미리 정해 주시면 {region_name} 현장 분류가 더 정확해집니다.",
            f"{info['tip']}",
        ])),
    ]
    lead = rng.choice([
        f"같은 평수라도 {region_name} 현장 조건에 따라 작업 시간과 인력이 달라집니다.",
        f"{info['housing']} 기준으로 본 {region_name} 비용 변동 요인입니다.",
        f"{region_name}에서 견적 차이가 생기는 대표 요소입니다.",
    ])
    grid = "\n".join(
        f"""      <div class="card">
        <h3>{title}</h3>
        <p>{body}</p>
      </div>"""
        for title, body in cards
    )
    return f"""
<section>
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 비용에 영향을 주는 요소</h2>
      <p>{lead}</p>
    </div>

    <div class="grid">
{grid}
    </div>
  </div>
</section>
"""


def seo_section(region_name, feature):
    info = region_info(region_name)
    rng = region_rng(region_name, "seo")
    p1 = rng.choice([
        f"{region_name} 유품정리는 단순 수거가 아니라, 고인의 생활 흔적 속에서 중요한 물품을 확인하고 가족이 보관할 것과 정리할 것을 나누는 과정입니다.",
        f"{region_name}에서 유품정리를 진행할 때는 먼저 보관 기준을 정한 뒤, 생활용품·가구·폐기물을 구분해 공간을 정리합니다.",
        f"{region_name} 유품정리는 {info['housing']} 환경에 맞춰 분류·반출·마무리 순서를 현장에 맞게 조정합니다.",
    ])
    p2 = f"{feature}입니다. {info['note']}"
    p3 = rng.choice([
        f"같은 {region_name}이라도 아파트, 빌라, 단독주택, 원룸, 상가주택에 따라 작업 방식과 시간이 달라질 수 있습니다.",
        f"{region_name} 내에서도 {info['focus']}에 따라 인력·차량·소요 시간이 달라지므로 사전 확인이 중요합니다.",
        f"{info['housing']}이 섞인 {region_name}에서는 현장 형태를 먼저 파악한 뒤 일정을 안내합니다.",
    ])
    prep = rng.choice([
        f"주소, 주거 형태, 층수, 엘리베이터 유무, 물품의 대략적인 양, 보관해야 할 물품 여부를 알려주시면 {region_name} 상담이 더 정확해집니다. {info['tip']}",
        f"{region_name} 상담 전에는 현장 사진과 함께 {info['focus']} 관련 정보를 남겨 주시면 빠른 안내가 가능합니다. {info['tip']}",
        f"희망 일정과 정리 범위를 구체적으로 남겨 주시면 {region_name} 방문·견적 안내가 수월합니다. {info['tip']}",
    ])
    godok = rng.choice([
        f"장기간 방치되거나 냄새·오염이 남은 {region_name} 현장은 일반 유품정리만으로 끝나지 않을 수 있습니다. 이 경우 소독·탈취·특수청소 범위를 함께 안내합니다.",
        f"{region_name} 고독사청소·특수청소가 필요하면 오염 범위를 확인한 뒤 유품 분류와 위생 작업을 구분해 진행합니다.",
        f"습기·악취·방치 흔적이 있는 {region_name} 공간은 현장 확인 후 특수청소 포함 여부를 명확히 설명드립니다.",
    ])
    checks = rng.sample([
        "통장, 도장, 계약서 등 중요 서류",
        "사진, 앨범, 편지 등 추억 물품",
        "귀금속, 현금, 보관 물품",
        "폐기물 양과 반출 동선",
        "냄새, 오염, 특수청소 필요 여부",
        f"{info['focus']} 관련 현장 조건",
        "엘리베이터·주차·진입로 상태",
        "창고·마당 등 부속 공간 포함 여부",
    ], 5)
    check_lis = "\n".join(f"      <li>{c}</li>" for c in checks)

    return f"""
<section class="seo">
  <div class="wrap">
    <h2>{region_name} 유품정리, 현장마다 달라지는 이유</h2>

    <p>{p1}</p>

    <p>{p2}</p>

    <p>{p3}</p>

    <h3>{region_name} 유품정리 전 먼저 확인하는 것</h3>

    <ul>
{check_lis}
    </ul>

    <h3>{region_name} 고독사청소와 특수청소가 필요한 경우</h3>

    <p>{godok}</p>

    <h3>{region_name} 유품정리 상담 전 준비하면 좋은 내용</h3>

    <p>{prep}</p>
  </div>
</section>
"""


def process_section(region_name):
    info = region_info(region_name)
    rng = region_rng(region_name, "process")
    steps = [
        ("상담 접수", rng.choice([
            f"{region_name} 주소, 주거 형태, 정리 범위, 희망 일정을 확인합니다.",
            f"연락처와 함께 {info['focus']}에 대한 현장 정보를 받아 상담을 시작합니다.",
            f"{region_name} 상담 시 보관 물품 기준과 폐기물 처리 희망 여부를 함께 확인합니다.",
        ])),
        ("현장 확인", rng.choice([
            f"사진 또는 방문으로 {region_name} 물품 양과 작업 범위를 파악합니다.",
            f"{info['housing']} 구조와 반출 동선을 확인해 인력·차량을 산정합니다.",
            f"{region_name} 현장의 층수·진입·오염 여부를 확인합니다.",
        ])),
        ("중요 물품 분류", rng.choice([
            "서류, 사진, 귀중품 등 보관 물품을 먼저 확인합니다.",
            f"가족이 남길 물건을 기준으로 {region_name} 현장에서 우선 분류합니다.",
            "통장·도장·계약서·앨범 등을 별도로 구분해 안내합니다.",
        ])),
        ("정리 및 처리", rng.choice([
            f"보관 물품과 폐기 물품을 구분해 {region_name} 현장에 맞춰 처리합니다.",
            f"유품정리와 필요 시 고독사청소·폐기물처리를 범위에 맞게 진행합니다.",
            f"{info['focus']}를 고려한 순서로 정리와 반출을 진행합니다.",
        ])),
        ("마무리 확인", rng.choice([
            "작업 완료 후 요청사항과 현장 상태를 최종 확인합니다.",
            f"{region_name} 공간 상태와 추가 요청을 확인한 뒤 마무리합니다.",
            "정리 결과와 폐기물 처리 여부를 함께 확인해 드립니다.",
        ])),
    ]
    lead = rng.choice([
        f"{region_name} 상담부터 마무리 확인까지 순서대로 진행합니다.",
        f"{info['housing']} 현장에 맞춘 {region_name} 진행 절차입니다.",
        f"{region_name} 유품정리는 확인·분류·처리·마무리 순으로 진행합니다.",
    ])
    body = ""
    for i, (title, desc) in enumerate(steps, 1):
        body += f"""
    <div class="step">
      <div class="num">{i}</div>
      <div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>
    </div>
"""
    return f"""
<section class="process">
  <div class="wrap">
    <div class="section-title">
      <h2>{region_name} 유품정리 진행과정</h2>
      <p>{lead}</p>
    </div>
{body}
  </div>
</section>
"""


def build_faqs(region_name):
    info = region_info(region_name)
    rng = region_rng(region_name, "faq")
    cost = (
        f"{region_name} 유품정리 비용은 어떻게 정해지나요?",
        f"유품정리는 25만원부터, 고독사청소는 80만원부터, 폐기물처리는 1톤 1대 기준 25만원부터 안내드리며, {region_name}의 {info['focus']}와 물품 양에 따라 달라질 수 있습니다.",
    )
    local = info["faq"]
    pool = [
        (f"{region_name} 고독사청소도 함께 가능한가요?", f"가능합니다. {region_name} 현장의 냄새·오염·방치 여부를 확인한 뒤 특수청소 범위를 안내합니다."),
        (f"{region_name} 빈집정리도 하나요?", f"가능합니다. 상속·매매·임대 전후 {region_name} 공간의 잔짐과 폐기물을 정리합니다."),
        (f"{region_name} 당일 상담도 가능한가요?", f"일정에 따라 가능합니다. {region_name} 주소와 현장 사진을 보내주시면 더 빠르게 안내드립니다."),
        (f"{region_name}에서 중요 물품은 따로 확인하나요?", "통장, 도장, 계약서, 사진, 귀금속 등은 작업 중 별도로 확인합니다."),
        (f"{region_name} 아파트·주택 모두 가능한가요?", f"가능합니다. {info['housing']} 모두 상담하며, 구조에 맞춰 일정을 안내합니다."),
        (f"{region_name} 폐기물처리만 상담할 수 있나요?", "유품정리와 함께 상담하는 경우가 많으며, 범위에 따라 폐기물처리 안내도 가능합니다."),
    ]
    extras = rng.sample(pool, 3)
    # unique order: cost, local, extras (dedupe by question)
    seen = set()
    faqs = []
    for item in [cost, local, *extras]:
        if item[0] in seen:
            continue
        seen.add(item[0])
        faqs.append(item)
    return faqs[:5]


def faq_section_fixed(region_name):
    faqs = build_faqs(region_name)
    items = ""
    for i, (q, a) in enumerate(faqs):
        open_attr = " open" if i == 0 else ""
        items += f"""
    <details{open_attr}>
      <summary>{q}</summary>
      <p>{a}</p>
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


def faq_section(region_name):
    return faq_section_fixed(region_name)


def faq_schema(region_name):
    faqs = build_faqs(region_name)
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
    desc = f"{BRAND}는 경남, 부산, 울산 전지역 유품정리, 고독사청소, 특수청소 상담. 유품정리 25만원부터, 고독사청소 80만원부터, 폐기물처리 1톤 1대 기준 25만원부터 안내드립니다."
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
    info = region_info(name)
    rng = region_rng(name, "hero")
    desc = f"{name} 유품정리, 고독사청소, 특수청소 상담. 유품정리 25만원부터, 고독사청소 80만원부터, 폐기물처리 1톤 1대 기준 25만원부터. {info['housing']} 중심. {BRAND} {PHONE}"
    url = f"{SITE_URL}/regions/{slug}.html"
    subtitle = rng.choice([
        f"{name} 유품정리·고독사청소·특수청소·빈집정리를 안내합니다. {info['note']}",
        f"{name}의 {info['housing']} 특성에 맞춰 중요 물품 분류부터 폐기물 처리까지 상담합니다. {info['tip']}",
        f"{name} 현장에서 {info['focus']}를 확인한 뒤 유품정리와 필요 시 특수청소 범위를 안내드립니다.",
    ])
    badge = rng.choice([
        f"{group} {name} 상담",
        f"{name} 방문 상담 가능",
        f"{group} · {name} 유품정리",
    ])

    return f"""<!DOCTYPE html>
<html lang="ko">
{head(title, desc, url)}
<body>
{header()}
<main>
{hero_section(f"{name} 유품정리<br>{BRAND}", subtitle, badge)}
{service_section(name)}
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
      <p>{name} 외 인근·상위 지역 페이지로 이동할 수 있습니다.</p>
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
{faq_schema(name)}
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