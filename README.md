
- User Login/Signup
- Search Users by Email or Name
- Send, Accept, Reject Friend Requests
- List Friends
- List Pending Friend Requests
- Rate limiting on friend request sending (max 3 per minute)

STEP 1:

git clone https://github.com/Ajananth27/social_network.git
cd social_network

STEP 2:
after create environment folder If requirment in requirement.txt,

pip install -r requirements.txt

STEP 3:
python manage.py makemigrations
python manage.py migrate

python manage.py runserver

API Endpoints:

1 - USEr signup::
  URL: /api/signup/
  Method: POST
 data = {
  "email": "user@example.com",
  "password": "password123"
}

2- LOgin 

URL: /api/login/
Method: POST
data: {
  "email": "user@example.com",
  "password": "password123"
}

3 - Search Users

URL: /api/search/
Method: GET
Query Params: keyword
/api/search/?keyword=am

4 Send Friend Request

URL: /api/send-friend-request/
Method: POST

5 Accept Friend Request

URL: /api/accept-friend-request/<request_id>/
Method: POST

6 Reject Friend Request
URL: /api/reject-friend-request/<request_id>/
Method: POST

7 List Friends

URL: /api/friends/
Method: GET


8 List Pending Friend Requests

URL: /api/pending-requests/
Method: GET

