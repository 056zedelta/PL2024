import sys 
import re

def mdtohtml(md):
    #Cabeçalhos
    md = re.sub(r'###\s+(.+)',r'<h3>\1</h3>', md)
    md = re.sub(r'##\s+(.+)',r'<h2>\1</h2>', md)
    md = re.sub(r'#\s+(.+)',r'<h1>\1</h1>', md)
    
    #Negrito
    md = re.sub(r'\*{2}(.+)\*{2}', r'<b>\g<1></b>', md)

    #Itálico
    md = re.sub(r'\*(.*)\*', '<i>\g<1></i>', md)

    #Blockquote
    md = re.sub(r'^>\s(.*?)$', r'<blockquote>\1</blockquote>', md)

    # Lista numerada
    md = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', md)
    md = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>\n', md)

    # Lista não numerada
    md = re.sub(r'(-\s+.*\n?)+', r'<ul>\g<0></ul>', md)
    md = re.sub(r'-\s+(.*)', r'<li>\1</li>\n', md)

    #Código
    md = re.sub(r'`(.+?)`', r'<code>\1</code>', md)

    # Linha horizontal
    md = re.sub(r'---', r'<hr>', md)

    # Imagem
    md = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md)
    
    #Hiperligação
    md = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md)

    return md

def main():
    md_text = sys.stdin.read()
    html_text = mdtohtml(md_text)
    with open('convertido.html','w') as file:
        file.write(html_text)

if __name__ == '__main__':
    main()