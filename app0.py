import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # HTTPステータスコードを設定
        resp.body = "Hello, World!"    # レスポンスの内容を設定

# Falconアプリケーションを作成
app = falcon.App()

# HelloWorldResourceクラスをルートとして登録
app.add_route('/', HelloWorldResource())

if __name__ == '__main__':
    # HTTPサーバーを起動し、Falconアプリケーションを実行
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
