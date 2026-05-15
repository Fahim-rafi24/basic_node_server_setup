# Basic Node.js Server Setup

A clean, modular, and professional boilerplate for building RESTful APIs using **Raw Node.js** (without frameworks like Express). This project demonstrates how to handle routing, controllers, utilities, and JSON-based data storage in a structured manner.

---

## 🚀 Features

- **Raw Node.js Implementation:** Built using the native `http` module for a lightweight footprint.
- **Modular Architecture:** Clear separation of concerns with `routes`, `controllers`, and `utils`.
- **JSON Database:** Uses a local `.json` file for data persistence.
- **Environment Configuration:** Managed via `.env` files using the `dotenv` package.
- **CORS Support:** Pre-configured Cross-Origin Resource Sharing headers.
- **Mock Data Generation:** Includes a Python script to generate large sets of user data.
- **Development Mode:** Uses `nodemon` for automatic server restarts.

---

## 🛠️ Tech Stack

- **Runtime:** Node.js
- **Dependencies:** `dotenv`, `nodemon`
- **Data Source:** JSON (file-based)
- **Data Generator:** Python (Faker library compatible logic)

---

## 📂 Project Structure

```text
.
├── data/
│   └── users.json          # JSON storage for user data
├── generate_users_with_python/
│   └── generate_users.py   # Python script to generate mock users
├── src/
│   ├── controllers/
│   │   └── userController.js # Logic for user-related requests
│   ├── routes/
│   │   └── index.js        # Primary route handler
│   ├── utils/
│   │   └── handler.js      # Utility functions (File I/O, Responses)
│   └── server.js           # Entry point of the application
├── .env                    # Environment variables
├── .gitignore              # Git ignore rules
├── package.json            # Project dependencies and scripts
└── README.md               # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v14 or higher recommended)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)
- [Python](https://www.python.org/) (optional, for data generation)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Fahim-rafi24/basic_node_server_setup.git
   cd basic_node_server_setup
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   PORT=5000
   DATABASE=users.json
   ```

---

## 🏃 Running the Server

### Development Mode (with Nodemon)

```bash
npm run dev
```

### Production Mode

```bash
npm start
```

The server will start at `http://localhost:5000`.

---

## 📡 API Endpoints

| Method  | Endpoint        | Description                            |
| :------ | :-------------- | :------------------------------------- |
| **GET** | `/api/users`    | Fetch all users from the database      |
| **GET** | `/api/user/:id` | Fetch a single user by their unique ID |

---

## 🐍 Mock Data Generation

To generate new mock data for the `users.json` file, run the Python script provided:

```bash
cd generate_users_with_python
python generate_users.py
```

---

## 🛡️ License

This project is licensed under the **ISC License**. See the [package.json](package.json) for details.

---

## 👨‍💻 Author

Developed with ❤️ by **Fahim Rafi**.
