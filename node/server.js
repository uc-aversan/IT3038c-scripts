var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");

const toTime = require('to-time');

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err,body) {
                res.writeHead(200, {"Content-Type": "text/html"});
                res.end(body);
        })
    }

    else if(req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        const cpus = os.cpus().length;
        freemem = ((os.freemem()) * .001);
        totalmem = ((os.totalmem()) * .001);
        const frame = toTime.fromSeconds(os.uptime());
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${frame.humanize()}</p>
            <p>Total Meemory: ${totalmem} MB</p>
            <p>Free Memory: ${freemem} MB</p>
            <p>Number of CPUs: ${cpus}</p>
        </dody>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else{
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");

