
import json

params = {}
@given(u'alarma esta "{alarma}"')
def step_impl(context, alarma):
    params['hora-alarma'] = alarma


@when(u'hora es "{hora}"')
def step_impl(context, hora):
    params['hora-actual'] = hora


@then(u'suena la alarma')
def step_impl(context):
    response = context.client.get('/api/alarma/sonar', query_string=params)
    resultado = json.loads(response.data)
    assert resultado['sonar']
