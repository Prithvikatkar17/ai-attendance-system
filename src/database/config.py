import streamlit as st
from supabase import create_client, Client

url = st.secrets.get("SUPABASE_URL", "NOT_FOUND").strip().strip('"').strip("'")
key = st.secrets.get("SUPABASE_KEY", "NOT_FOUND").strip().strip('"').strip("'")

if url == "NOT_FOUND" or key == "NOT_FOUND":
    st.error("🚨 SUPABASE SECRETS ARE MISSING IN STREAMLIT CLOUD!")
else:
    st.success(f"✅ Secrets loaded! URL starts with: {url[:10]}... and length is {len(url)}")

try:
    supabase : Client = create_client(url, key)
except Exception as e:
    st.error(f"Failed to create Supabase client: {e}")