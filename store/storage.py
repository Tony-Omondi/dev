from django.core.files.storage import Storage
from supabase import create_client
import os

class SupabaseStorage(Storage):
    def __init__(self, *args, **kwargs):
        # Use environment variables for sensitive data in production
        self.supabase_url = "https://jxegrzviztasnwbzxzqa.supabase.co"
        self.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp4ZWdyenZpenRhc253Ynp4enFhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMDQxOTYzNCwiZXhwIjoyMDQ1OTk1NjM0fQ.78xvfqGIincye-31VOZ3fzOvjTvy4N7lpI_xWORugNA"
        self.client = create_client(self.supabase_url, self.supabase_key)
        super().__init__(*args, **kwargs)

    def _save(self, name, content):
        # Upload file to Supabase Storage
        bucket_name = "product-images"  # Ensure this is the correct bucket name
        self.client.storage.from_(bucket_name).upload(name, content.read())
        return name

    def url(self, name):
        # Generate a public URL for the file
        bucket_name = "product-images"  # Ensure this is the correct bucket name
        public_url = self.client.storage.from_(bucket_name).get_public_url(name)
        
        if isinstance(public_url, str):
            return public_url
        else:
            raise Exception(f"Unexpected response when getting public URL: {public_url}")

    def exists(self, name):
        # Check if a file exists in Supabase Storage
        bucket_name = "product-images"  # Ensure this is the correct bucket name
        response = self.client.storage.from_(bucket_name).list()

        # Check if the response is a list and if the requested file exists
        return any(item['name'] == name for item in response)
