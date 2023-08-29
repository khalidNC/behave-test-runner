from behave import fixture, use_fixture
from mocks.website_mock import WebsiteMock
from mocks.api_mock import APIMock


@fixture
def website_mock(context):
    context.mock = WebsiteMock()
    yield context.mock
    context.mock.reset()


@fixture
def api_mock(context):
    context.mock = APIMock()
    yield context.mock
    context.mock.reset()


def before_feature(context, feature):
    use_fixture(website_mock, context)
    use_fixture(api_mock, context)
