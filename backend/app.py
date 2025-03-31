from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_amazon_product
from ai_summary import generate_ai_summary

app = Flask(__name__)
CORS(app)  # Enable frontend-backend communication

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    product_url = data.get("url")

    if not product_url:
        return jsonify({"error": "No URL provided"}), 400

    # Scrape product details
    product_data = scrape_amazon_product(product_url)

    if "error" in product_data:
        print("Scraper Error:", product_data["error"])
        return jsonify({"error": product_data["error"]}), 500

    print("Scraped Data:", product_data)  # Debugging

    # Generate AI review summary
    try:
        product_data["review_summary"] = generate_ai_summary(product_data["description"])
    except Exception as e:
        print("AI Summary Error:", str(e))
        product_data["review_summary"] = "AI Summary Failed"

    # Generate AI product image
    try:
        product_data["ai_generated_image"] = generate_ai_image(product_data["description"])
    except Exception as e:
        print("AI Image Error:", str(e))
        product_data["ai_generated_image"] = None

    return jsonify(product_data)


if __name__ == "__main__":
    app.run(debug=True)
