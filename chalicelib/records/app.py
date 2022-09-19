import traceback
from chalice.app import NotFoundError, BadRequestError
from chalice.app import Blueprint
from chalicelib import database


db_record = Blueprint(__name__)


@db_record.route("/records/{record_id}", methods=["GET"], cors=True)
def get_records(record_id):
    record = database.get_record(record_id)
    if record:
        return record
    else:
        raise NotFoundError("record not found")


@db_record.route("/records", methods=["POST"], cors=True)
def post_record():
    try:
        return database.post_record(db_record.current_request.json_body)
    except database.MyError as e:
        print(traceback.format_exc())
        print(f"DB登録エラー!詳細 : {e}")
        raise BadRequestError("This is a bad request")
    except Exception as e:
        print(traceback.format_exc())
        print(f"DB登録エラー!詳細 : {e}")
        raise BadRequestError("This is a bad request")


@db_record.route("/records/{record_id}", methods=["DELETE"], cors=True)
def delete_record(record_id):
    try:
        return database.delete_record(record_id)
    except database.MyError as e:
        print(traceback.format_exc())
        print(f"DB登録エラー!詳細 : {e}")
        raise BadRequestError("This is a bad request")
    except Exception as e:
        print(traceback.format_exc())
        print(f"DB登録エラー!詳細 : {e}")
        raise BadRequestError("This is a bad request")
