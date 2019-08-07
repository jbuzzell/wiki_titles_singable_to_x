import auth

api = auth.auth()


def post():
    status = api.update_status("getting tweet id from api")
    api.update_status("replying", in_reply_to_status_id=status._json["id"])


if __name__ == "__main__":
    post()
