 removeNullValues = (params, initial = {}) =>
        Object.keys(params).reduce(
            (acc, key) =>
                params[key] &&
                (Array.isArray(params[key]) ? params[key].length : true) &&
                (typeof params[key] === 'object'
                    ? Object.keys(params[key]).length
                    : true)
                    ? Object.assign(acc, {[`${key}`]: params[key]})
                    : acc,
            initial,
        );
    removeNullValuesRecursively = (
        params,
        cb = res1 => this.removeNullValues(res1),
    ) => {
        const res = Object.keys(params).reduce(
            (acc, key) =>
                params[key] &&
                (Array.isArray(params[key]) ? params[key].length : true)
                    ? typeof params[key] !== 'object'
                        ? Object.assign(acc, {[`${key}`]: params[key]})
                        : Object.assign(acc, {
                              [`${key}`]: this.removeNullValuesRecursively(
                                  params[key],
                              ),
                          })
                    : acc,
            {},
        );
        return cb(res);
    };
