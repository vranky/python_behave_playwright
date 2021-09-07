from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from sys import platform
import os
import allure


@fixture
def browser(context):
    with sync_playwright() as playwright:
        isHeadless = True if platform == 'linux' else False
        context.bw_context = playwright.chromium.launch(headless=True)

        # TODO video recording
        # record_video_dir='report/video',
        # record_video_size={"width": 1024, "height": 768}
        yield context.bw_context


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if step.status == "failed":
        screen_name = f"{context.step.name}_fail.png".replace(" ", "_")
        # video_name = f"{context.step.name}_video_fail.WEBM".replace(" ", "_")
        ctx = context.page if 'getnada' not in step.name else context.page2
        screenshot = ctx.screenshot(full_page=True)
        # video_path = ctx.video.path()
        allure.attach(screenshot, name=screen_name, attachment_type=allure.attachment_type.PNG)
        # allure.attach(video_path, name=video_name, attachment_type=allure.attachment_type.WEBM)

def before_scenario(context, scenario):
    use_fixture(browser, context)
