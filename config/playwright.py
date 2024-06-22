import os
import dotenv

dotenv.load_dotenv()

class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    ENV = os.getenv('ENV') if os.getenv('ENV') is not None else 'stage'
    BROWSER = os.getenv('BROWSER') if os.getenv('BROWSER') is not None else 'chrome'
    IS_HEADLESS = True if os.getenv('HEADLESS') and os.getenv('HEADLESS') == "True" else False
    print(IS_HEADLESS)
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US'