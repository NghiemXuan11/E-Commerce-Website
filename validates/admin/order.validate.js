

//validate info order 
module.exports.infoUser = (req,res,next) => {
    console.log(req.body.fullName)
    console.log(req.body.phone)

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

    const num = /[qwertyuioasdfghjklzxcvbnma!@#$%^&*()\[\]_+{}\|; :'"?.>,<\/-]/;
    if(num.test(req.body.phone)){
        req.flash("error", "Số điện thoại không hợp lệ")
        res.redirect("back");
        return;
    }

    if(req.body.phone.length < 10 || req.body.phone.length > 11){
        req.flash("error", "Số điện thoại phải chứa từ 10 hoặc 11 số")
        res.redirect("back");
        return;
    }

    next();
}