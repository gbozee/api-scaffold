import jwt
from {{cookiecutter.project_slug}} import types, settings

async def verify_access_token(bearer_token, **kwargs) -> types.AuthorizedUser:
    init = jwt.decode(bearer_token, verify=False)
    if "aud" in init:
        decoded_value = decode_access_token(bearer_token, audience=init["aud"][0])
    else:
        decoded_value = decode_access_token(bearer_token)
        return types.AuthorizedUser(
            user=decoded_value["email"], auth_roles=["authenticated"]
        )


def decode_access_token(access_token, **kwargs):
    ALGORITHM = "HS256"
    access_token_jwt_subject = "access"
    decoded_value = jwt.decode(
        access_token, str(settings.SECRET_KEY), algorithms=ALGORITHM, **kwargs
    )
    return decoded_value
