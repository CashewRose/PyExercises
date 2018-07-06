stockDict = { 
    'GE': 'General Motors',
    'CAT':'Caterpillar', 
    'EK':"Eastman Kodak" 
}

purchases = [ 
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'EK', 375, '24-mar-2007', 10 ),
    ( 'GE', 200, '1-jul-1998', 56 ) 
]

combine_sameStock = {}

def purchase_summary():
    for purchase in purchases:
        if purchase[0] in combine_sameStock:
            combine_sameStock[purchase[0]].append(purchase[1:])
        else:
            combine_sameStock.update({purchase[0]:[purchase[1:]]})
           
def purchase_report():
    for purchase in purchases:
        full_purchase_price = purchase[1] * purchase[3]
        for key,value in stockDict.items():
            if purchase[0] == key:
                print(f'The total purchase price for our shares in {value} on {purchase[2]} was ${full_purchase_price}.')

purchase_report()
purchase_summary()
print(combine_sameStock)