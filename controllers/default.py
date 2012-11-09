def user():
        return dict(form=auth())

def index():
    newsItems = db().select(db.newsItem.ALL, orderby=db.newsItem.title)
    return dict(newsItems=newsItems)

def show():
    newsItems = db.newsItem(request.args(0)) or redirect(URL('index'))
    newsItemForm = crud.create(db.newsItem, message="Your News Item is posted", next=URL(args=newsItems.id))
    return dict(newsItems=newsItems, comments=comments, form=form, newsItemForm=newsItemForm)

def download():
    return response.download(request, db)

#@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.smartgrid(db.newsItem)
    #newsItem = db.newsItem(request.args(0)) or redirect(URL('manage'))
    newsItemForm = crud.create(db.newsItem, message="Your news item is posted")
    return dict(newsItemForm=newsItemForm, grid=grid)