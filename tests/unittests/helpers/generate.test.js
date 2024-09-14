const generateRandom = require('../../../helpers/generate.helper') 

describe('generateRandomNumber', () => {
    it('should generate a random number string of the specified length', () => {
      const length = 5; // Adjust as needed
      const randomNumber = generateRandom.generateRandomNumber(length);
      expect(randomNumber.length).toBe(length);
      // Check if the string contains only numeric characters
      expect(randomNumber).toMatch(/^\d+$/);
    });
    
    it('should return a string of specified length', () => {
        const length = 8;
        const result = generateRandom.generateRandomNumber(length);
        expect(result).toHaveLength(length);
        expect(typeof result).toBe('string');
    });
    
    it('should only contain numbers', () => {
        const length = 8;
        const result = generateRandom.generateRandomNumber(length);
        const numbers = "0123456789";
        for (let char of result) {
          expect(numbers).toContain(char);
        }
    });
    
    it('should return an empty string if length is 0', () => {
        const result = generateRandom.generateRandomNumber(0);
        expect(result).toHaveLength(0);
        expect(result).toBe('');
    });
    
    it('should return an empty string if length is negative', () => {
        const result = generateRandom.generateRandomNumber(-5);
        expect(result).toHaveLength(0);
        expect(result).toBe('');
    });

});

describe('generateRandomString', ()=>{
    it('Should generate a random String includes letter and numeric characters', () => {
        const length = 5;
        const randomString = generateRandom.generateRandomString(length);
        expect(randomString).not.toMatch(/^\d+$/);
    })
})  

