from pathlib import Path
from selenium import webdriver
from time import sleep


class ScreenshotTaker:
    def __init__(self):
        self.driver = webdriver.Safari()

    def take_screenshot(self, url: str | Path, output_path: str | Path) -> None:
        self.driver.get(url)
        self.driver.find_element("id", "snip").screenshot(str(output_path))
        sleep(1)
        return None

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    rendered_dir = Path("_site/drafts/highlight-styles")
    shot_dir = Path("drafts/highlight-styles")
    html_files = rendered_dir.glob("*.html")
    shot = ScreenshotTaker()

    for f in html_files:
        if f.name.startswith("code-snippets"):
            continue
        if f.name.startswith("a11"):
            continue

        shot.take_screenshot(
            f"file://{f.absolute()}", shot_dir.joinpath(f.stem + ".png")
        )
        print(f"✅ Saved {f.stem}.png")
    shot.close()
