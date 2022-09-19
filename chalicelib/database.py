import os
import boto3

from boto3.resources.base import ServiceResource


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
    table = _get_database().Table("Records")
    response = table.get_item(Key={"id": record_id})
    return response["Item"]
