import React, { useState } from "react";
import axios from "./api";

function App() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleScrape = async () => {
    setLoading(true);
    try {
      const response = await axios.post("/scrape", { url });
      setData(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">Amazon Smart TV Scraper</h1>
      <input
        type="text"
        placeholder="Enter Amazon Product URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="p-2 border rounded w-full max-w-lg mb-4"
      />
      <button
        onClick={handleScrape}
        className="bg-blue-500 text-white px-4 py-2 rounded"
        disabled={loading}
      >
        {loading ? "Scraping..." : "Scrape Data"}
      </button>

      {data && (
        <div className="mt-6 bg-white p-4 rounded shadow w-full max-w-2xl">
          <h2 className="text-xl font-bold">{data.name}</h2>
          <p>⭐ {data.rating} ({data.num_ratings})</p>
          <p>💰 Price: ₹{data.price} ({data.discount} off)</p>
          <h3 className="mt-2 font-semibold">Description:</h3>
          <p>{data.description}</p>

          <h3 className="mt-2 font-semibold">AI-Generated Review Summary:</h3>
          <p>{data.review_summary}</p>

          <h3 className="mt-2 font-semibold">Amazon Product Images:</h3>
          <div className="flex flex-wrap gap-2">
            {data.images.map((img, index) => (
              <img key={index} src={img} alt="Product" className="w-24 h-24 object-cover rounded" />
            ))}
          </div>

          <h3 className="mt-2 font-semibold">AI-Generated Product Image:</h3>
          {data.ai_generated_image && (
            <img src={data.ai_generated_image} alt="AI Product" className="w-64 h-64 object-cover rounded mx-auto" />
          )}
        </div>
      )}
    </div>
  );
}

export default App;
