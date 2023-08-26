#!/home/erkan/.nvm/versions/node/v19.2.0/bin/ts-node
import { readFileSync } from "fs";
import { join } from "path";


const moveTail = (head: [number, number], tail: [number, number]) => {
    const dX = head[0]-tail[0]
    const dY = head[1]-tail[1]

    if ((Math.abs(dX) > 1 && Math.abs(dY) == 1) || (Math.abs(dX) == 1 && Math.abs(dY) > 1)){
        dX > 0 ? tail[0]++ : tail[0]--
        dY > 0 ? tail[1]++ : tail[1]--
    }
    else{

        Math.abs(dX) > 1 ? tail[0] += dX/2 : null
        Math.abs(dY) > 1 ? tail[1] += dY/2 : null
    }
}




const moveHead = (commands: string[]): number => {
    const visitedNodes: Set<string> = new Set<string>() 
    visitedNodes.add("0,0")

    const knots: [number, number][] = [...Array(10)].map(() => [0,0])

    commands.forEach((cmd) => {
        const cmdArr = cmd.split(" ")
        const dir = cmdArr[0]
        const steps = cmdArr[1]
        for (let i = 0; i < +steps; i++){
            dir === "R" ? knots[0][1]++ : null
            dir === "L" ? knots[0][1]-- : null
            dir === "D" ? knots[0][0]++ : null
            dir === "U" ? knots[0][0]-- : null

            for (let j = 0; j < knots.length-1; j++){
                moveTail(knots[j], knots[j+1])
            }
            const strTail = knots[9].map((value) => ""+value).reduce((prev, current) => prev+","+current)
            
            visitedNodes.add(strTail)
        }
    })
    
    return visitedNodes.size
}



const file = readFileSync(join(__dirname,"/input.csv"), "utf-8")
const commands = file.trim().split("\n")

const nVisits = moveHead(commands)

console.log(nVisits);

