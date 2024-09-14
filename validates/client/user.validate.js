const schema = require("../../helpers/validation-schema.helper");

//validate register
module.exports.registerPost = (req, res ,next) => {
    if(!req.body.fullName) {
        req.flash("error","Họ tên không được để trống!");
        res.redirect("back");
        return;
    }

    const regex = /[0123456789!@#$%^&*()\[\]_+{}\|;:'"?.>,<\/-]/;
    if(regex.test(req.body.fullName)){
        req.flash("error","Họ tên không hợp lệ");
        res.redirect("back");
        return;
    }

    if(!req.body.email){
        req.flash("error","Email không được để trống!");
        res.redirect("back");
        return;
    }

    if(!schema.validate(req.body.password)){
        const inValid = schema.validate(req.body.password ,{ details: true });
        const errorMessage = inValid[0];
        req.flash("error", errorMessage.message);
        res.redirect("back");
        return;
    }

    next();
};

//validate login user account
module.exports.loginPost = (req, res, next) => {
    if(!req.body.email){
        req.flash("error", "Email không được để trống")
        res.redirect("back");
        return;
    }

    if(!req.body.password){
        req.flash("error", "Mật khẩu không được để trống")
        res.redirect("back");
        return;
    }

    next();
};

// validate user account forgot password
module.exports.forgotPasswordPost = (req, res, next) => {
    if(!req.body.email){
        req.flash("error", "Email không được để trống!")
        res.redirect("back");
        return;
    }

    next();
}


//validate user account reset password
module.exports.resetPassowrdPost = (req, res, next) => {
    if(!schema.validate(req.body.password)){
        const inValid = schema.validate(req.body.password ,{ details: true });
        const errorMessage = inValid[0];
        req.flash("error", "password: " + errorMessage.message);
        res.redirect("back");
        return;
    }
    if(!schema.validate(req.body.confirmPassword)){
        const inValid = schema.validate(req.body.confirmPassword ,{ details: true });
        const errorMessage = inValid[0];
        req.flash("error", "confirm Password: " + errorMessage.message);
        res.redirect("back");
        return;
    }
    if(req.body.password !== req.body.confirmPassword){
        req.flash("error","Xác nhận mật khẩu không khớp với mật khẩu trên!")
        res.redirect("back");
        return;
    }

    next();
}

//validate info order 
module.exports.infoUser = (req,res,next) => {
    if(!req.body.fullName) {
        req.flash("error","Họ tên không được để trống!");
        res.redirect("back");
        return;
    }

    const regex = /[0123456789!@#$%^&*()\[\]_+{}\|;:'"?.>,<\/-]/;
    if(regex.test(req.body.fullName)){
        req.flash("error","Họ tên không hợp lệ");
        res.redirect("back");
        return;
    }

    if(req.body.phone.length < 10 || req.body.phone.length > 11){
        req.flash("error", "Số điện thoại phải chứa từ 10 hoặc 11 số")
        res.redirect("back");
        return;
    }

    const num = /[qwertyuioasdfghjklzxcvbnma!@#$%^&*()\[\]_+{}\|;:'"?.>,<\/-]/;
    if(num.test(req.body.phone)){
        req.flash("error", "Số điện thoại không hợp lệ")
        res.redirect("back");
        return;
    }

    next();
}