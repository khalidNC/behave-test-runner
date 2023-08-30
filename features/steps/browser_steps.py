from behave import given, when, then
# from asserts import assert_equal
import sys

sys.path.append('../')
from mocks.browser_mock import Browser


@given('I am logged as admin frontend')
def step_given_logged_as_admin(context):
    context.browser = Browser("https://myweb.com")


@when('I am in Users page')
def step_when_in_users_page(context):
    context.browser.visit_users_page()


@then('4 users are listed')
def step_then_4_users_listed(context):
    user_list = context.browser.find_object('user_list')
    assert_equal(len(user_list), 4)


@then('1 of them is Admin')
def step_then_1_of_them_is_admin(context):
    admin_count = context.browser.find_object('admin_count')
    assert_equal(admin_count, 1)
