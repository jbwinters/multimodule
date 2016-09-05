import multiorm

orm = multiorm.get('v0')

def execute():
    return { 
               'api': 'v0', 
               'orm': orm.execute()
           }
