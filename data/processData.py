# encoding:gbk
# ��ȡȫ��������
appFile = open("app.csv", "r", encoding="utf8")
lines = appFile.readlines()
appFile.close()
print("��ȡ����")
# ��������浽data.csv��
dataFile = open("data.csv", "w", encoding="utf8")
for line in lines:
    # ȥ�����οո񲢻�ȡ�ַ�������
    lineLen = len(line.strip())
    if lineLen != 0:
        dataFile.write(line)
dataFile.close()
print("���ݴ������")
