from supabase import create_client, Client
from dotenv import load_dotenv
import os
from cars_demo.data import cars_db

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL", "supabase project url")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "supabase project key")

supabase : Client = create_client(SUPABASE_URL, SUPABASE_KEY)

results = supabase.table("cars-demo").select("*").execute()

# for car in cars_db:
#     if not any(d['id'] == car['id'] for d in results.data):
#         try:
#             supabase.table("cars-demo").insert(car).execute()
#             print(f"Inserted car with id: {car['id']}")
#         except Exception as e:
#             print(f"Error inserting car with id: {car['id']}. Error: {e}")
#     else:
#         print(f"Car with id: {car['id']} already exists")

## Updating a record
new_car = {"id":"3", "created_at":"2025-10-01 13:15:05+00", "make":"chevrolet", "model": "chevelle malibu", "city": "Toronto"}
supabase.table("cars-demo").update(new_car).eq("city", "Ottawa").execute()

## Deleting a record
# supabase.table("cars-demo").delete().eq("id", 2).execute()

response = supabase.storage().from_("cars-demo").get_public_url("tesla.png")
