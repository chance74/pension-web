from flask import Flask, render_template

app = Flask(__name__)

# 임시 객실 데이터 (나중에 실제 펜션 정보로 수정하시면 됩니다)
ROOMS = [
    {
        "id": 1,
        "name": "포레스트 스위트 (Forest Suite)",
        "desc": "통창으로 숲속 뷰가 펼쳐지는 복층형 프리미엄 객실입니다.",
        "price": "250,000원 / 1박",
        "capacity": "기준 2인 / 최대 4인",
        "image": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "name": "레이크 뷰 테라스 (Lake View)",
        "desc": "프라이빗 테라스에서 개별 바비큐를 즐길 수 있는 아늑한 공간입니다.",
        "price": "180,000원 / 1박",
        "capacity": "기준 2인 / 최대 3인",
        "image": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "name": "가든 패밀리 룸 (Garden Family)",
        "desc": "넓은 잔디 마당과 연결되어 가족 단위 여행객에게 추천합니다.",
        "price": "320,000원 / 1박",
        "capacity": "기준 4인 / 최대 6인",
        "image": "https://images.unsplash.com/photo-1542718610-a1d656d1884c?auto=format&fit=crop&w=800&q=80"
    }
]

@app.route('/')
def home():
    # index.html 파일을 불러오면서 ROOMS 데이터를 함께 전달합니다.
    return render_template('index.html', rooms=ROOMS)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)