const curseforge = require("mc-curseforge-api");

args = process.argv.slice(2);

if (args[0] === "search" || args[0] === "bigsearch") {
    options = {}
    if (args.length >= 2) {
        options["searchFilter"] = args[1];
    }
    if (args.length >= 3) {
        options["gameVersion"] = args[2];
    }
    if (args.length >= 4) {
        throw "invalid extra arguments to search: " + args.slice(3);
    }
    if (args[0] === "bigsearch") {
        options["pageSize"] = 50;
    }
    curseforge.getMods(options).then((mods) => {
        console.log(JSON.stringify(mods));
    }).catch((err) => {
        console.error(err);
    });
} else if (args[0] === "getfiles") {
    if (args.length >= 3) {
        throw "invalid extra arguments to getfiles: " + args.slice(2);
    }
    curseforge.getModFiles(parseInt(args[1])).then((files) => {
        console.log(JSON.stringify(files));
    }).catch((err) => {
        console.error(err);
    });
} else {
    throw "Unknown arg: " + args[0];
}
