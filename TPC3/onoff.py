import re
import sys

def onoff(text):
    soma = 0
    resultado = re.findall(r"([+-]?\d+)|(on|off)|(\=)", text, re.IGNORECASE)
    matches = []
    for match in resultado:
        for element in match:
            if element != '':
                matches.append(element)

    for item in matches:
        if item == '=':
            print(soma)
        else:
            if item.isdigit():
                soma += int(item)
    return soma

def main():
    input_text = sys.stdin.read()
    print(onoff(input_text))

if __name__ == '__main__':
    main()
