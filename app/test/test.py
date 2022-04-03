from pdfminer.high_level import extract_text

text = extract_text('teste.pdf')

names = []

value = {}

count = 0
for line in text.split('\n'):
    if count == 9 and len(line) > 1:
        value['prods'][0]['price'] = line

    if count == 8 and len(line) > 1:
        value['prods'][0]['qtd'] = line
        count = 9

    if count == 7 and len(line) > 1:
        if not value['prods'][0].get('var'):
            value['prods'][0]['var'] = []

        value['prods'][0]['var'].append(line)

    if count == 5 and len(line) > 1:
        value['prods'][0]['desc'] = line
        count = 6

    if count == 4 and len(line) > 1:
        n = line.split(' ')
        value['prods'].append({
            'n': n[0],
            'cod': n[1]
        })
        count = 5

    if count == 2 and len(line) > 1:
        value = { 'name': line, 'prods': []}
        names.append(value)
        count = 3

    if line.startswith('QTD'):
        count = 8

    if line.startswith('VARIAÇÃO'):
        count = 7

    if line.startswith('Nº'):
        count = 4

    if (line.startswith('NOME:')):
        count = count > 2 and 1 or 2
   
a = open('teste2.txt', 'w')
for name in names:
    a.write(name['name'] + '\n')
    for prod in name['prods']:
        a.write((prod['n'] or '') + '\t' + (prod.get('code') or '') + '\t' + (prod.get('desc') or '') + '\t' + (prod.get('qtd') or '') + '\t' + (prod.get('price') or '') + '\n')
        for var in prod.get('var') or []:
            a.write(var + '\n')

a.close()