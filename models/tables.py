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
from datetime import datetime


#Database for stored images
db.define_table('images',
                Field('picture', 'upload', uploadfield = 'picture_file'),
                Field('picture_file', 'blob')
                )
COLLEGES = ('College 10', 'College 9', 'Kresge',
            'Porter', 'Crown', 'Merill', 'Stevenson',
            'Cowell', 'Oakes', 'College 8')

GENDER = ('Male', 'Female')


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

CATEGORY = ['Books', 'Music', 'Outdoors', 'For the House', 'Misc.']
SOLD = ['Sold', 'Still Available']


db.define_table('bboard',
                Field('name'),
                Field('user_id', db.auth_user),
                Field('phone'),
                Field('email'),
                Field('category'),
                Field('sold'),
                Field('date_posted', 'datetime'),
                Field('title'),
                Field('price'),
                Field('bbmessage', 'text'),
                Field('image', 'upload')
                )

db.define_table('post',
             Field('author', db.auth_user, default=auth.user_id),
             Field('message_content', 'text'),
             Field('is_draft', 'boolean', default=False),
             Field('message_id'), # To uniquely identify drafts and messages.
            )

db.auth_user.College.requires = IS_IN_SET(COLLEGES)
db.auth_user.Gender.requires = IS_IN_SET(GENDER)
db.bboard.id.readable = False
db.bboard.bbmessage.label = 'Message'
db.bboard.name.default = get_first_name()
db.bboard.date_posted.default = datetime.utcnow()
db.bboard.name.writable = False
db.bboard.date_posted.writable = False
db.bboard.user_id.default = auth.user_id
db.bboard.user_id.writable = db.bboard.user_id.readable = False
db.bboard.email.requires = IS_EMAIL()
db.bboard.category.requires = IS_IN_SET(CATEGORY)
db.bboard.category.default = 'Misc'
db.bboard.category.required = True
db.bboard.sold.requires = IS_IN_SET(SOLD)
db.bboard.sold.default = 'Still Available'
db.bboard.sold.required = True
db.bboard.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.bboard.phone.requires = IS_MATCH('^\d{10}$',
         error_message='not a phone number')

