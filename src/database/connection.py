from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
api_key = os.getenv("SUPABASE_API_KEY")

# Crea la conexión a Supabase
supabase: Client = create_client(url, api_key)
