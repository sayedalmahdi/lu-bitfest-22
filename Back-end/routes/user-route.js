const express = require("express");
const user_controller = require("../controllers/user-controller");
const router = express.Router();
router.post("/add", user_controller.add_new_user);
module.exports = router;
