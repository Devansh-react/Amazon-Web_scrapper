from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_amazon_product(url):
    options = Options()
    options.headless = True  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        
        wait = WebDriverWait(driver, 8)

        product_name = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()
        rating = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-icon-alt"))).text.strip()
        num_ratings = wait.until(EC.presence_of_element_located((By.ID, "acrCustomerReviewText"))).text.strip()
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price-whole"))).text.strip()
        
        try:
            discount = driver.find_element(By.CSS_SELECTOR, ".savingsPercentage").text.strip()
        except:
            discount = "No discount available"

        descriptions = []
        desc_elements = driver.find_elements(By.CSS_SELECTOR, "#feature-bullets ul li span")
        for desc in desc_elements:
            descriptions.append(desc.text.strip())

        image_elements = driver.find_elements(By.CSS_SELECTOR, "#altImages img")
        images = [img.get_attribute("src") for img in image_elements]

        driver.quit()

        return {
            "name": product_name,
            "rating": rating,
            "num_ratings": num_ratings,
            "price": price,
            "discount": discount,
            "description": " ".join(descriptions),
            "images": images,
        }

    except Exception as e:
        driver.quit()
        return {"error": str(e)}
