#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

#Database for stored images
db.define_table('images',
                Field('picture', 'upload', uploadfield = 'picture_file'),
                Field('picture_file', 'blob')
                )
COLLEGES = ('College 10', 'College 9', 'Kresge',
            'Porter', 'Crown', 'Merill', 'Stevenson'
            'Cowell', 'Oakes', 'College 8')
db.auth_user.College.requires = IS_IN_SET(COLLEGES)
