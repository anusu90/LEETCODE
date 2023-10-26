class EventEmitter {
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    
    store={}
    sol=[]
	subscribe(eventName, callback) {
        if(!(eventName in this.store)){
            this.store[eventName]={}
        }
        const cbName = (callback?.name ?? "") + Math.floor(Math.random() * 1e10)
        this.store[eventName] = {...this.store[eventName],[cbName]:callback}
      	
		return {
			unsubscribe: () => {
                if(this.store?.[eventName]?.[cbName]){
                    delete this.store[eventName][cbName]
                }
                
			}
		};
	}
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
	emit(eventName, args = []) {
        this.sol = []
        console.log(this.store)
        Object.values(this.store[eventName]??{}).forEach(cb=>{
                      this.sol.push(cb.apply(this,args))
                      })
                      return this.sol;
	}
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */