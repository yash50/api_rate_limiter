Objective:
The objective of this project is to make a plug and play API rate limiter. The framework of choice for now is Django mostly because of convenience provided by inbuilt features of Django and more importantly because it takes time to learn new frameworks.

Approach taken:
1. First thing to be noted is that only authenticated users are allowed to make any calls to the APIs. If an unauthenticated user makes a request to any of the APIs, the request will be declined. Also, a token needs to be generated manually for each user once registered, which is used for making any further requests for the APIs.
2. Next aspect is the APIs – default limits exist for individual APIs. However if some user has a special status, the number of requests allowed for that user are fetched from the database and then a call to the ‘ratelimit’ function is made with token, number of requests allowed and expiry time for allowed requests as parameters.
3. Now comes the function that checks whether the user has exhausted his allowed requests or not. For keeping track of requests, another table in database must be created. However, database access time is high, every time a request is encountered, the toll on the server increases and hence a different way of keeping track of requests must be taken into consideration.
4. So the Redis database comes into consideration. Redis is an in-memory NoSQL database used mostly for caching purposes. So, we generate a key on the combination of token of the user and the API being requested and that key is used to keep track of number of requests. Another aspect that is taken into consideration by Redis is the expiry time. Hence, once the requests are exhausted, the key in the Redis database denies the call to API and as soon as the expiry time of the requests is completed (say 60 seconds), the key gets deleted from the database by itself. So whenever a new request is made outside the expiry time window (after 60 seconds), a new entry will be made into the Redis database (i.e., cache) and the call to API would be processed.

Storage format:
For data storage, the inbuilt database provided by the Django framework, i.e., sqlite3 is being used. However, since the response to the requests from the server needs to be quick, we have to use an additional caching layer. For this caching layer, Redis database has been used to keep track of number of requests by any user.
Redis just stores the key corresponding to the token of user and API called and the number of requests already made for the allotted time period.
Instead of Redis, MemCached can also be used for the caching layer as both are quite similar in their performance


Setup & running Guide:

Before Setup, Make sure you have these in your system:

	Python Version-3.5/3.6

	Django Version-2.1.1


Setup Instructions:

1. Install redis using the link (only for Windows-based systems): https://github.com/downloads/rgl/redis/redis-2.4.6-setup-64-bit.exe
2. Get into project directory: 'cd api_rate_limiter'
3. Create a new virtual environment, using python 3.x
	a) 'pip install virtualenv'
	b) 'virtualenv <env_name>'
4. Activate the virtual environment: '<env_name>\Scripts\activate'
5. Issue this command in terminal: 'pip install -r requirements.txt'
6. Start redis server: <redis_path>\redis-server.exe

Run Server:

7. Change directory to YashAPI : 'cd MyAPI'
8. Issue command on terminal: 'python manage.py runserver'

Run Client:
(On a new command prompt)
9. Get into project directory: 'cd api_rate_limiter'
10. Activate virtual environment: 'env_name\Scripts\activate'
11. Change directory to testing-clients: 'cd testing-clients'
12. run a client - 'python test_developer.py'

Note - admin panel credentials (localhost:8000/admin):
username - admin
password - testpassword


Assumptions
1.	Default developer API hits allowed – 5 requests per 60 seconds
2.	Default organization API hits allowed – 10 requests per 60 seconds
3.	User needs to be registered with the server for making any API calls
4.	Authentication tokens need to be separately communicated to the clients
5.	Authentication tokens need to be manually configured on client side for now

Improvements
1.	Anonymous user can also be allowed to make API calls by keeping a track of the IP address being used by the user.
2.	The program can be made plug and play by making the program as an external library.
3.	Token generation and communication to the client can be automated
