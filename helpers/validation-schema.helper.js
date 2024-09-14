const passwordValidator = require('password-validator');
const schema = new passwordValidator()

schema
.is().min(8,"Độ dài mật khẩu tối thiểu phải 8 ký tự")                                   
.is().max(100, "Độ dài mật khẩu không được quá 100 ký tự")                                 
.has().uppercase(1, "Phải có ít nhất 1 chữ viết hoa")                             
.has().lowercase(1, "Phải có ít nhất 1 chữ viết thường")                             
.has().digits(2, "Phải có ít nhất 2 chữ số")                                
.has().not().spaces(0,"Không được có khoảng trắng")

module.exports = schema;