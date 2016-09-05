import multiorm

orm = multiorm.get('v1')

def execute():
    return { 
               'api': 'v2', 
               'orm': orm.execute()
           }
