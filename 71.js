var simplifyPath = function (path) {
    let simplePath = []
    let str = ""

    for (i = 0; i < path.length; i++) {
        if (path[i] === "/") {
            if (str == "..") {
                simplePath.pop()
                str = ""
            } else if (str == ".") {
                str = ""
                continue;
            } else {
                if (str != "") simplePath.push(str);
                str = ""
            }
        } else {
            str += path[i];
        }
    }

    if (str == "..") {
        simplePath.pop()
    } else {
        if (str != "" && str != ".") simplePath.push(str);
    }
    return ("/" + simplePath.join("/"))

};