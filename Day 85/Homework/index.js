function manualFilter(func, arr) {
    const result = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (func(arr[i])) {
            result.push(arr[i]);
        }
    }
    
    return result;
}