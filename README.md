# Todo Django App

Admin informations
```
Username: masterplan
Email address: isakajames@medikea.co.tz
Password: hDF98&@bRTaE4
```

## Testing Tools:
> httpie
| Command | Usage |
|----------|:--------:|
| http POST http://127.0.0.1:80/api/register/ username=newuser password=newpassword email=newuser@example.com role=user | Register a new user | 
| http POST http://127.0.0.1:80/api/login/ username=masterplan password='hDF98&@bRTaE4'| Obtain a token for the user | 
| TOKEN=<your_access_token got from first command>  http POST http://127.0.0.1:80/api/todos/ title="Test Todo" description="This is a test todo" expires_at="2024-07-12T12:00:00Z" "Authorization: Bearer $TOKEN" | Create a new Todo | 
 | http GET http://127.0.0.1:80/api/todos/1 "Authorization: Bearer $TOKEN" | Retrieve details of a specific Todo |
 | http PUT http://127.0.0.1:80/api/todos/1 title="Updated Todo" description="Updated description" "Authorization: Bearer $TOKEN" | Update a Todo (only accessible by admin) |
 | http DELETE http://127.0.0.1:80/api/todos/1 "Authorization: Bearer $TOKEN" | Delete a Todo (only accessible by admin) |



```bash
httpie #used to test request on command line ie http POST http://127.0.0.1:80/api/register/ username=newuser password=newpassword email=newuser@example.com role=user

```
