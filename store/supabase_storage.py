# myapp/storage.py

from django.core.files.storage import Storage
from supabase import create_client
import os

class SupabaseStorage(Storage):
    def __init__(self, *args, **kwargs):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_API_KEY")
        self.client = create_client(self.supabase_url, self.supabase_key)
        super().__init__(*args, **kwargs)

    def _save(self, name, content):
        # Upload file to Supabase Storage
        bucket_name = "your_bucket_name"  # Change to your bucket name
        self.client.storage.from_(bucket_name).upload(name, content.read())
        return name

    def url(self, name):
        # Generate a public URL for the file
        bucket_name = ""  # Change to your bucket name
        return self.client.storage.from_(bucket_name).get_public_url(name)["publicURL"]