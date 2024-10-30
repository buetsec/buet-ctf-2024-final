const express = require('express');
const { readFileSync } = require("fs");
const jsonwebtoken = require('jsonwebtoken');

const serverPort = 2490;

let sharedKey = readFileSync('public.pem', 'utf-8');
let confidentialKey = readFileSync('private.pem', 'utf-8');

let initialState = {
    isUserRegistered: false,
};

const baseToken = jsonwebtoken.sign(initialState, confidentialKey, { algorithm: 'RS256' });
const successResponse = JSON.stringify({ message: 0 });
const errorResponse = JSON.stringify({ message: 1 });
const ctfResponse = JSON.stringify({ message: "BUETCTF{DR1V3RZ_R3V3NG3_3NDG4M3}" });

const serverApp = express();

serverApp.get('/validate', (request, response) => {
    let result = successResponse;

    if (request.cookies.token) {
        try {
            if (jsonwebtoken.verify(request.cookies.token, sharedKey)) {
                const decodedToken = jsonwebtoken.decode(request.cookies.token);
                if (decodedToken.isUserRegistered === true) {
                    result = ctfResponse;
                }
            }
        } catch (error) {
            result = errorResponse;
        }
    }

    response.setHeader('Content-Type', 'application/json');
    response.cookie('token', baseToken);
    response.send(result);
});

serverApp.listen(serverPort, () => {
    console.log(`Server is operational at http://localhost:${serverPort}`);
});