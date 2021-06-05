from behave import *

from props.properties import get_url


@step(u'User launch the-internet home page with injected http_auth')
def step_impl(context):
    context.username = context.table.rows[0][0]
    context.password = context.table.rows[0][1]
    context.pw_context = context.bw_context.new_context(http_credentials={
        'username': context.username,
        'password':  context.password,
    })
    context.page = context.pw_context.new_page()
    context.page.goto(get_url())
    context.page.wait_for_load_state("load")
    context.page.wait_for_load_state("domcontentloaded")
    context.page.wait_for_load_state("networkidle")
    # context.page.goto("localhost:3000")


@step(u'User choose {test_type}')
def step_impl(context, test_type):
    context.page.click(f"text={test_type}")


@step(u'Positive test message {happy_message} occurred')
def step_impl(context, happy_message):
    el = f"text={happy_message}"
    context.page.wait_for_selector(el)
    eval = context.page.is_visible(el)
    assert eval, "Hoho happy message is not happy!"

