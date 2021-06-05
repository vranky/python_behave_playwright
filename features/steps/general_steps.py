import os

from behave import *
from sys import platform
from helpers.helper import get_context_item, random_data


@given(u'User is created with params')
def step_impl(context):
    context.first_name = get_context_item(context.table, 'first_name')
    context.last_name = get_context_item(context.table, 'last_name')
    context.user_name = get_context_item(context.table, 'user_name')
    context.company_name = get_context_item(context.table, 'company_name')
    context.password = get_context_item(context.table, 'password')
    context.active = get_context_item(context.table, 'active')


@given(u'User is created with params and subscription')
def step_impl(context):
    context.first_name = get_context_item(context.table, 'first_name')
    context.last_name = get_context_item(context.table, 'last_name')
    context.user_name = get_context_item(context.table, 'user_name')
    context.company_name = get_context_item(context.table, 'company_name')
    context.password = get_context_item(context.table, 'password')
    context.active = get_context_item(context.table, 'active')


@given(u'Mailbox with prefix {mail_prefix} is created')
def step_impl(context, mail_prefix):
    if mail_prefix == 'random':
        context.user_name = random_data()['user_name']
    else:
        context.user_name = f"{mail_prefix}@maildrop.cc",


@step(u'Create temp mailbox in getnada client')
def step_impl(context):
    context.page2 = context.pw_context.new_page()

    context.user = context.user_name.split('@')[0].lower()
    context.page2.goto("https://getnada.com/")
    context.page2.click("text=Add inboxe")

    context.page2.focus("[placeholder=\"user name\"]")
    if platform == 'linux':
        context.page2.keyboard.dblclick("[placeholder=\"user name\"]")
        context.page2.keyboard.press("Delete")
    else:
        context.page2.keyboard.press("Meta+A")
        context.page2.keyboard.press("Delete")
    context.page2.type("[placeholder=\"user name\"]", context.user)
    context.page2.select_option("select", "robot-mail.com")

    context.page2.click("text=Add now!")

@step(u'Confirm email through getnada client')
def step_impl(context):
    context.page2.wait_for_timeout(20000)
    context.page2.reload()
    context.page2.wait_for_load_state("load")
    context.page2.wait_for_load_state("domcontentloaded")
    context.page2.wait_for_load_state("networkidle")
    context.page2.click("text=Activate your user profile")
    context.page2.reload()
    context.page2.wait_for_load_state("load")
    context.page2.wait_for_load_state("domcontentloaded")
    context.page2.wait_for_load_state("networkidle")
    context.page2.frame(name="the_message_iframe").click("span:has-text(\"Activate your user profile\")")


