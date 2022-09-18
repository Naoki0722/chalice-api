from chalice.app import Chalice
from chalice.app import Blueprint
articles_app = Blueprint(__name__)


@articles_app.route('/articles/{id}', methods=['GET'])
def getArticles(id):
    # ～
    # Something Code
    # ～～～
    return {'articles': f'記事情報 : {id}' }

