const { getUsers, getSingleUser } = require('../controllers/userController');
const { sendResponse } = require('../utils/handler');

// route handler to manage request routing
const routeHandler = (req, res) => {
    const { url, method } = req;

    // GET /api/users
    if (url === '/api/users' && method === 'GET') {
        getUsers(req, res);
    } 
    // GET /api/user/:id
    else if (url.startsWith('/api/user/') && method === 'GET') {
        const id = url.split('/')[3];
        getSingleUser(req, res, id);
    }
    // route : not found
    else {
        sendResponse(res, 404, {
            success: false,
            message: "Route not found"
        });
    }
};

module.exports = { routeHandler };