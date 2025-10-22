import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL", "supabase project url")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "supabase project key")
SUPABASE_BUCKET: str = os.getenv("SUPABASE_BUCKET", "supabase storage bucket name")

if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_BUCKET]):
    raise EnvironmentError("Supabase configuration is incomplete. Please set SUPABASE_URL, SUPABASE_KEY, and SUPABASE_BUCKET environment variables.")

## Initializing Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

