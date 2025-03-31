Here's your **README.md** file for the Amazon India Smart TV Scraper project.  

---

# **Amazon India Smart TV Scraper**  

This project is a **web scraper** for **Amazon India Smart TV product pages**. It extracts product details, images, and descriptions and generates an **AI-based review summary** and an **AI-generated image** for the product.

## **Features**  
✅ **Scrape Amazon Product Details**  
✅ **Extract "About this item" & "Product Information"**  
✅ **Fetch All Product Images**  
✅ **Generate AI Review Summary (Gemini API)**  
✅ **Generate AI-Based Product Image**  
✅ **Headless Scraping with Proxy Support**  

---

## **Folder Structure**  
```
Amazon-Web_Scraper/
│── backend/
│   │── app.py                 # Flask backend
│   │── scraper.py             # Web scraper (Selenium)
│   │── ai_summary.py          # AI review summary & AI image generation
│   │── requirements.txt       # Backend dependencies
│
│── frontend/
│   │── src/
│   │   │── components/
│   │   │── App.jsx            # Main React component
│   │   │── api.js             # Handles API calls to backend
│   │── public/
│   │── index.html             # HTML entry point
│   │── package.json           # Frontend dependencies
│
│── README.md                  # Project documentation
```

---

## **Installation**  

### 🔹 **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/Amazon-Web_Scraper.git
cd Amazon-Web_Scraper
```

### 🔹 **2️⃣ Backend Setup (Python)**  
#### **Install Dependencies**  
```sh
cd backend
pip install -r requirements.txt
```

#### **Run Backend**  
```sh
python app.py
```

### 🔹 **3️⃣ Frontend Setup (React + Vite)**  
#### **Install Dependencies**  
```sh
cd frontend
npm install
```

#### **Run Frontend**  
```sh
npm run dev
```

---

## **Backend API Endpoints**  

### **📌 Scrape Product Data**  
#### **Endpoint:**  
```http
POST /scrape
```
#### **Request Body (JSON):**  
```json
{
  "url": "https://www.amazon.in/dp/B09G9HD6PD"
}
```

#### **Response (JSON):**  
```json
{
  "name": "Samsung 43-inch Crystal 4K TV",
  "rating": "4.5 out of 5 stars",
  "num_ratings": "12,345",
  "price": "₹34,999",
  "discount": "10% off",
  "description": "Powerful 4K UHD TV with HDR10+...",
  "images": [
    "https://m.media-amazon.com/images/I/xyz.jpg",
    "https://m.media-amazon.com/images/I/abc.jpg"
  ],
  "review_summary": "This Smart TV offers great picture quality...",
  "ai_image": "https://openai.com/generated-image-url.jpg"
}
```

---

## **Key Technologies Used**  
### **📌 Backend**  
- **Flask** – Handles API requests  
- **Selenium** – Scrapes Amazon India  
- **Gemini API** – AI-generated review summary  
- **DALL·E** – AI-generated product images  

### **📌 Frontend**  
- **React.js (Vite)** – Modern UI framework  
- **Axios** – Fetches data from the backend  

---

## **Troubleshooting & Common Errors**  

### ❌ **Selenium: `no such element` error**  
✅ **Solution:**  
- Amazon changes its website frequently. Check if product elements exist using `WebDriverWait`.

### ❌ **Network Error (`AxiosError: ERR_NETWORK`)**  
✅ **Solution:**  
- Ensure the backend is running on `http://localhost:5000`.  

### ❌ **AI Summary/AI Image Fails (`openai.ChatCompletion` Error)**  
✅ **Solution:**  
- Upgrade OpenAI library:  
  ```sh
  pip install --upgrade openai
  ```
