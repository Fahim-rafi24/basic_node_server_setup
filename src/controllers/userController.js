const path = require('path');
const { readJSONFile, sendResponse } = require('../utils/handler');

require('dotenv').config();
const dataPath = path.join(__dirname, `../../data/${process.env.DATABASE}`);


// handle all users requests
const getUsers = async (req, res) => {
    try {
        const users = await readJSONFile(dataPath);
        sendResponse(res, 200, {
            success: true,
            message: "Users fetched successfully",
            data: users
        });
    } catch (error) {
        sendResponse(res, 500, {
            success: false,
            message: "Failed to fetch users",
            error: error.message
        });
    }
};

// handle each user data
const getSingleUser = async (req, res, id) => {
    try {
        const users = await readJSONFile(dataPath);
        const user = users.find(u => u.id === parseInt(id));
        
        if (user) {
            sendResponse(res, 200, {
                success: true,
                data: user
            });
        } else {
            sendResponse(res, 404, {
                success: false,
                message: "User not found"
            });
        }
    } catch (error) {
        sendResponse(res, 500, {
            success: false,
            message: "Internal Server Error"
        });
    }
};

module.exports = { getUsers, getSingleUser };