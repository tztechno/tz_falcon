import falcon

class StaticResource:
    def on_get(self, req, resp):
        # index.htmlの内容を読み込み、レスポンスとして返す
        with open('index.html', 'r', encoding='utf-8') as f:
            resp.body = f.read()
        resp.content_type = falcon.MEDIA_HTML  # コンテンツタイプをHTMLとして設定

# Falconアプリケーションを作成
app = falcon.App()

# StaticResourceクラスをルートとして登録
app.add_route('/', StaticResource())

if __name__ == '__main__':
    # HTTPサーバーを起動し、Falconアプリケーションを実行
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
