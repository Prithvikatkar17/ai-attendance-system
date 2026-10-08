import streamlit as st
from supabase import create_client, Client

url = st.secrets.get("SUPABASE_URL", "NOT_FOUND").strip().strip('"').strip("'")
key = st.secrets.get("SUPABASE_KEY", "NOT_FOUND").strip().strip('"').strip("'")

if url == "NOT_FOUND" or key == "NOT_FOUND":
    st.error("🚨 SUPABASE SECRETS ARE MISSING IN STREAMLIT CLOUD!")
else:
    st.success(f"✅ Secrets loaded! URL starts with: {url[:10]}... and length is {len(url)}")

try:
    import requests
    res = requests.get(f"{url}/rest/v1/", headers={"apikey": key})
    if res.status_code == 401 or res.status_code == 200:
        st.success(f"✅ `requests` successfully connected to Supabase! (Status: {res.status_code})")
    else:
        st.warning(f"⚠️ `requests` reached Supabase but got status: {res.status_code}")
except Exception as e:
    st.error(f"🚨 `requests` ALSO failed to connect: {e}")

try:
    supabase : Client = create_client(url, key)
    # Test a quick query to see if it works during boot
    test_res = supabase.table('students').select("id").limit(1).execute()
except Exception as e:
    st.error(f"Failed to create Supabase client or run query: {e}")