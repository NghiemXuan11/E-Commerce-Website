const express = require('express');
const router = express.Router();

const validate = require("../../validates/admin/order.validate")
const controller = require("../../controllers/admin/order.controllers")


router.get("/", controller.index);
router.get("/detail/:orderId", controller.detail);
router.patch("/detail/:orderId", controller.detailPatch);
router.get("/edit/:orderId", controller.edit);
router.patch("/edit/:orderId", controller.editPatch);
module.exports = router;