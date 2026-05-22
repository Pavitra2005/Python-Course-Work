
products={
    'salt':{'stock':20,'Discount':20,'price':60},
    'sugar':{'stock':0,'Discount':12,'price':70},
    'chilli':{'stock':10,'Discount':0,'price':50},
    'bread':{'stock':22,'Discount':15,'price':40},
    'butter':{'stock':11,'Discount':10,'price':80},
    'honey':{'stock':0,'Discount':50,'price':160}
}
    
for i in products:
    print(i,products[i]['price']-(products[i]['price']*(products[i]['Discount']/100)))



