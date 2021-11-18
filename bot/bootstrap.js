function boot(){
    const fs = require("fs")

    let application = fs.readFileSync("./application.yml", "utf8")


    if (process.env.PORT) {
        application = application.replace("DYNAMICPORT", process.env.PORT)
    }

    if (process.env.PASS) {
        application = application.replace("youshallnotpass", process.env.PASS)
    }

    fs.writeFileSync("./application.yml", application)
}

boot()