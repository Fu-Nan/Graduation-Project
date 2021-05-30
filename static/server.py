from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from router import app

if __name__ == "__main__":
    # 使用WSGI容器家宅Flask Web应用程序
    httpServer = HTTPServer(WSGIContainer(app))
    # 监听8000端口
    httpServer.listen(8000)
# 启动Web服务器实例
IOLoop.instance().start()
