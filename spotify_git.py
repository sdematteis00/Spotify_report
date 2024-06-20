import requests
import base64
import pandas as pd

# Replace these with your own client ID and client secret
client_id = '[your client id]'
client_secret = '[your client secret]'

# Encode the client ID and client secret
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

# Request access token
token_url = "https://accounts.spotify.com/api/token"
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}"
}

response = requests.post(token_url, data=token_data, headers=token_headers)
auth_data = response.json()
access_token = auth_data['access_token']

# Prepare headers for API requests
headers = {'Authorization': f'Bearer {access_token}'}

# Load your existing CSV file into a DataFrame
# Replace with the actual path to your file
df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Create an empty list to store cover URLs and track URLs
cover_urls = []
track_urls = []

# Loop through each row in the DataFrame to search for tracks on Spotify
for _, row in df.iterrows():
    track_name = row['track_name']
    artist_name = row["artist(s)_name"]
    
    # Create a query string
    query = f"track:{track_name} artist:{artist_name}"
    
    # Search for the track on Spotify
    search_response = requests.get(
        f"https://api.spotify.com/v1/search?q={query}&type=track",
        headers=headers
    )
    
    search_data = search_response.json()
    
    try:
        # Extract track URL and album cover URL
        track_info = search_data['tracks']['items'][0]
        track_url = track_info['external_urls']['spotify']
        cover_url = track_info['album']['images'][0]['url']
    except (KeyError, IndexError):
        track_url = 'Not Found'
        cover_url = 'Not Found'
    
    # Append the URLs to the respective lists
    track_urls.append(track_url)
    cover_urls.append(cover_url)

# Add the URLs to the DataFrame
df['track_url'] = track_urls
df['album_cover_url'] = cover_urls

# Save the updated DataFrame back to a CSV file
df.to_csv('spotify-2023-updated.csv', index=False)

print(df)
