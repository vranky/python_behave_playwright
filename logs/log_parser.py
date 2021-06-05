import requests
import json
import sys
import re

# resp = requests.get(url="https://dockerlogs.test.liquidtool.com/log/lts_keycloak_1", auth=("lts","LTS!34"))

row= "2021-05-26T12:07:21.789215883Z 12:07:21,789 INFO  [com.lts.keycloak.providers.LtsEmailSenderProviderFactory] (default task-712) send emailEvent: 'USER_ACTIVATION' with attributes: {userUsername=test_tinarange@robot-mail.com, userLastName=Woodard, realmName=Liquidtool, link=https://identity.test.liquidtool.com/auth/realms/lts/login-actions/action-token?key=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2YTVlMGZhZC1mN2YxLTRjMzctOTVmYS1iNjkwNjNhYTUzMWQifQ.eyJleHAiOjE2MjIwMzQ0NDEsImlhdCI6MTYyMjAzMDg0MSwianRpIjoiOTYyNzg5YTMtOTVjOC00ZTU2LWFhNzItZWQyYjRhMzI3ZDg3IiwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS50ZXN0LmxpcXVpZHRvb2wuY29tL2F1dGgvcmVhbG1zL2x0cyIsImF1ZCI6Imh0dHBzOi8vaWRlbnRpdHkudGVzdC5saXF1aWR0b29sLmNvbS9hdXRoL3JlYWxtcy9sdHMiLCJzdWIiOiJkNWZkNjllNi03Yzc4LTQ2ZTktOTlkYS02MTRkODFiYTRmMzMiLCJ0eXAiOiJ2ZXJpZnktZW1haWwiLCJhenAiOiJsaXF1aWQtdG9vbC1wb3J0YWwiLCJub25jZSI6Ijk2Mjc4OWEzLTk1YzgtNGU1Ni1hYTcyLWVkMmI0YTMyN2Q4NyIsImVtbCI6InRlc3RfdGluYXJhbmdlQHJvYm90LW1haWwuY29tIiwiYXNpZCI6IjYzMGEyNWRjLTU2MmEtNDQzMi1hODkwLTNlODY1YzcwNmRmZS5haVNRZFF3THhiTS5hOTZiOTU5MS00OWY5LTRhYWItODhhOC1lZWJmOTE1Y2U5MTQiLCJhc2lkIjoiNjMwYTI1ZGMtNTYyYS00NDMyLWE4OTAtM2U4NjVjNzA2ZGZlLmFpU1FkUXdMeGJNLmE5NmI5NTkxLTQ5ZjktNGFhYi04OGE4LWVlYmY5MTVjZTkxNCJ9.Gv9ZPZGLufUMmb099hvKaxj8k9OXHxlf5_iSdivTqlk&client_id=liquid-tool-portal&tab_id=aiSQdQwLxbM, userEmail=test_tinarange@robot-mail.com, userFirstName=Jano, expire-in=60, userId=d5fd69e6-7c78-46e9-99da-614d81ba4f33}"


# 27.59.104.166 - - [04/Oct/2019:21:15:54 +0000] "GET /users/login HTTP/1.1" 200 41716 "-" "okhttp/3.12.1"
