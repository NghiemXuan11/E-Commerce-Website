const Order = require("../../models/order.model")
const Product = require("../../models/product.model")
const User = require("../../models/user.model")
const systemCongif = require("../../config/system")
const filterStatusHelper = require("../../helpers/filterState.helper");
const paginationHelper = require("../../helpers/pagination.helper")


//[GET] /admin/order/index
module.exports.index = async (req, res) => {
    const filterState = filterStatusHelper(req.query);
    
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
    const countOrder = await Order.countDocuments(find);
    const objectPagination = paginationHelper(4, req.query, countOrder);
    //End pagination

    const order = await Order.find(find);
    res.render("admin/pages/orders/index.pug", {
        pageTitle: "Danh sách đơn hàng",
        order: order,
        filterState: filterState,
        keyword: req.query.keyword,
        pagination: objectPagination,
    })
}

//[GET] /admin/order/detail/id
module.exports.detail = async (req,res) => {
    const id = req.params.orderId;
    try {
        const order = await Order.findOne({
            _id: id,
        });
    
        order.totalPrice = 0;
        
        for (const item of order.products){
            const infoProduct = await Product.findOne({
                _id: item.product_id
            });
            item.title = infoProduct.title;
            item.thumbnail = infoProduct.thumbnail;
            item.priceNew = (item.price * (100 - item.discountPercentage)/100).toFixed(0);
            item.totalPrice = item.priceNew * item.quantity;
            order.totalPrice += item.totalPrice;
        }
    
        res.render("admin/pages/orders/detail.pug", {
            pagetitle: "Chi tiết hoá đơn",
            order: order,
        })
    } catch (error) {
        req.flash("error", "Không thể xem hoá đơn đã thanh toán")
        res.redirect(`/${systemCongif.prefixAdmin}/order`)
    }
}

//[PATCH] /admin/order/detail/change-status/id
module.exports.detailPatch = async (req,res) => {
    const id = req.params.orderId;
    try {
        await Order.updateOne({
            _id: id,
            deleted: false,
            status: "active",
        },{
            status: "inactive",
        })
        req.flash('Success','Thanh toán hoá đơn thành công');
    } catch (error) {
        req.flash('Error','Thanh toán hoá đơn thất bại');
        console.log("error");
    } finally {
        res.redirect(`/${systemCongif.prefixAdmin}/order`);
    }
}

//[GET] /admin/order/edit/id
module.exports.edit = async (req,res) => {
    const id = req.params.orderId;
    const order = await Order.findOne({
        _id: id,
        status: "active",
        deleted: false,
    })

    res.render("admin/pages/orders/edit.pug",{
        pageTitle: "Chỉnh sửa hoá đơn",
        order: order
    })
}

//[PATCH] /admin/order/edit/id
module.exports.editPatch = async (req,res) => {
    const id = req.params.orderId;
    console.log(req.body.fullName);
    console.log(req.body.phone);
    console.log(id);
    req.flash("error","Hệ thống đang bảo trì")
    res.redirect("back")
}