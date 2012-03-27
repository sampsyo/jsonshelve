import jsonshelve

for cls in (jsonshelve.FlatShelf, jsonshelve.PickleShelf,
            jsonshelve.SQLiteShelf):
    filename = 'test_{}.db'.format(cls.__name__)
    print(filename)

    db = cls(filename)
    with db:
        print('key' in db)
        db['key'] = 'value'
        print('key' in db)
    db.close()

    db = cls(filename)
    with db:
        print(db['key'])
        db['anotherkey'] = {'foo': 'bar'}
        print(dict(db))
    db.close()
