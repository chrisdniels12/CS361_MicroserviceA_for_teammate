import requests

character_name = "Iron Man"
response = requests.get(f"http://localhost:5000/popularity?characterName={character_name}")

if response.status_code == 200:
    data = response.json()
    print(f"{data['character']} ranks #{data['rank']} with a score of {data['popularityScore']}.")
else:
    print("Error:", response.json()["error"])
