/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
	return async function(...args) {
        return new Promise(function(res,rej){
            const internalPromise = fn(...args)
            const timeout = setTimeout(()=>{
                rej("Time Limit Exceeded")
            },t)
            internalPromise.then(v=>{
                clearTimeout(timeout)
                res(v)}).catch(e=>{rej(e)})
        })
        // return new Promise(function(res,rej){
        //     const start = performance.now();
        //     const internalPromise  = fn(...args);
        //     const timeout = setTimeout(()=>{
        //         rej("Time Limit Exceeded")
        //     },t)
        //     internalPromise.then(val=>{
        //         clearTimeout(timeout)
        //         res(val)
        //     }).catch(err=>{
        //         rej(err)
        //     })
        // })
        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */