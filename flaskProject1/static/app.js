"use strict";

var myInit = {
    method: 'GET',
    headers: {
        'Content-type': 'Application/Json'
    },
    mode: 'cors',
    cache: 'default' };

let myRequest = new Request ("static/saidadocw.json", myInit);

fetch(myRequest)
    .then(function (resp) {
        return resp.json();
    })
    .then(function (data){
        console.log(data.Timestamp);
    });


readfile