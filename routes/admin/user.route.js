const express = require("express");
const router = express.Router();

controller = require("../../controllers/admin/user.controller")

router.get("/", controller.index)
router.patch("/change-status/:status/:id", controller.changeStatus)
router.delete("/delete/:id", controller.deleteUser)

module.exports = router;