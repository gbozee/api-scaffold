{% if cookiecutter.auth_backend|lower == 'y' -%}import jwt{% endif %}
from {{cookiecutter.project_slug}} import types, settings

{% if cookiecutter.auth_backend|lower == 'y' -%}
async def verify_access_token(bearer_token, **kwargs) -> types.AuthorizedUser:
    init = jwt.decode(bearer_token, verify=False)
    if "aud" in init:
        decoded_value = decode_access_token(bearer_token, audience=init["aud"][0])
    else:
        decoded_value = decode_access_token(bearer_token)
        return types.AuthorizedUser(
            user=decoded_value["email"], auth_roles=["authenticated"]
        )
def auth_result_callback(kls, verified_user: types.AuthorizedUser):
    return kls(verified_user.auth_roles), verified_user.user

def decode_access_token(access_token, **kwargs):
    ALGORITHM = "HS256"
    access_token_jwt_subject = "access"
    decoded_value = jwt.decode(
        access_token, str(settings.SECRET_KEY), algorithms=ALGORITHM, **kwargs
    )
    return decoded_value
{% endif %}

async def demo(post_data,query_params=None, headers=None)->types.ServiceResult:
    return types.ServiceResult(data={'hello':'world'})

service = {
    "/demo":{"func":demo,'methods':['GET']}
}