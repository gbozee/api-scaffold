import typing
from sstarlette.base import ServiceResult

{% if cookiecutter.auth_backend|lower == 'y' -%}
class AuthorizedUser(typing.NamedTuple):
    user: str
    auth_roles: typing.List[str]
{% endif %}

