#!/home/erkan/.nvm/versions/node/v19.2.0/bin/ts-node
import { readFileSync } from "fs";
import { join } from "path";







const tick = (clock: number, X:number, sum:number, CRT: string[][]) =>{
    let x = Math.floor(clock/40)
    let y = clock%40;
    
    (clock%40)+1-X >= 0 && (clock%40)+1-X <=2 ? CRT[x][y] = "#" : null
    
    clock++
    if((clock - 20) % 40 === 0){
        const mult = X*clock
        sum += mult
    } 

    return [clock, X, sum]
}


const execute = (commands: string[]) => {
    let clock = 0
    let X = 1
    let sum = 0
    
    const CRT: string[][] = Array(6).fill(".").map(() => Array(40).fill("."))

    commands.forEach((command) => {
        const cmds = command.split(" ");
        
        [clock, X, sum] = tick(clock, X, sum, CRT)
        if (cmds[0] === "addx"){
            [clock, X, sum] = tick(clock, X, sum, CRT)
            X += +cmds[1]
        }
    })


    CRT.forEach((row) => console.log(row.reduce((prev, curr) => prev+curr)))
    
    
    return sum
}




const file = readFileSync(join(__dirname, "/input.csv"), "utf-8").trim()
const commands = file.split("\n")


const sum = execute(commands)
console.log(sum);


