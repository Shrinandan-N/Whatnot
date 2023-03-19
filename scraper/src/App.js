import React, { useState } from "react";
import ReactDOM from "react-dom";
import axios from "axios";

const API_KEY = "Bearer apify_api_OZNmauRkDJ8MGsofrwikMrgcTL8exe0ZgF7q";
const App = () => {
  const [textFields, setTextFields] = useState([{ id: 0, value: "" }]);
  const [results, setResults] = useState("");

  const handleAddField = () => {
    setTextFields((prevState) => [
      ...prevState,
      { id: prevState.length, value: "" },
    ]);
  };

  const handleTextFieldChange = (id, value) => {
    setTextFields((prevState) =>
      prevState.map((field) => (field.id === id ? { ...field, value } : field))
    );
  };

  const handleGetData = async () => {
    const usernames = textFields.map((field) => field.value);
    console.log(usernames);
    const bodyJson = { usernames: usernames };
    try {
      const response = await axios.post(
        "http://localhost:800/profile",
        bodyJson,
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: API_KEY,
          },
        }
      );
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1
        style={{
          fontFamily: "Futura",
          fontWeight: "bold",
          fontSize: "36px",
          marginBottom: "20px",
        }}
      >
        Whatnot Scraper
      </h1>
      <div
        style={{ marginTop: "20px", fontFamily: "Futura", fontSize: "16px" }}
      >
        Usernames:
      </div>
      {textFields.map((field) => (
        <input
          key={field.id}
          type="text"
          value={field.value}
          onChange={(e) => handleTextFieldChange(field.id, e.target.value)}
          style={{
            margin: "5px",
            padding: "10px",
            borderRadius: "10px",
            border: "1px solid #ddd",
            marginBottom: "10px",
            fontFamily: "Futura",
            fontSize: "16px",
          }}
        />
      ))}
      <button
        onClick={handleAddField}
        style={{
          margin: "10px",
          padding: "10px",
          borderRadius: "10px",
          border: "2px solid #1E90FF",
          backgroundColor: "#fff",
          color: "#1E90FF",
          fontFamily: "Futura",
          fontSize: "16px",
          fontWeight: "bold",
          marginRight: "10px",
        }}
      >
        +
      </button>
      <button
        onClick={handleGetData}
        style={{
          marginLeft: "10px",
          padding: "10px",
          borderRadius: "10px",
          border: "2px solid #1E90FF",
          backgroundColor: "#1E90FF",
          color: "#fff",
          fontFamily: "Futura",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Get Data
      </button>
      <div
        style={{ marginTop: "20px", fontFamily: "Futura", fontSize: "16px" }}
      >
        Results:
        <div
          style={{
            marginTop: "10px",
            border: "1px solid #ddd",
            padding: "10px",
            borderRadius: "10px",
          }}
        >
          {/* Display results here */}
        </div>
      </div>
    </div>
  );
};

export default App;
