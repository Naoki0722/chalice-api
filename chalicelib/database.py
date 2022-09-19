import os
import boto3
from boto3.resources.base import ServiceResource


class DBDataCheckException(Exception):
    pass


def _get_database() -> ServiceResource:
    """
    DB接続関数

    Returns:
        ServiceResource: dynamoDBリソース
    """
    endpoint = os.environ.get("DB_ENDPOINT")
    if endpoint:
        print("DB接続")
        print(endpoint)
        return boto3.resource("dynamodb", endpoint_url=endpoint)
    else:
        print("DB接続エンドポイント指定なし")
        return boto3.resource("dynamodb")


def get_record(record_id):
    table = _get_database().Table(os.environ["DB_TABLE_NAME"])
    response = table.get_item(Key={"id": record_id})
    return response["Item"]


def post_record(item):
    table = _get_database().Table(os.environ["DB_TABLE_NAME"])
    table_data = table.get_item(Key={"id": item["id"]})
    if "Item" in table_data:
        raise DBDataCheckException("既にデータがあります")
    put_data = table.put_item(Item=item)
    if put_data:
        put_data["ResponseMetadata"]["message"] = "success create!"
        return put_data["ResponseMetadata"]


def delete_record(record_id):
    table = _get_database().Table(os.environ["DB_TABLE_NAME"])
    table_data = table.get_item(Key={"id": record_id})
    if "Item" not in table_data:
        raise DBDataCheckException("データがないため、削除できません")
    delete_data = table.delete_item(
        TableName=os.environ["DB_TABLE_NAME"], Key={"id": record_id}
    )
    if delete_data:
        delete_data["ResponseMetadata"]["message"] = "success delete!"
    return delete_data["ResponseMetadata"]
