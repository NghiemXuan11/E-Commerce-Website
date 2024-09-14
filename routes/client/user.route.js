const express = require("express")
const router = express.Router()
const controller = require("../../controllers/client/user.controller.js")


const validate = require("../../validates/client/user.validate.js")
const authMiddleware = require("../../middlewares/client/auth.middleware.js")

//Register
router.get("/register", controller.register)
router.post("/register", validate.registerPost, controller.registerPost)
//End register

//Login
router.get("/login",controller.login)
router.post("/login", validate.loginPost, controller.loginPost)
router.get("/logout",  controller.logout)
//End login

//Password forgot
router.get("/password/forgot", controller.forgotPassword)
router.post("/password/forgot", validate.forgotPasswordPost, controller.forgotPasswordPost)
router.get("/password/otp", controller.otpPassword)
router.post("/password/otp", controller.otpPasswordPost)
router.get("/password/reset", controller.resetPassword)
router.post("/password/reset", validate.resetPassowrdPost, controller.resetPasswordPost)
router.get("/info", authMiddleware.requireAuth, controller.info)
//End password forgot

// Order
router.delete("/delete/:orderId", authMiddleware.requireAuth, controller.cancelOrder)
router.get("/detail/:orderId", authMiddleware.requireAuth, controller.detailOrder)
// End order
module.exports = router;