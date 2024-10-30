const express = require('express');
const { readFileSync } = require("fs");
const cookieParser = require('cookie-parser');
const jsonwebtoken = require('jsonwebtoken');
const path = require('path');

const serverPort = 2490;

let sharedKey = readFileSync('public.pem', 'utf-8');
let confidentialKey = readFileSync('private.pem', 'utf-8');

let initialState = {
    isUserRegistered: false,
};

const baseToken = jsonwebtoken.sign(initialState, confidentialKey, { algorithm: 'RS256' });
const successResponse = JSON.stringify({ message: 0 });
const errorResponse = JSON.stringify({ message: 1 });
const ctfResponse = JSON.stringify({ message: "BUETCTF{D34dEnd_JWT_AccessEng1n3_C1ty0fF4ll_4lg0FL4W_r3V3aLeD_H4ck3d_Path_5ePsckJ5PnYT}" });

const serverApp = express();
const staticFilesPath = path.join(__dirname, 'public');
serverApp.use(express.static(staticFilesPath));
serverApp.use(cookieParser());

serverApp.get('/validate-token', (request, response) => {
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

serverApp.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

serverApp.get('/garage', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'garage.html'));
});

serverApp.listen(serverPort, () => {
    console.log(`Server is operational at http://localhost:${serverPort}`);
});