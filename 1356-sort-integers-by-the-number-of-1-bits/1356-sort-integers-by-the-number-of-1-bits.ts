function sortByBits(arr: number[]): number[] {
    
    function countOne(n:number){
        let count = 0;
        while(n>0){
            // console.log('count',count)
            count += n&1;
            n=n>>1;
        }
        return count;
    }
    const sol = arr.sort(function(a:number,b:number){
        // console.log(countOne(a),countOne(b))
            const ca = countOne(a)
            const cb = countOne(b)
            if (ca ==cb){
                return a-b;
            }else{
                return ca-cb
            }
        })
    return sol;
    };