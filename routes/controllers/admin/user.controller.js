const User = require("../../models/user.model")
const systemCongif = require("../../config/system")
const filterStatusHelper = require("../../helpers/filterState.helper");
const paginationHelper = require("../../helpers/pagination.helper")


//[GET] /admin/users
module.exports.index = async (req,res) => {
    const filterState = filterStatusHelper(req.query)
    
    const find = {
        deleted: false,
    };
    
    if(req.query.status){
        find.status = req.query.status;
    };

    //Search
    if(req.query.keyword){
        const regex = new RegExp(req.query.keyword, "i");
        find.fullName = regex;
        // reExp: "so khớp chuỗi , 'i' là so khớp không phân biệt hoa hay thường "
    }
    //End search

    //pagination
    const countUser = await User.countDocuments(find);
    const objectPagination = paginationHelper(4, req.query, countUser);
    //End pagination   

    const user = await User.find(find);

    res.render("admin/pages/users/index.pug", {
        pageTitle: "Danh sách tài khoản khách hàng",
        user: user,
        filterState: filterState,
        keyword: req.query.keyword,
        pagination: objectPagination,
    })
}

//[PATCH] /admin/users/change-status/status/id
module.exports.changeStatus = async (req,res) => {
    const id = req.params.id;
    const status = req.params.status;

    await User.updateOne({
        _id: id
    }, {
        status: status
    })
    req.flash("Success","Cập nhật trạng thái tài khoản thành công");
    res.redirect("back");
}

//[DELETE] /admin/users/delete/id
module.exports.deleteUser = async (req,res) =>{
    const id = req.params.id;
    try {
        await User.updateOne({
            _id: id
        }, {
            deleted: true
        })
        req.flash("Success","Xoá tài khoản thành công");
    } catch (error) {
        console.log(error);
    }
    res.redirect("back");    
}
