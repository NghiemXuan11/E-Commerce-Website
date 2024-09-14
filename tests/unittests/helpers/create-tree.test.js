const createTree = require('../../../helpers/create-tree.helper');

describe('createTree function', () => {
  it('should create a tree structure from array of objects', () => {
    const arr = [
      { id: '1', parent_id: '' },
      { id: '2', parent_id: '1' },
      { id: '3', parent_id: '1' },
      { id: '4', parent_id: '2' },
      { id: '5', parent_id: '3' }
    ];

    const expectedTree = [
      { id: '1', parent_id: '', children: [
        { id: '2', parent_id: '1', children: [
          { id: '4', parent_id: '2' }
        ] },
        { id: '3', parent_id: '1', children: [
          { id: '5', parent_id: '3' }
        ] }
      ] }
    ];

    const result = createTree(arr);
    expect(result).toEqual(expectedTree);
  });

  it('should return an empty array if input array is empty', () => {
    const arr = [];
    const result = createTree(arr);
    expect(result).toEqual([]);
  });

  it('should handle circular references gracefully', () => {
    const arr = [
      { id: '1', parent_id: '' },
      { id: '2', parent_id: '3'},
      { id: '3', parent_id: '' },
      { id: '4', parent_id: '1'},
    ];

    const result = createTree(arr);
    expect(result).toHaveLength(2);
    expect(result[0].id).toBe('1');
    expect(result[1].id).toBe('3');
  });
});