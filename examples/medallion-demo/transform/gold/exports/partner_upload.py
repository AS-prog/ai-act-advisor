"""Entrega de Gold a un socio de medios (ficticio)."""
from google.cloud import storage


def upload(local_path: str, bucket_name: str, blob_name: str) -> None:
    client = storage.Client()
    client.bucket(bucket_name).blob(blob_name).upload_from_filename(local_path)
