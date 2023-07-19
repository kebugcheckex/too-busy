import xmltodict


def read_xml():
    with open("./Gujian2-Steam.CT", encoding="utf-8") as xml_file:
        content = xml_file.read()
        return xmltodict.parse(content)


def create_table(items_data):
    pass

def process():
    data = read_xml()
    data = data["CheatTable"]["CheatEntries"]["CheatEntry"]
    for item in data:
        for key, value in item.items():
            


if __name__ == "__main__":
    process()
