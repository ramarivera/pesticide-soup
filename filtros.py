from bs4 import BeautifulSoup,Tag


def div_content(tag: Tag) -> bool:
    aux = tag.name == 'div' and tag.get("id") == "content"
    if aux:
        print("Name: {0}, 'id':{1}".format(tag.name, tag.get("id")))
    return aux


def happen_box(tag: Tag) -> bool:
    aux = tag.name == "div" and "happen-box" in tag.get('class', [])
    if aux:
        print("Name: {0}, class:{1}".format(tag.name, tag.get('class')))
    return aux


def titulo_noticia(tag : Tag) -> bool:
    aux = happen_box(tag)
    if aux:
        print (tag.h1.span.text)

    return aux


