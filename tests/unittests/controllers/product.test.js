const controller = require("../../../controllers/admin/product.controllers.js")

jest.mock("../../../models/product.model.js")
const Product = require("../../../models/product.model.js");


describe('changeStatus function', () => {
  test('updates product status and redirects back with success flash message', async () => {
    // Mock request and response objects
    const req = {
      params: { id: 'product_id', status: 'new_status' },
      flash: jest.fn(),
      redirect: jest.fn()
    };
    const res = { redirect: jest.fn() };

    // Mock Product.updateOne method
    Product.updateOne = jest.fn().mockResolvedValue({});

    // Call the controller function
    await controller.changeStatus(req, res);

    // Verify that Product.updateOne was called with the correct parameters
    expect(Product.updateOne).toHaveBeenCalledWith(
      { _id: req.params.id },
      { status: req.params.status }
    );

    // Verify that req.flash was called with the success message
    expect(req.flash).toHaveBeenCalledWith('Success', 'Cập nhật trạng thái thành công!');

    // Verify that res.redirect was called to redirect back
    expect(res.redirect).toHaveBeenCalledWith('back');
  });

  // Add more test cases to cover other scenarios...
});
describe('deleteItem function', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('should update deleted to true for given ids', async () => {        
        const req = {
            params: { id: 'product_id', status: 'new_status' },
            flash: jest.fn(),
            redirect: jest.fn()
        };
        const res = { redirect: jest.fn() };
        Product.updateOne = jest.fn().mockResolvedValue({});
        await controller.deleteItem(req, res);
        expect(Product.updateOne).toHaveBeenCalledWith(
            { _id: req.params.id },
            { deleted: true, deletedAt: new Date() }
        );
        // Verify that req.flash was called with the success message
        expect(req.flash).toHaveBeenCalledWith('Success','Xóa sản phẩm thành công!');

        // Verify that res.redirect was called to redirect back
        expect(res.redirect).toHaveBeenCalledWith('back');
    });

    test('should update new create', async() => {
      
    })
});
