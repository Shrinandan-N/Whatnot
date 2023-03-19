import React, { useState } from "react";
import { useEffect } from "react";
import "./upload.css";
import axios from "axios";
import Leads from "./Leads";
import { CircularProgress } from "@material-ui/core";
import logo from "./whatnot.png";

function Upload() {
  const [fileContent, setFileContent] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isLoading2, setIsLoading2] = useState(false);
  const [showLeads, setShowLeads] = useState(false);
  const [leadData, setLeadData] = useState([]);
  const [scrapedResults, setResults] = useState("");
  const dummyData = [
    {
      ownerUsername: "carrera.go.spain",
      likesCount: 80,
      followers: 226,
      url: "instagram.com/carrera.go.spain",
      link: "linktree.bio",
    },
    {
      ownerUsername: "mrslotcar_mossettiracing",
      likesCount: 92,
      followers: 439,
      url: "instagram.com/carrera.go.spain",
      link: "www.mrslotcar.ca",
    },
    {
      ownerUsername: "carrera_usa",
      likesCount: 78,
      followers: 12100,
      url: "instagram.com/carrera.go.spain",
      link: "carrera-revell-toys.com/carrera",
    },
    {
      ownerUsername: "carrera.official",
      likesCount: 6,
      followers: 61500,
      url: "instagram.com/carrera.official",
      link: "linktr.ee/carrera.official",
    },
  ];

  function handleInputFile(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (event) {
      const csvData = event.target.result.replace(/\r/g, ""); // remove extra '\r' characters
      const rows = csvData.split("\n");
      const headers = rows[0].split(",");
      const data = [];
      for (let i = 1; i < rows.length; i++) {
        const row = rows[i].split(",");
        const item = {};
        for (let j = 0; j < headers.length; j++) {
          item[i] = row[j];
        }
        data.push(item);
      }
      setFileContent(data.flatMap((item) => Object.values(item)));
    };

    reader.readAsText(file);
  }

  const handleClick = () => {
    setIsLoading(true);
  };

  useEffect(() => {
    const handleScraping = async () => {
      try {
        const usernames = fileContent;
        const bodyJson = { hashtags: usernames, resultsLimit: 20 };
        const response = await axios.post(
          "http://localhost:800/hashtag",
          bodyJson,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: API_KEY,
            },
          }
        );
        const scrapedUsernames = [];
        const data = await response.data["data"];
        console.log(data);
        data.forEach((element) => {
          scrapedUsernames.push(element.ownerUsername);
        });

        setResults(scrapedUsernames);
      } catch (error) {
        console.error(error);
      }
    };
    const postUsernames = async () => {
      setIsLoading2(true);
      try {
        const bodyJsonProfile = { usernames: scrapedResults };
        await axios.post("http://localhost:800/profile", bodyJsonProfile, {
          headers: {
            "Content-Type": "application/json",
            Authorization: API_KEY,
          },
        });
      } catch (error) {
        console.error(error);
      }

      setIsLoading2(false);
    };
    const fetchLeads = async () => {
      try {
        const leadResponse = await axios.get("http://localhost:800/profile", {
          headers: {
            "Content-Type": "application/json",
            Authorization: API_KEY,
          },
        });
        const leadJson = await leadResponse.data["data"];
        const leads = [];
        leadJson.forEach((item) => {
          const userObj = {
            username: item["username"],
            url: item["url"],
            link:
              item["externalUrl"] != null
                ? item["externalUrl"]
                : "Not Available",
            followers: item["followersCount"],
          };
          leads.push(userObj);
        });
        setLeadData(leads);
        console.log(leads);
        setIsLoading(false);
        setShowLeads(true);
      } catch (error) {
        console.error(error);
      }
    };
    if (isLoading) {
      handleScraping();
      postUsernames();
      if (!isLoading2) {
        fetchLeads();
      }
    }
  }, [isLoading]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} />
        <h1 style={{ fontFamily: "Futura", fontSize: "32px" }}>
          Influencer Sourcing Scraper Tool
        </h1>
        <h3 style={{ fontFamily: "Futura", fontSize: "15px", color: "gold" }}>
          Upload hashtags csv file
        </h3>
        <input
          type="file"
          onChange={handleInputFile}
          style={{ marginRight: "10px" }}
        />
        <button
          style={{
            marginTop: "16px",
            borderRadius: "8px",
            padding: "8px",
            border: "none",
            backgroundColor: "#0074D9",
            color: "white",
            fontFamily: "Futura",
            fontSize: "16px",
            cursor: "pointer",
          }}
          onClick={handleClick}
        >
          Get Leads
        </button>
        {isLoading && (
          <div style={{ marginTop: "16px" }}>
            <h2 style={{ fontFamily: "Futura", fontSize: "15px" }}>
              Deriving leads...
            </h2>
            <CircularProgress />
            <div className="loader" />
          </div>
        )}
        <Leads showLeads={showLeads} scrapedResults={leadData} />
      </header>
    </div>
  );
}

export default Upload;
