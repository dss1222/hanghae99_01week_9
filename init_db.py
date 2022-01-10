from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.project

BBQ = [
   {'chicken_id': 1, 'name': '눈맞은 닭', 'img_url': 'https://img.bbq.co.kr:449/uploads/bbq_d/mobile/%EB%88%88%EB%A7%9E%EC%9D%80%EB%8B%AD%20%EC%8D%B8%EB%84%A4%EC%9D%BC(0).png',
  'like': 0, 'dislike': 0, 'status': '짭조름한 특제간장 소스&고소한 갈릭 후레이크, 단짠단짠 바삭한 윙&봉 치킨 위에 눈꽃같은 갈릭스노우가 듬뿍!', 'brand': 'BBQ'},
   {'chicken_id': 2,'name': '황금 올리브', 'img_url': 'https://img.bbq.co.kr:449/uploads/bbq_d/mobile/BBQ_%EC%95%B1_%EC%8D%B8%EB%84%A4%EC%9D%BC(480x480)_%ED%9B%84%EB%9D%BC%EC%9D%B4%EB%93%9C%EB%A5%98_%ED%99%A9%EA%B8%88%EC%98%AC%EB%A6%AC%EB%B8%8C%EC%B9%98%ED%82%A8_%EC%88%98%EC%A0%95_out.png',
    'like': 0, 'dislike': 0, 'status': '육즙 가득한 BBQ 대표 메뉴', 'brand': 'BBQ'},
   {'chicken_id': 3, 'name': '체고치', 'img_url': 'https://img.bbq.co.kr:449/uploads/bbq_d/mobile/20210323_BBQ_%EC%95%B1_%EC%8D%B8%EB%84%A4%EC%9D%BC(480x480)_%EC%B2%B4%EA%B3%A0%EC%B9%98_01.jpg',
    'like': 0, 'dislike': 0, 'status': '치즐링에 체다, 고다치즈 한번 더! 치즈맛의 최고치, 체고치 순살!', 'brand': 'BBQ'},

   {'chicken_id': 4, 'name': '극한 왕갈비', 'img_url': 'https://img.bbq.co.kr:449/uploads/bbq_d/mobile/20200717_BBQ_%EC%95%B1_%EC%8D%B8%EB%84%A4%EC%9D%BC(%EC%96%91%EB%85%90%EB%A5%98)_%EA%B7%B9%ED%95%9C%EC%99%95%EA%B0%88%EB%B9%84.png',
    'like': 0, 'dislike': 0, 'status': 'BBQ 극한왕갈비치킨.', 'brand': 'BBQ'},
   {'chicken_id': 5, 'name': '자메이카 통다리', 'img_url': 'https://img.bbq.co.kr:449/uploads/bbq_d/mobile/20210318_BBQ_%EC%95%B1_%EC%8D%B8%EB%84%A4%EC%9D%BC_%EA%B5%AC%EC%9D%B4%EB%A5%98(480x480px)-%EC%9E%90%EB%A9%94%EC%9D%B4%EC%B9%B4%ED%86%B5%EB%8B%A4%EB%A6%AC%EA%B5%AC%EC%9D%B4.jpg',
    'like': 0, 'dislike': 0, 'status': '자메이카 저크소스를 발라 더욱 맛있는 통다리구이!', 'brand': 'BBQ'},
]

Puradak = [
   {'chicken_id': 6, 'name': '콘소메이징', 'img_url': 'https://www.puradakchicken.com/upload/menu/%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF_%E1%84%8F%E1%85%A9%E1%86%AB%E1%84%89%E1%85%A9%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%E1%86%BC%E1%84%88%E1%85%A7_pc0.png',
  'like': 0, 'dislike': 0, 'status': '소복히 뿌려낸 단짠단짠 콘소메 시즈닝에 바삭한 옥수수 후레이크와 쫄깃한 리얼 군옥수수 토핑까지! 입안 가득 와르르 쏟아지는 옥수수의 무한 매력을 즐겨보세요', 'brand': 'Puradak'},
   {'chicken_id': 7, 'name': '블랙알리오', 'img_url': 'https://www.puradakchicken.com/upload/menu/%E1%84%86%E1%85%A6%E1%84%82%E1%85%B2-040.png',
    'like': 0, 'dislike': 0, 'status': '깊고 진한 간장과 고소하면서 담백한 마늘의 만남! 치킨을 넘어 진정한 요리를 느낄 수 있는 푸라닭의 대표 메뉴.', 'brand': 'Puradak'},
   {'chicken_id': 8, 'name': '매드갈릭 치킨', 'img_url': 'https://www.puradakchicken.com/upload/menu/%E1%84%86%E1%85%A6%E1%84%82%E1%85%B2-220.png',
    'like': 0, 'dislike': 0, 'status': '마늘에 미치다. 깊은 마늘향, 알싸한 마늘의 맛과 바삭한 마늘크러쉬드의 환상적인 조합. 기존의 마늘치킨의 업그레이드 버전.', 'brand': 'Puradak'},

   {'chicken_id': 9, 'name': '고추마요 치킨', 'img_url': 'https://www.puradakchicken.com/upload/menu/%E1%84%86%E1%85%A6%E1%84%82%E1%85%B2-290.png',
    'like': 0, 'dislike': 0, 'status': '강력추천! 한 입 먹으면 계속 손이 갈 수 밖에 없는 마법의 치킨. 맵다, 부드럽다, 고소하다, 달콤하다, 새콤하다. 맛의 조합이 환상적인 강추메뉴.', 'brand': 'Puradak'},
   {'chicken_id': 10, 'name': '투움바 치킨', 'img_url': 'https://www.puradakchicken.com/upload/menu/(%EA%B5%90%EC%B2%B4)%ED%88%AC%EC%9B%80%EB%B0%94%EC%B9%98%ED%82%A80.jpg',
    'like': 0, 'dislike': 0, 'status': '고소한 크림소스에 매콤함을 더해 완성된 푸라닭만의 투움바 치킨! 부드럽게 매콤한 투움바 풍미에 한번, 로제 빛 비주얼에 두번, 쫄깃한 떡사리에 세번 반할 수 밖에 없는 매력만점 신개념 치킨!', 'brand': 'Puradak'},
]

BHC = [
   {'chicken_id': 11, 'name': '뿌링클', 'img_url': 'http://www.bhc.co.kr//upload/bhc/menu//BB(0).jpg',
  'like': 0, 'dislike': 0, 'status': '뿌링뿌링! 세상에 없던 마법의 맛 뿌링클', 'brand': 'BHC'},
   {'chicken_id': 12, 'name': '맛초킹', 'img_url': 'http://www.bhc.co.kr//upload/bhc/menu//macho_20150728_v(1).jpg',
    'like': 0, 'dislike': 0, 'status': '매콤짭짤! 밥과 함께 먹기에 딱 좋은 완벽조합', 'brand': 'BHC'},
   {'chicken_id': 13, 'name': '골드퀸', 'img_url': 'http://www.bhc.co.kr//upload/bhc/menu//410x271_view_%EA%B3%A8%EB%93%9C%ED%95%9C%EB%A7%88%EB%A6%AC(0).png',
    'like': 0, 'dislike': 0, 'status': '단짠단짠! 숙성간장과 꿀의 황금비율', 'brand': 'BHC'},

   {'chicken_id': 14, 'name': '커리퀸', 'img_url': 'http://www.bhc.co.kr//upload/bhc/menu//%EC%8D%B8%EB%84%A4%EC%9D%BC_%EC%BB%A4%EB%A6%AC%ED%80%B8_%EC%83%81%EC%84%B8(2).jpg',
    'like': 0, 'dislike': 0, 'status': '나마스테! 인도 커리 파우더와 로스팅 갈릭 시즈닝을 더해 이국적인 맛', 'brand': 'BHC'},
   {'chicken_id': 15, 'name': '하바네로 포테킹 후라이드', 'img_url': 'http://www.bhc.co.kr//upload/bhc/menu//%ED%95%98%EB%B0%94%EB%84%A4%EB%A1%9C%20%ED%8F%AC%ED%85%8C%ED%82%B9_410x271(0).png',
    'like': 0, 'dislike': 0, 'status': '포텐폭발! 바삭한 감자가 팡팡, 세상에 없던 리얼 감자 후라이드 (스윗하바네로 소스 1개 포함)', 'brand': 'BHC'},

]
kyochon = [
   {'chicken_id': 16, 'name': '교촌 허니콤보', 'img_url': 'http://www.kyochon.com/uploadFiles/TB_ITEM/%EA%B5%90%EC%B4%8C-%ED%97%88%EB%8B%88-%EC%BD%A4%EB%B3%B4.png',
  'like': 0, 'dislike': 0, 'status': '달콤한 허니소스에 쫄깃한 날개와 담백한 다리가 만난 메뉴', 'brand': 'kyochon'},
   {'chicken_id': 17, 'name': '교촌 레드콤보', 'img_url': 'http://www.kyochon.com/uploadFiles/TB_ITEM/%EB%B8%8C%EB%9E%9C%EB%93%9C_list_15-10-231098.png',
    'like': 0, 'dislike': 0, 'status': '국내산 청양 홍고추의 매콤한 맛에 날개와 다리를 함께 즐길 수 있는 메뉴', 'brand': 'kyochon'},
   {'chicken_id': 18, 'name': '교촌 신화오리지날', 'img_url': 'http://www.kyochon.com/uploadFiles/TB_ITEM/%EC%8B%A0%ED%99%94%EC%98%A4%EB%A6%AC%EC%A7%80%EB%82%A0-(3).png',
    'like': 0, 'dislike': 0, 'status': '매콤한 불맛의 한 마리 치킨', 'brand': 'kyochon'},

   {'chicken_id': 19, 'name': '교촌 신화트러플순살', 'img_url': 'http://www.kyochon.com/uploadFiles/TB_ITEM/list_%EC%A0%9C%ED%92%88%EC%BB%B7_%EC%B9%98%EC%A6%88%ED%8A%B8%EB%9F%AC%ED%94%8C%EC%88%9C%EC%82%B4_new.png',
    'like': 0, 'dislike': 0, 'status': '진한 치즈 맛과 깊은 풍미의 트러플 향이 조화로운 부드러운 순살 치킨 (가슴살 100%)', 'brand': 'kyochon'},
   {'chicken_id': 20, 'name': '교촌 살살치킨', 'img_url': 'http://www.kyochon.com/uploadFiles/TB_ITEM/%EB%B8%8C%EB%9E%9C%EB%93%9C_list_15-10-221035.png',
    'like': 0, 'dislike': 0, 'status': '가슴살과 다리살이 쌀가루와 만나 고소하고 바삭한 맛이 일품', 'brand': 'kyochon'},
]
Goobne = [
   {'chicken_id': 21, 'name': '불금치킨', 'img_url': 'https://order.goobne.co.kr:8481//Upload/menu//2021122214542808_99ilfris.png',
  'like': 0, 'dislike': 0, 'status': '"불"맛 가득한 치킨 위에 "금"빛 버터 갈릭 소스를 드리즐해 매콤달달 고소한 맛이 조화로운 치킨', 'brand': 'Goobne'},
   {'chicken_id': 22, 'name': '갈릭마왕', 'img_url': 'https://order.goobne.co.kr:8481//Upload/menu//2021122214545110_0ab7fpei.png',
    'like': 0, 'dislike': 0, 'status': '국산 마늘을 국산 꿀과 함께 숙성시켜 달달하고 알싸한 맛이 어우러진 마늘 치킨', 'brand': 'Goobne'},
   {'chicken_id': 23, 'name': '갈비천왕', 'img_url': 'https://order.goobne.co.kr:8481//Upload/menu//101030414.png',
    'like': 0, 'dislike': 0, 'status': '정통 갈비양념의 깊은 맛을 그대로 품은 단짠단짠의 정석! 밥과 함께 일품요리로 즐길 수 있는 치킨', 'brand': 'Goobne'},

   {'chicken_id': 24, 'name': '고추바사삭', 'img_url': 'https://order.goobne.co.kr:8481//Upload/menu//2021072711194121_7611uuql.png',
    'like': 0, 'dislike': 0, 'status': '1초에 한마리씩 팔리는 굽네치킨 대표 메뉴, 매콤바삭 고추바사삭! 취향따라 마블링/고블링 소스와 함께 먹으면 더 맛있는 치킨', 'brand': 'Goobne'},
   {'chicken_id': 25, 'name': '볼케이노', 'img_url': 'https://order.goobne.co.kr:8481//Upload/menu//%EA%B5%BD%EB%84%A4%EB%B3%BC%EC%BC%80%EC%9D%B4%EB%85%B8_L_01.png',
    'like': 0, 'dislike': 0, 'status': '매운맛 치킨&치밥 열풍의 시초 볼케이노, 불맛과 감칠맛이 자꾸 생각나는 중독성 있는 치킨', 'brand': 'Goobne'},
]
Momstouch = [
   {'chicken_id': 26, 'name': '간장마늘 싸이순살', 'img_url': 'https://momstouchdev.co.kr/upload_file/product_info/1625637423-TDMIS.png',
  'like': 0, 'dislike': 0, 'status': '알싸한 마늘 향의 매콤함, 특제 간장소스의 단짠이 조화로운 닭다리살 순살치킨', 'brand': 'Momstouch'},
   {'chicken_id': 27, 'name': '블랙소이 싸이순살', 'img_url': 'https://momstouchdev.co.kr/upload_file/product_info/1625636522-SENXN.png',
    'like': 0, 'dislike': 0, 'status': '은은한 불향의 간장소스 풍미 가득, 이색 토핑을 듬뿍 넣은 닭다리살 순살치킨', 'brand': 'Momstouch'},
   {'chicken_id': 28, 'name': '치즈뿌치 싸이순살', 'img_url': 'https://momstouchdev.co.kr/upload_file/product_info/1625649541-WGVNE.png',
    'like': 0, 'dislike': 0, 'status': '스페셜 치즈 시즈닝의 단짠 매력이 환상적인 닭다리살 순살치킨', 'brand': 'Momstouch'},

   {'chicken_id': 29, 'name': '치파오  싸이순살', 'img_url': 'https://momstouchdev.co.kr/upload_file/product_info/1625649080-KITAI.png',
    'like': 0, 'dislike': 0, 'status': '라유에 볶아 은은한 파향, 흑임자와 매콤달콤한 중화풍 사천식 소스를 담은 닭다리살 순살치킨', 'brand': 'Momstouch'},
   {'chicken_id': 30, 'name': '유린기 순살치킨', 'img_url': '	https://momstouchdev.co.kr/upload_file/product_info/1631687569-PMQJP.png',
    'like': 0, 'dislike': 0, 'status': '중화 요리, 치킨을 품다! 맘스터치 유린기 순살치킨, 매콤새콤 간장소스, 아삭한 야채, 바삭 닭다리살을 한입에!', 'brand': 'Momstouch'},
]
db.chicken.drop()
db.chicken.insert_many(BBQ)
db.chicken.insert_many(Puradak)
db.chicken.insert_many(BHC)
db.chicken.insert_many(kyochon)
db.chicken.insert_many(Goobne)
db.chicken.insert_many(Momstouch)

