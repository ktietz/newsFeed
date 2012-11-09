db = DAL("sqlite://storage.sqlite")
db.define_table('newsItem', Field('title', unique=True), Field('body', 'text'), format = '%(title)s')

db.newsItem.title.requires = IS_NOT_IN_DB(db, db.newsItem.title)

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables()

from gluon.tools import Crud
crud = Crud(db)