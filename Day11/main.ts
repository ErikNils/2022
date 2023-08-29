#!/home/erkan/.nvm/versions/node/v19.2.0/bin/ts-node
import { readFileSync } from "fs";
import { join } from "path";
import {Monkey} from "./Monkey"



const initMonkeys = (monkeyParse: string[], divs: number[]) => {

    const monkeys = new Map<number, Monkey>()

    monkeyParse.forEach((monkeyStr) => {
      const monkeyArr = monkeyStr.split("\n")
      const id = +monkeyArr[0].split(":")[0]
      const items = monkeyArr[1].split(":")[1].split(",").map((item) => item.trim())
      const opString = monkeyArr[2].split("=")[1].trim().split(" ")
      divs.push(+monkeyArr[3].split(" ").at(-1)!)

      const test = (worry: string, mod: number): [number, number] => {
        const operation = [...opString]
        operation[0] = worry
        operation.at(-1)?.trim() === "old" ? operation[operation.length-1] = worry : null
        
        const div = monkeyArr[3].split(" ").at(-1)
        const newWorry = eval(operation.reduce((prev, curr) => prev+curr)) % mod

        const monkeyTrue =  monkeyArr[4].split(" ").at(-1)
        const monkeyFalse =  monkeyArr[5].split(" ").at(-1)
        const newMonkey = newWorry % +div! === 0 ? +monkeyTrue! : +monkeyFalse!
        return [newWorry, newMonkey]
      }

      const monkey = new Monkey(id, items, 0, test)
      monkeys.set(id, monkey)
      
    })

    return monkeys
}


const chase = (monkeys: Map<number, Monkey>, mod: number) => {
    monkeys.forEach((monkey) => {
        while (monkey.items.length > 0){
            const item = monkey.items.shift();
            if(!item){
                continue
            }
            let newWorry: number
            let newMonkey: number
            [newWorry, newMonkey] = monkey.test(item, mod)
            const monkey2 = monkeys.get(newMonkey)
            monkey2?.items.push(""+newWorry)
            monkey.nInspections++
            
        }
    })
}



const monkeyParse = readFileSync(join(__dirname, "/input.csv"), "utf-8").trim().split("Monkey")
monkeyParse.splice(0,1)

const divs: number[] = []

const monkeys = initMonkeys(monkeyParse, divs)

const mod = divs.reduce((prev, curr) => prev*curr)

for (let i = 0; i < 10000; i++){
    chase(monkeys, mod)
}

const result: number[] = []
monkeys.forEach(({nInspections}) => result.push(nInspections))
result.sort((a,b) => a-b)

console.log(result.pop()!*result.pop()!);







