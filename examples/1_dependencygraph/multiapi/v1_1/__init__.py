import multiorm

orm = multiorm.get('v0.1')

def execute():
    return { 
               'api': 'v1.1', 
               'orm': orm.execute()
           }
