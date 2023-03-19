const express = require("express");
const axios = require("axios");

const app = express();
const port = 800;

const postData =
  "https://api.apify.com/v2/acts/apify~instagram-profile-scraper/runs";
const getData =
  "https://api.apify.com/v2/acts/apify~instagram-profile-scraper/runs/last/dataset/items";

const getHashtags =
  "https://api.apify.com/v2/acts/apify~instagram-hashtag-scraper/run-sync-get-dataset-items";
app.use(express.json());

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST");
  res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
  next();
});

app.post("/profile", async (req, res) => {
  const { body } = req;
  console.log(body);

  try {
    const response = await axios.post(postData, body, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `${req.headers.authorization}`,
      },
    });

    console.log(req.headers.authorization);

    res.send({ token: response.data.id });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error storing data");
  }
});

app.get("/profile", async (req, res) => {
  try {
    const response = await axios.get(getData, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `${req.headers.authorization}`,
      },
    });

    res.status(200).send({ data: response.data });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data");
  }
});

app.post("/hashtag", async (req, res) => {
  const { body } = req;
  try {
    const response = await axios.post(getHashtags, body, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `${req.headers.authorization}`,
      },
    });
    res.status(200).send({ data: response.data });
  } catch (error) {
    console.error(error);
    res.status(404).send("Error posting data");
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
