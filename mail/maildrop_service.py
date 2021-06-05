import json
from pyquery import PyQuery

from rest.controllers.rest_controllers import session_request

BASE_URL = "https://api.maildrop.cc/v2/mailbox"


# Note comment about API here:
# https://github.com/m242/maildrop/issues/18#issuecomment-158133564
class Maildrop:
    def __init__(self, inbox_name):
        self._inbox_name = inbox_name

    def inbox(self):
        url = "/".join([BASE_URL, self._inbox_name])
        headers = {
            'authority': 'api.maildrop.cc',
            'x-api-key': 'QM8VTHrLR2JloKTJMZ3N6Qa93FVsx8LapKCzEjui',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = session_request("GET", url=url, headers=headers, body={}, isJsonPayload=False, allow_fw=False)
        assert response.status_code == 200, f'issue during inbox read occurred for client {self._inbox_name}'
        inbox = json.loads(response.text)
        return inbox

    def create_inbox(self):
        url = "/".join([BASE_URL, self._inbox_name])
        headers = {
            'authority': 'api.maildrop.cc',
            'x-api-key': 'QM8VTHrLR2JloKTJMZ3N6Qa93FVsx8LapKCzEjui',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = session_request("OPTIONS", url=url, headers=headers, body={}, isJsonPayload=False, allow_fw=False)
        assert response.status_code == 200, f'issue during mail {self._inbox_name} creation occurred'

    def message(self, email_id):
        url = "/".join([BASE_URL, self._inbox_name, email_id])
        headers = {
            'authority': 'api.maildrop.cc',
            'x-api-key': 'QM8VTHrLR2JloKTJMZ3N6Qa93FVsx8LapKCzEjui',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = session_request("GET", url=url, headers=headers, body={}, isJsonPayload=False, allow_fw=False)
        assert response.status_code == 200, f'issue during message read occurred for client {self._inbox_name}'
        message = json.loads(response.text)
        return message

    def delete(self, email_id):
        url = "/".join([BASE_URL, self._inbox_name, email_id])
        headers = {
            'authority': 'api.maildrop.cc',
            'x-api-key': 'QM8VTHrLR2JloKTJMZ3N6Qa93FVsx8LapKCzEjui',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = session_request("DELETE", url=url, headers=headers, body={}, isJsonPayload=False, allow_fw=False)
        deleted = json.loads(response.text)

        return deleted


def create_mailbox(recipient):
    maildrop = Maildrop(recipient)
    maildrop.inbox()
    maildrop.create_inbox()


def get_confirmation_url(recipient):
    maildrop = Maildrop(recipient)
    emails = maildrop.inbox()
    maildrop.create_inbox()

    email_id = emails['messages'][0]['id']
    email = maildrop.message(email_id)

    pq = PyQuery(email['html'])
    link = pq(".rounded-btn-a")
    confirmation_url = link.attr("href")
    return confirmation_url

print(get_confirmation_url("test_AnnaMiller"))