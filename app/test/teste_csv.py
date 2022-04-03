import openpyxl
from pprint import pprint

a = openpyxl.load_workbook('teste.xlsx')
sheet = a.active

data = {}

for i, row in enumerate(sheet.iter_rows(values_only=True)):
    if i == 0:
        data['track_id'] = []
        data['item_id'] = []
        data['item_info'] = []
        data['client_obs'] = []
        data['note'] = []

    else:
        data['track_id'].append(row[0])
        data['item_id'].append(row[1])
        data['item_info'].append(row[2])
        data['client_obs'].append(row[3])
        data['note'].append(row[4])

track_list = []
for id in range(len(data['track_id'])):
    track_list.append({
        'track_id': data['track_id'][id],
        'item_id': data['item_id'][id],
        'item_info': data['item_info'][id],
        'client_obs': data['client_obs'][id],
        'note': data['note'][id]
    })

for track in track_list:
    prod_list = ''.join(track['item_info']).split('\r\n') or []
    item_list = []
    track['item_list'] = item_list
    for prod in prod_list:
        if not prod:
            continue
        item = {
            'id': '',
            'name': '',
            'variation': '',
            'amount': '',
            'price': '',
            'sku': '',
            'sku_main': ''
        }
        index = prod.find(']')
        item['id'] = prod[1:index]
        for item_info in prod[index + 1:].split(';'):
            item_info = item_info.strip().split(':')
            if len(item_info) > 1:
                label = item_info[0].strip().lower()
                value = item_info[1].strip()
                if label.startswith('nome do produto'):
                    item['name'] = value

                elif label.startswith('nome da variação'):
                    item['variation'] = value

                elif label.startswith('quantidade'):
                    item['amount'] = value

                elif label.startswith('preço'):
                    item['price'] = value

                elif label.startswith('número de referência sku'):
                    item['sku'] = value

                elif label.startswith('nº de referência do sku principal'):
                    item['sku_main'] = value

        item_list.append(item)

item_map = {}

with open('teste.csv', 'w') as f:
    for track in track_list:
        f.write('Número de rastreamento;ID do pedido;Observação do comprador;Nota\n')
        f.write('{data[track_id]};{data[item_id]};{data[client_obs]};{data[note]}\n'.format(data=track))

        f.write(';;;;ID;Nome do produto;Variação;SKU;SKU Principal;Quantidade;Preço\n')
        for item in track['item_list']:
            f.write(';;;;{data[id]};{data[name]};{data[variation]};{data[sku]};{data[sku_main]};{data[amount]};{data[price]}\n'.format(data=item))

            item_var_map = item_map.get(item['name'])
            if not item_var_map:
                item_map[item['name']] = {}
                item_var_map = item_map[item['name']]

            var_list = item_var_map.get(item['variation'])
            if not var_list:
                item_var_map[item['variation']] = []
                var_list = item_var_map[item['variation']]

            var_list.append(item)

        f.write('\n')
    
    f.write(';;;;;;;;;;;;Nome do produto;SKU;Variação;Quantidade;Preço\n')
    for name, item_var_map in item_map.items():
        for var, item_list in item_var_map.items():
            amount = 0
            price = ''
            sku = ''
            for item in item_list:
                amount += float(item['amount'] or '0') or 0
                price = item['price']
                sku = item['sku']
            
            amount = ('%f'% amount).replace('.', ',')
            f.write((';;;;;;;;;;;;%s;%s;%s;%s;%s\n')%(name, sku, var, amount, price))
    

        