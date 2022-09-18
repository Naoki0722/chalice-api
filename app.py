from chalice.app import Chalice
from chalice.app import BadRequestError
from chalicelib.articles.app import articles_app

app = Chalice(app_name="sample-app")
app.register_blueprint(articles_app)


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/hello/{name}")
def hello_name(name):
    return {"hello": name}


@app.route("/users", methods=["POST"])
def create_user():
    if app.current_request is not None:
        user_as_json = app.current_request.json_body
        return {"user": user_as_json}
    raise BadRequestError("paramater not found")


# Exception Example
@app.route("/badrequest")
def badrequest():
    raise BadRequestError("This is a bad request")
