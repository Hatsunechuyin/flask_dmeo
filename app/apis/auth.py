from sqlalchemy.testing import db

from app.apis import apis
from app.extension import db

@apis.route(
    'test',
    methods=['GET'],
    endpoint='test'
)
def test():
    return 'test'


class Article(db.Model):
    __tablename__ = 'article'  # 如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


@apis.route(
    'index',
    methods=['GET'],
    endpoint='index'
)
def index():
    article1 = Article(title=u'aaa', content=u'bbb')
    print(article1)
    db.session.add(article1)
    db.session.commit()
    return 'test'