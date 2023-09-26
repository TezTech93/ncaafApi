const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const _ = require("lodash");

const app = express();
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static("public"));

mongoose.connect("mongodb+srv://shawnteztech93:Tezzyk32$@cluster0.ahofjvw.mongodb.net/")

const jobsSchema ={
  postClient: String,
  datetime: String,
  content:String,
  location:String
}

const servicesSchema ={
  postClient: String,
  datetime: String,
  content:String,
  location:String
}

const eventsSchema ={
  postClient: String,
  datetime: String,
  content:String,
  location:String
}

const Jobs = mongoose.model("Jobs",jobsSchema)
const Services = mongoose.model("Services",servicesSchema)
const Events = mongoose.model("Events",eventsSchema)

// Route to render the main page
app.get("/jobs", (req, res) => {
  res.render("jobs");
});

// Route to render the edit page
app.get("/services", (req, res) => {
  res.render("services");
});

app.get("/events", (req, res) => {
  res.render("events");
});

// Create a new post
app.post("/jobs", async (req, res) => {
  const postClient = req.body.postClient;
  const datetime = req.body.datetime;
  const content = req.body.content;
  const location = req.body.location;

  const job = new Jobs({
    postClient:postClient,
    datetime:datetime,
    content:content,
    location:location
  })

  job.save();
});

app.post("/services", async (req, res) => {
  const postClient = req.body.postClient;
  const datetime = req.body.datetime;
  const content = req.body.content;
  const location = req.body.location;

  const service = new Services({
    postClient:postClient,
    datetime:datetime,
    content:content,
    location:location
  })

  service.save(); 
});

app.post("/events", async (req, res) => {
  const postClient = req.body.postClient;
  const datetime = req.body.datetime;
  const content = req.body.content;
  const location = req.body.location;

  const event = new Events({
    postClient:postClient,
    datetime:datetime,
    content:content,
    location:location
  })

  event.save();
});

var port = 3000;

app.listen(port, () => {
  console.log(`Backend server is running on http://localhost:${port}`);
});
