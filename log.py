import datetime

def Log(key, comment):
    File = open("Log.txt","a", encoding="utf-8")
    if key == "CRE":
        File.write("Создание экземпляра класса")
    if key == "INF":
        File.write("Изменение")
    if key =="ERR":
        File.write("Сработало исключение")
    File.write(f" --- {datetime.datetime.now()} --- {comment}\n")
    File.close()