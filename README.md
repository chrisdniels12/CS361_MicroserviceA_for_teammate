# COMMUNICATION CONTRACT for CS 361 MICROSERVICE A for TEAMMATE

A. How to programmatically REQUEST data from the microservice you implemented. 
To request data I used the HTTP Method: GET
with this endpoint:
**http://localhost:5000/popularity?characterName=<CharacterName>**

Note: the queery has specific parameters: 
characterName is a string, It must have an exact name of the Marvel character as seen in the dictionary, this is case sensitive.

**Example call:**
import requests

character = "Spider-Man"
response = requests.get(f"http://localhost:5000/popularity?characterName={character}")

B.how to programmatically RECEIVE data from the microservice you implemented.
Response format: JSON
Example JSON response:
{
  "character": "Spider-Man",
  "popularityScore": 98,
  "rank": 1
}

example code to receive and use the data in python:
data = response.json()
print(f"{data['character']} ranks #{data['rank']} with a popularity score of {data['popularityScore']}")

C. UML Sequence Diagram
![UML](https://github.com/user-attachments/assets/b0a17fb4-3594-46da-b00b-037873b5343e)

**4. The MITIGATION PLAN**
A. For which teammate did you implement “Microservice A”?
- I implemented this microservice for Edward

B. What is the current status of the microservice? Hopefully, it’s done!
- The microservice is fully implemented, tested, and working as expected.

C. If the microservice isn’t done, which parts aren’t done and when will they be done?
- N/A – the microservice is complete.

D. How is your teammate going to access your microservice?
Edward can clone the GitHub repository and run the Flask app locally. or he 

GitHub Repo: https://github.com/chrisdniels12/CS361_MicroserviceA_for_teammate

Run instructions: ******************************

This will start the server at http://localhost:5000.


E. If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?

- If Edward runs into issues, he should contact me through personal email, Discord, or Teams so I can troubleshoot. I’m happy to help with setup or debugging.

-  What’s your availability?
I’m available Monday to Friday, from 1pm to 3pm and 5pm -8pm PST, Saturday and Sunday: 1pm to 5pm PST.


F. If your teammate cannot access/call your microservice, by when do they need to tell you?
May 22, 2025

G. Is there anything else your teammate needs to know?
- Input is case sensitive. Please use exact Marvel character names like "Iron Man", "Spider-Man".
- Otherwise, everything should work out of the box

