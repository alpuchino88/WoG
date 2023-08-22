from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_scores_service(app_url):
    try:
        driver = webdriver.Chrome()
        driver.get(app_url)

        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    finally:
        driver.quit()


def main_function(app_url):
    if test_scores_service(app_url):
        print("Tests passed successfully!")
        return 0
    else:
        print("Tests failed.")
        return -1


if __name__ == "__main__":
    app_url = "http://127.0.0.1:5000"
    exit_code = main_function(app_url)
    sys.exit(exit_code)
