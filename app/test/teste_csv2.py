import openpyxl
from pprint import pprint

''' 
    type, key, description
'''

ORDER_TYPE = 'order_type'
ITEM_TYPE = 'item_type'

xls_layout = [
    (ORDER_TYPE,   'order_id'),
    (ORDER_TYPE,   'order_status'),
    (ORDER_TYPE,   'order_return_status'),
    (ORDER_TYPE,   'tracking_number'),
    (ORDER_TYPE,   'shipping_option'),
    (ORDER_TYPE,   'shipping_method'),
    (ORDER_TYPE,   'shipping_planned_date'),
    (ORDER_TYPE,   'shipping_time'),
    (ORDER_TYPE,   'shipping_creation_date'),
    (ORDER_TYPE,   'shipping_pay_date_time'),
    (ITEM_TYPE,    'item_sku_main'),
    (ITEM_TYPE,    'item_name'),
    (ITEM_TYPE,    'item_sku_number'),
    (ITEM_TYPE,    'item_variation_name'),
    (ITEM_TYPE,    'item_price_original'),
    (ITEM_TYPE,    'item_price_agreed'),
    (ITEM_TYPE,    'item_amount'),
    (ITEM_TYPE,    'item_subtotal'),
    (ITEM_TYPE,    'item_discount'),
    (ITEM_TYPE,    'item_discount2'),
    (ITEM_TYPE,    'item_shopee_refund'),
    (ITEM_TYPE,    'item_sku_weight'),
    (ORDER_TYPE,   'order_item_amount'),
    (ORDER_TYPE,   'order_weight'),
    (ORDER_TYPE,   'order_coupon_code'),
    (ORDER_TYPE,   'order_coupon_seller'),
    (ORDER_TYPE,   'order_seller_cashback'),
    (ORDER_TYPE,   'order_cupom_shopee'),
    (ORDER_TYPE,   'order_more_for_less_flag'),
    (ORDER_TYPE,   'order_more_for_less_discount_shopee'),
    (ORDER_TYPE,   'order_more_for_less_discount_seller'),
    (ORDER_TYPE,   'order_shopee_compensate_coins'),
    (ORDER_TYPE,   'order_cred_card_discount'),
    (ORDER_TYPE,   'order_total'),
    (ORDER_TYPE,   'shipping_tax'),
    (ORDER_TYPE,   'shipping_tax_discount'),
    (ORDER_TYPE,   'shipping_reverse_tax'),
    (ORDER_TYPE,   'shipping_transaction_tax'),
    (ORDER_TYPE,   'commission_tax'),
    (ORDER_TYPE,   'service_tax'),
    (ORDER_TYPE,   'global_tax'),
    (ORDER_TYPE,   'shipping_tax_estimated'),
    (ORDER_TYPE,   'customer_name'),
    (ORDER_TYPE,   'receiver_name'),
    (ORDER_TYPE,   'customer_phone'),
    (ORDER_TYPE,   'customer_document'),
    (ORDER_TYPE,   'receiver_address'),
    (ORDER_TYPE,   'receiver_city_old'),
    (ORDER_TYPE,   'receiver_district'),
    (ORDER_TYPE,   'receiver_city'),
    (ORDER_TYPE,   'receiver_state'),
    (ORDER_TYPE,   'receiver_country'),
    (ORDER_TYPE,   'receiver_zip_code'),
    (ORDER_TYPE,   'customer_obs'),
    (ORDER_TYPE,   'order_time'),
    (ORDER_TYPE,   'order_invoice'),
]

order_layout = [
    [
        ('order_id',                             'ID do pedido'),
        ('order_status',                         'Status do pedido'),
        ('shipping_creation_date',               'Data de criação do pedido'),
        ('shipping_pay_date_time',               'Hora do pagamento do pedido'),
        ('order_total',                          'Valor Total'),
        ('order_coupon_code',                    'Código do Cupom'),
        ('order_time',                           'Hora completa do pedido'),
        ('order_invoice',                        'Nota'),
        ('order_item_amount',                    'Número de produtos pedidos'),
        ('order_weight',                         'Peso total do pedido'),
    ],
    [
        ('tracking_number',                      'Número de rastreamento'),
        ('order_return_status',                  'Status da Devolução / Reembolso'),  
        ('shipping_option',                      'Opção de envio'),
        ('shipping_method',                      'Método de envio'),
        ('shipping_planned_date',                'Data prevista de envio'),
        ('shipping_time',                        'Tempo de Envio'),
    ],
    [
        ('shipping_tax',                         'Taxa de envio pagas pelo comprador'),
        ('shipping_tax_discount',                'Desconto de Frete Aproximado'),
        ('shipping_reverse_tax',                 'Taxa de Envio Reversa'),
        ('shipping_transaction_tax',             'Taxa de transação'),
        ('commission_tax',                       'Taxa de comissão'),
        ('service_tax',                          'Taxa de serviço'),
        ('global_tax',                           'Total global'),
        ('shipping_tax_estimated',               'Valor estimado do frete'),
    ],
    [
        ('order_coupon_seller',                  'Cupom do vendedor'),
        ('order_seller_cashback',                'Seller Absorbed Coin Cashback'),
        ('order_cupom_shopee',                   'Cupom Shopee'),
        ('order_more_for_less_flag',             'Indicador da Leve Mais por Menos'),
        ('order_more_for_less_discount_shopee',  'Desconto Shopee da Leve Mais por Menos'),
        ('order_more_for_less_discount_seller',  'Desconto da Leve Mais por Menos do vendedor'),
        ('order_shopee_compensate_coins',        'Compensar Moedas Shopee'),
        ('order_cred_card_discount',             'Total descontado Cartão de Crédito'),
    ],
    [
        ('customer_name',                        'Nome de usuário (comprador)'),
        ('receiver_name',                        'Nome do destinatário'),
        ('customer_phone',                       'Telefone'),
        ('customer_document',                    'CPF do Comprador'),
        ('receiver_address',                     'Endereço de entrega'),
        ('receiver_city',                        'Cidade'),
        ('receiver_district',                    'Bairro'),
        ('receiver_state',                       'UF'),
        ('receiver_country',                     'País'),
        ('receiver_zip_code',                    'CEP'),
    ],
    [
        ('customer_obs',                         'Observação do comprador'),
    ]
]

item_layout = [
    ('item_sku_main',        'Nº de referência do SKU principal'),
    ('item_sku_number',      'Número de referência SKU'),
    ('item_name',            'Nome do Produto'),
    ('item_variation_name',  'Nome da variação'),
    ('item_sku_weight',      'Peso total SKU'),
    ('item_shopee_refund',   'Reembolso Shopee'),
    ('item_amount',          'Quantidade'),
    ('item_discount',        'Desconto do vendedor'),
    ('item_discount2',       'Desconto do vendedor'),
    ('item_price_original',  'Preço original'),
    ('item_price_agreed',    'Preço acordado'),  
    ('item_subtotal',        'Subtotal do produto'),
]

variation_layout = [
    ('item_sku_main',        'Nº de referência do SKU principal'),
    ('item_sku_number',      'Número de referência SKU'),
    ('item_name',            'Nome do Produto'),
    ('item_variation_name',  'Nome da variação'),
    ('item_sku_weight',      'Peso total SKU'),
    ('item_amount',          'Quantidade'),
]

'''
    xls_Read xl file, create data according to layout
'''
a = openpyxl.load_workbook('teste2.xlsx')
sheet = a.active

data_sheet = {}

for i, row in enumerate(sheet.iter_rows(values_only=True)):
    if i == 0:
        for type, key in xls_layout:
            data_sheet[key] = []

    else:
        for rowIndex in range(len(xls_layout)):
            type, key = xls_layout[rowIndex]
            data_sheet[key].append(row[rowIndex])

'''
    Mapping by order_id
'''

data_map = {}
for id in range(len(data_sheet['order_id'])):
    data_list = data_map.get(data_sheet['order_id'][id])
    if not data_list:
        data_map[data_sheet['order_id'][id]] = []
        data_list = data_map[data_sheet['order_id'][id]]

    order_dict = {}
    for type, key in xls_layout:
        order_dict[key] = data_sheet[key][id]
    
    data_list.append(order_dict)

'''
    Create order_list by mapping
'''

order_list = []
for data_list in data_map.values():
    order_dict = { 'item_list': [] }

    for data in data_list:
        item_dict = {}
        for type, key in xls_layout:
            if type == ORDER_TYPE:
                order_dict[key] = data[key]

            if type == ITEM_TYPE:
                item_dict[key] = data[key]

        order_dict['item_list'].append(item_dict)

    order_list.append(order_dict)

item_map = {}

max_order_line = 0
max_item_line = 0

with open('teste2.csv', 'w') as f:
    for order_dict in order_list:
        
        for line_layout in order_layout:
            if len(line_layout) > max_order_line:
                max_order_line = len(line_layout)

            f.write(';'.join([label for key, label in line_layout]) + '\n')
            f.write(';'.join([str(order_dict.get(key)) for key, label in line_layout]) + '\n')

        f.write('\n')
        f.write((';' * max_order_line) + ';'.join([label for key, label in item_layout]) + '\n')
        for item_dict in order_dict['item_list']:
            if len(item_layout) > max_item_line:
                max_item_line = len(item_layout)

            f.write((';' * max_order_line) + ';'.join([str(item_dict[key]) for key, label in item_layout]) + '\n')

            item_var_map = item_map.get(item_dict['item_name'])
            if not item_var_map:
                item_map[item_dict['item_name']] = {}
                item_var_map = item_map[item_dict['item_name']]

            var_list = item_var_map.get(item_dict['item_variation_name'])
            if not var_list:
                item_var_map[item_dict['item_variation_name']] = []
                var_list = item_var_map[item_dict['item_variation_name']]

            var_list.append(item_dict)

        f.write('\n')

    f.write('\n')
    f.write((';' * (max_order_line + max_order_line)) + ';;' + ';'.join([label for key, label in variation_layout]) + '\n')

    for name, item_var_map in item_map.items():
        for var, item_list in item_var_map.items():
            variation_dict = {}
            amount = 0
            for item_dict in item_list:
                variation_dict = item_dict
                amount += float(item_dict['item_amount'] or '0') or 0

            amount = ('%f'% amount).replace('.', ',')
            variation_dict['item_amount'] = amount

            f.write((';' * (max_order_line + max_order_line)) + ';;' +';'.join([str(variation_dict[key]) for key, label in variation_layout]) + '\n')
    