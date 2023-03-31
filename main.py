class company:
    def __init__(self, name, capacity=1, client=[]):
        self.name = name
        self.capacity = capacity
        self.client = client

class client:
    def __init__(self, name, company=[]):
        self.name = name
        self.company = company

def max_position(v,index,companies):
    max=v[0]
    for i in range(1,len(v)):
        if companies[index].client.index(v[i])>companies[index].client.index(max):
            max=v[i]
    return companies[index].client.index(max), v.index(max)


# charika1=company('Mountain', 1, ['Pat', 'Anna','Jamie','Rahim','Sam'])
# charika2=company('Bayview', 1, ['Anna', 'Jamie','Rahim','Pat','Sam'])
# charika3=company('Hillside', 2, ['Pat', 'Rahim','Anna','Jamie'])
# charika4=company('Main', 1, ['Anna', 'Rahim','Sam','Jamie','Pat'])

# name1=client('Anna',['Mountain', 'Bayview','Hillside','Main'])
# name2=client('Jamie',['Bayview', 'Mountain','Hillside','Main'])
# name3=client('Pat',['Mountain', 'Main','Hillside'])
# name4=client('Rahim',['Bayview', 'Main'])
# name5=client('Sam',['Main', 'Bayview','Hillside'])









