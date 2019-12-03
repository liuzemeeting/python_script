import os


def insert_data(item):
    file = open("data3.txt", "a+", encoding="utf-8")
    file.write(item+"\n")
    file.close()


if __name__ == "__main__":
    for root, dirs, files in os.walk("tornado", topdown=False):
        for item in files:
            try:
                f = open(root + "\\" + item, "r", encoding="utf-8")
                data = f.readlines()
                for i in data:
                    insert_data(i)
                f.close()
            except Exception as e:
                continue