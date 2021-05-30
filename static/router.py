from flask import Flask, render_template
import numpy as np
import services.app

app = Flask(__name__)


# @app.route定义Web路由路径,实现url与请求处理函数对应
@app.route('/')
def index():
    service = services.app.AppService()
    serviceData = service.getAppAnalysis()
    serviceData["list"]["index"] = np.arange(len(serviceData["list"]))
    return render_template('index.html', data=serviceData)
