const express = require("express")
const router = express.Router()
const controller = require("../../controllers/client/checkout.controller")
const validate = require("../../validates/client/user.validate")

router.get("/", controller.index);
router.post("/order", validate.infoUser, controller.order)
router.get("/success/:orderId", controller.success)

module.exports = router;