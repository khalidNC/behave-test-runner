from behave import fixture, use_fixture
from mocks.api_mock import APIMock
from mocks.browser_mock import Browser


@fixture
def browser_mock(context):
    context.browser = Browser('myweb.com')
    yield context.browser
    context.browser.reset()


@fixture
def api_mock(context):
    context.api = APIMock()
    yield context.api
    context.api.reset()


def before_feature(context, feature):
    use_fixture(browser_mock, context)
    use_fixture(api_mock, context)
