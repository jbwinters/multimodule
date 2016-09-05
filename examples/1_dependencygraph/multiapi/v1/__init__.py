import multiorm

orm = multiorm.get('v0')

def execute():
    return { 
               'api': 'v1', 
               'orm': orm.execute()
           }
