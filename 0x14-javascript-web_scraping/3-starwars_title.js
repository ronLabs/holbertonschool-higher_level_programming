#!/usr/bin/node
const axios = require('axios');
const idFilm = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${idFilm}`)
  .then(res => {
    console.log(res.data.title);
  });
