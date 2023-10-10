/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    let total = functions.length
    let resolved = 0
    let sol = new Array(total)
    const promise = new Promise((res,rej)=>{
        for(let i=0;i<total;i++){
            functions[i]().then(val=>{
                sol[i]=val;
                resolved++;
                if(resolved === total){
                    res(sol);
                }
            }).catch(err=>{
                rej(err)
            })
        }
    })
    return promise
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */