/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps  = function(num) {
        var n = 0;
        
        while (num != 0){
            if (num % 2 == 0)
                num /= 2;
            else
                num -= 1;
            
            n += 1;
        }
        return n;
};
