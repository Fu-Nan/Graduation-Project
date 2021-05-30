# encoding:gbk
# 读取全部行数据
appFile = open("app.csv", "r", encoding="utf8")
lines = appFile.readlines()
appFile.close()
print("读取数据")
# 将数据另存到data.csv中
dataFile = open("data.csv", "w", encoding="utf8")
for line in lines:
    # 去掉两段空格并获取字符串长度
    lineLen = len(line.strip())
    if lineLen != 0:
        dataFile.write(line)
dataFile.close()
print("数据处理完成")
