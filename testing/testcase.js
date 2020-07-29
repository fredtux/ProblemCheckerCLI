const rl = require('readline')
const readline = rl.createInterface({
    input: process.stdin,
    output: process.stdout
})

let a = 0
let b = []
let c = []

readline.question("", function(result){
    a = result
    readline.question("", function(result){
        b = result.split(" ")
        readline.question("", function(result){
            c = result.split(" ")
            readline.close()

            let out = ""
            for(let val of b){
                out += (parseInt(val) * a) + " "
            }
            out.trim()
            console.log(out)

            out = ""
            for(let val of c){
                out += (parseInt(val) * a) + " "
            }
            out.trim()
            console.log(out)
        })
    })
})