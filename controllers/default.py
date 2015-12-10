# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    #Testing123
    #Need to add something to store search variable in here
    if auth.user is None:
        my_username = ''
    else:
        my_username = auth.user.username
    form = SQLFORM.factory(
                   Field("username"),
                   formstyle='divs',
                   submit_button="Search"
    )
    if form.process().accepted:
        #Data from SQLFORM
        username = form.vars.username
        #conditions
        if username:
            redirect(URL('default', 'user_profile', args=[username]))
    return dict(form=form, my_username=my_username)

def submit_a_listing():
    if auth.user is None:
        my_username = ''
    else:
        my_username = auth.user.username
    form = SQLFORM(db.bboard)
    if form.process().accepted:
        # Successful processing.
        session.flash = T("inserted")
        redirect(URL('default', 'index'))
    return dict(my_username=my_username, form=form)

def view_listing():
    if auth.user is None:
        my_username = ''
    else:
        my_username = auth.user.username

    q = db.bboard

    def generate_del_button(row):
        # If the record is ours, we can delete it.
        b = ''
        if auth.user_id == row.user_id:
            b = A('Delete', _class='btn', _href=URL('default', 'delete', args=[row.id]))
        return b

    def generate_edit_button(row):
        # If the record is ours, we can delete it.
        b = ''
        if auth.user_id == row.user_id:
            b = A('Edit', _class='btn', _href=URL('default', 'edit', args=[row.id]))
        return b

    def shorten_post(row):
        return row.bbmessage[:10] + '...'

    # Creates extra buttons.

    links = [
        dict(header='', body = generate_del_button),
        dict(header='', body = generate_edit_button),
        ]

    if len(request.args) == 0:
        # We are in the main index.
        links.append(dict(header='Post', body = shorten_post))
        db.bboard.bbmessage.readable = False

    form = SQLFORM.grid(q,
        fields=[db.bboard.user_id, db.bboard.date_posted,
                db.bboard.category, db.bboard.title,
                db.bboard.bbmessage],
        editable=False, deletable=False,
        links=links,
        paginate=5,
        )
    return dict(my_username=my_username,form=form)

def search():
    if auth.user is None:
        my_username = ''
    else:
        my_username = auth.user.username
    form = SQLFORM.factory(
                   Field("username"),
                   formstyle='divs',
                   submit_button="Search"
    )
    if form.process().accepted:
        #Data from SQLFORM
        username = form.vars.username
        #conditions
        if username:
            redirect(URL('default', 'profile', args=[username]))
    return dict(form=form, my_username=my_username)



def profile():

    if auth.user is None:
        my_username = ''
    else:
        my_username = auth.user.username
    user_name = request.args(0)
    #Note: Profile Details
    my_first = db(db.auth_user.username == user_name).select(db.auth_user.first_name)
    my_last = db(db.auth_user.username == user_name).select(db.auth_user.last_name)
    my_college = db(db.auth_user.username == user_name).select(db.auth_user.College)
    my_major = db(db.auth_user.username == user_name).select(db.auth_user.Major)
    my_gender = db(db.auth_user.username == user_name).select(db.auth_user.Gender)
    ##############################


    user_images = db(db.auth_user.username == user_name).select()
    for row in db().select(db.auth_user.ALL):
        if row.username == user_name:
            print "Name found"
            found = 1
            break
        else:
            print "No username found"
            found = 0
    if found == 1:
        print "print out form"
    else:
        print "no username founded, print out no such username try again"


    return dict(user_name=user_name, user_images=user_images, my_username=my_username,
                my_first=my_first, my_last=my_last, my_college=my_college, my_major=my_major,
                my_gender=my_gender)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args(0) == 'profile':
        db.auth_user.username.readable = db.auth_user.username.writable = False
        db.auth_user.email.readable = db.auth_user.email.writable = False
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


