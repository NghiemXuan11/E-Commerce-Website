const Product = require("../../models/product.model")

module.exports.index = async (req,res) => {
    const keyword = req.query.keyword;
    
    let product = [];

    if(keyword){
        const keywordRegex = new RegExp(keyword, "i");
        product = await Product.find({
            title: keywordRegex,
            status: "active",
            deleted: false
        }).sort({ position: "desc" });
    }else{
        product = await Product.find({
            status: "active",
            deleted: false
        }).sort({ position: "desc" });
    }

    for (const item of product){
        item.priceNew = (item.price * (100 - item.discountPercentage)/100).toFixed(0);
    }  

    res.render("client/pages/search/index", {
        pageTitle: "Kết quả tìm kiếm",
        keyword: keyword,
        products: product
    });
}