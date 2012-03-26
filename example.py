import jsonshelve

db = jsonshelve.FlatShelf('foo.db')
with db:
    db['key'] = 'value'
    print('key' in db)
    print('anotherkey' in db)
db.close()

db = jsonshelve.FlatShelf('foo.db')
with db:
    print(db['key'])
