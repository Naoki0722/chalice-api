from chalice.app import NotFoundError
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
