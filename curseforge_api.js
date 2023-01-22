const {Curseforge} = require("node-curseforge");

let cf = new Curseforge(process.env.CURSEFORGE_API_KEY);

args = process.argv.slice(2);

if (args[0] === "search" || args[0] === "bigsearch") {
    options = {
        "pageSize": 50,
        "sortField": 2,
        "sortOrder": "desc",
    };
    if (args.length >= 2) {
        options["searchFilter"] = args[1];
    }
    if (args.length >= 3) {
        options["gameVersion"] = args[2];
    }
    if (args.length >= 4) {
        options["modLoaderType"] = args[3];
    }
    if (args.length >= 5) {
        throw "invalid extra arguments to search: " + args.slice(4);
    }
    cf.get_game("minecraft").then((mc) => {
        cf.search_mods(mc, options).then((mods) => {
            console.log(JSON.stringify(mods));
        }).catch((err) => {
            console.error(err);
        });
    }).catch((err) => {
        console.error(err);
    })
} else if (args[0] === "getfiles") {
    if (args.length >= 3) {
        throw "invalid extra arguments to getfiles: " + args.slice(2);
    }
    cf.get_files(parseInt(args[1])).then((files) => {
        console.log(JSON.stringify(files));
    }).catch((err) => {
        console.error(err);
    });
} else {
    throw "Unknown arg: " + args[0];
}
