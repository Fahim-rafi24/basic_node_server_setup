const http = require('http');
const { routeHandler } = require('./routes/index');
require('dotenv').config();


const PORT = process.env.PORT || 5000;

// initialize the HTTP server
const server = http.createServer((req, res) => {
    
    
    // cors settings
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');


    // handle preflight requests
    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    
    // defind route
    routeHandler(req, res);
});

// start the local server
server.listen(PORT, () => {
    console.log(`========================================`);
    console.log(`🚀 Server is running on port ${PORT}`);
    console.log(`👉 Access it at: http://localhost:${PORT}/api/users`);
    console.log(`========================================`);
});

// start the machine server
// server.listen(PORT, () => {});