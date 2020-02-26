from {{cookiecutter.project_slug}}.views import app
{% if cookiecutter.sentry_support|lower == 'y' -%}
app.initialize_sentry()
{% endif %}