from behave import given, when, then
import sys

sys.path.append('../')
from mocks.api_mock import APIMock


@given('I am logged as admin')
def step_given_logged_as_admin(context):
    context.api = APIMock()


@when('I request API GET api/v1/users')
def step_when_request_api_users(context):
    context.api.request('GET', '/api/v1/users')


@then('I get HTTP 200 status code')
def step_then_get_http_200(context):
    status_code = context.api.get_status_code()
    assert status_code == 200


@then('I get JSON in response body')
def step_then_get_json_response(context):
    response_json = context.api.get_response_json()
    assert response_json


@then('the HTTP response body contains a page with 4 users')
def step_then_http_response_contains_4_users(context):
    user_list = context.api.get_response_json()['data']
    assert len(user_list) == 4


@then('1 of them is Administrator')
def step_then_1_of_them_is_admin(context):
    user_list = context.api.get_response_json()['data']
    admin_count = len([user for user in user_list if user['role'] == 'Administrator'])
    assert admin_count == 1
