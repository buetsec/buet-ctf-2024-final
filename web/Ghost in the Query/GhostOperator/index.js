const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cookieParser = require('cookie-parser');
const puppeteer = require('puppeteer');
const settings = require('./config.json');
const server = express();

server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: false }));
server.use(cookieParser());
server.use(express.static(path.join(__dirname, "/public")));
server.set("views", path.join(__dirname, "views"));
server.set("view engine", "hbs");

server.get('/', (req, res) => {
    res.render('index', { challengeTitle: settings.challengeName });
});

server.post('/', (req, res) => {
    const targetURL = req.body.link;
    let capturedConsole = [];

    (async function navigateAndCapture() {
        const browser = await puppeteer.launch({ args: ['--no-sandbox', '--incognito'] });
        const page = await browser.newPage();

        if (settings.redirectConsoleOutput) {
            page.on('console', async (message) => {
                const logArgs = await Promise.all(message.args().map(arg => arg.jsonValue()));
                logArgs.forEach(arg => {
                    capturedConsole.push("||" + arg.replace(/\n/g, ''));
                });
            });
        }

        try {
            await page.goto(targetURL);
        } catch (error) {
            return res.render('index', {
                msgColor: "red",
                status: "Error visiting URL",
                challengeTitle: settings.challengeName
            });
        }

        await page.setCookie(...settings.cookies);
        await page.cookies(targetURL);
        await page.waitForTimeout(settings.timeout);

        await browser.close();

        if (settings.redirectConsoleOutput) {
            res.render('index', {
                msgColor: "green",
                status: "URL successfully accessed! Console data is available.",
                info: capturedConsole,
                challengeTitle: settings.challengeName
            });
        } else {
            res.render('index', {
                msgColor: "#00ff00",
                status: "URL successfully accessed!",
                challengeTitle: settings.challengeName
            });
        }
    })();
});

server.listen(2491, () => {
    console.log("Server running on port 2491. Access it at http://localhost:2491");
});
