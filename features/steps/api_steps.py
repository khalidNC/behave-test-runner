from behave import given, when, then
from asserts import assert_equal
from features.browser import Browser


@given('I am logged as admin')
def step_given_logged_as_admin(context):
    context.browser = Browser("https://api.myweb.com")


@when('I request API GET api/v1/users')
def step_when_request_api_users(context):
    context.browser.request('GET', '/api/v1/users')


@then('I get HTTP 200 status code')
def step_then_get_http_200(context):
    status_code = context.browser.get_status_code()
    assert_equal(status_code, 200)


@then('I get JSON in response body')
def step_then_get_json_response(context):
    response_json = context.browser.get_response_json()
    assert response_json


@then('the HTTP response body contains a page with 4 users')
def step_then_http_response_contains_4_users(context):
    user_list = context.browser.find_object('user_list')
    assert_equal(len(user_list), 4)


@then('1 of them is Administrator')
def step_then_1_of_them_is_admin(context):
    admin_count = context.browser.find_object('admin_count')
    assert_equal(admin_count, 1)