import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import time

async def verify():
    # Start server
    server = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
    time.sleep(2)  # Give server time to start

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000")

        print("Checking Login Page...")
        # Login
        await page.fill("#loginPass", "1234")
        await page.click("#btnLogin")
        await page.wait_for_selector("#app", state="visible")

        print("Checking Nav Items for role='button' and tabindex...")
        nav_items = await page.query_selector_all(".nav-item")
        for item in nav_items:
            role = await item.get_attribute("role")
            tabindex = await item.get_attribute("tabindex")
            if role != "button" or tabindex != "0":
                print(f"FAILED: Nav item {await item.inner_text()} missing role or tabindex")
                os._exit(1)
        print("PASS: Nav items ok")

        print("Checking Top Bar Badges for role='button' and tabindex...")
        badges = await page.query_selector_all(".badge-tc")
        for badge in badges:
            role = await badge.get_attribute("role")
            tabindex = await badge.get_attribute("tabindex")
            if role != "button" or tabindex != "0":
                print(f"FAILED: Badge {await badge.get_attribute('id')} missing role or tabindex")
                os._exit(1)
        print("PASS: Badges ok")

        print("Checking Hamburger for aria-label...")
        hamburger = await page.query_selector("#hamburger")
        label = await hamburger.get_attribute("aria-label")
        if not label:
            print("FAILED: Hamburger missing aria-label")
            os._exit(1)
        print("PASS: Hamburger ok")

        print("Checking focus-visible style presence...")
        content = await page.content()
        if ":focus-visible" not in content:
            print("FAILED: :focus-visible style not found in page content")
            os._exit(1)
        print("PASS: focus-visible ok")

        await browser.close()

    server.kill()
    print("ALL VERIFICATIONS PASSED")

if __name__ == "__main__":
    asyncio.run(verify())
