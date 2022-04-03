from pdfminer.high_level import extract_text

text = extract_text('teste.pdf')

names = []

value = {}

step = 0
count = 0
for line in text.split('\n'):
    if step == 9 and len(line) > 0:
        value['prods'][count]['price'] = line
        step += 1
        count += 1

    if step == 8 and len(line) > 0:
        value['prods'][count]['qtd'] = line
        step = 9

    if step == 7 and len(line) > 0 and not line.startswith('QTD'):
        if not value['prods'][0].get('var'):
            value['prods'][count]['var'] = []

        value['prods'][count]['var'].append(line)

    if step == 5 and len(line) > 0:
        value['prods'][count]['desc'] = line
        step = 6

    if step == 4 and len(line) > 0:
        n = line.split(' ')
        value['prods'].append({
            'n': n[0],
            'cod': n[1]
        })
        step = 5

    if step == 2 and len(line) > 0:
        value = { 'name': line, 'prods': []}
        names.append(value)
        step = 3

    if line.startswith('QTD'):
        step = 8

    if line.startswith('VARIAÇÃO'):
        step = 7

    if line.startswith('Nº'):
        step = 4

    if (line.startswith('NOME:')):
        step = step > 2 and 1 or 2
        count = 0
   
a = open('teste2.txt', 'w')
for name in names:
    a.write(name['name'] + '\n')
    for prod in name['prods']:
        a.write((prod['n'] or '') + '\t' + (prod.get('code') or '') + '\t' + (prod.get('desc') or '') + '\t' + (prod.get('qtd') or '') + '\t' + (prod.get('price') or '') + '\n')
        for var in prod.get('var') or []:
            a.write(var + '\n')

a.close()