const pagination = require("../../../helpers/pagination.helper")

describe('pagination function', () => {
    test('pagination with default values', () => {
        const result = pagination(10, {}, 100);
        expect(result.currentPage).toBe(1);
        expect(result.limitItem).toBe(10);
        expect(result.skip).toBe(0);
        expect(result.totalPage).toBe(10);
    });

    test('pagination with specified page' , () => {
        const result = pagination(10, {page: '3'}, 100);
        expect(result.currentPage).toBe(3);
        expect(result.limitItem).toBe(10);
        expect(result.skip).toBe(20);
        expect(result.totalPage).toBe(10);
    });

    test('pagination with different limitItem and count' , () => {
        const result = pagination(5, {page: '2'}, 20);
        expect(result.currentPage).toBe(2);
        expect(result.limitItem).toBe(5);
        expect(result.skip).toBe(5);
        expect(result.totalPage).toBe(4);
    });
    
    test('pagination with limitItems of 0', () => {
        const result = pagination(0, {}, 100);
        expect(result.currentPage).toBe(1);
        expect(result.limitItem).toBe(0);
        expect(result.skip).toBe(0);
        expect(result.totalPage).toBe(Infinity);
      });
})