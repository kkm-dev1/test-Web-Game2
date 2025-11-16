from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """
    지렁이 키우기 게임 메인 페이지
    SEO 최적화를 위해 간단한 서버 사이드 렌더링 제공
    """
    return render_template('game.html')

@app.route('/robots.txt')
def robots():
    """
    검색 엔진 크롤러를 위한 robots.txt 제공
    """
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    """
    검색 엔진을 위한 사이트맵 제공
    """
    return send_from_directory('static', 'sitemap.xml')

if __name__ == '__main__':
    # static 폴더가 없으면 생성
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, port=5000)


