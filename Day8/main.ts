#!/home/erkan/.nvm/versions/node/v19.2.0/bin/ts-node
import {readFileSync} from "fs";
import { join } from "path";



const visibleTree = (tree: number,trees: number[][], row: number, col: number) => {

    const scores: number[] = new Array(4).fill(0)
    const flags: boolean[] = new Array(4).fill(true)
    for (let r = row-1; r >= 0; r--){
        scores[0]++
        const adjTree = trees[r][col] 
        if (adjTree >= tree){
            flags[0] = false
            break
        }
    }
   
    for (let r = row+1; r < trees.length; r++){
        scores[1]++
        const adjTree = trees[r][col] 
        if (adjTree >= tree){
            flags[1] = false
            break
        }
    }
   
    for (let c = col-1; c >= 0; c--){
        scores[2]++
        const adjTree = trees[row][c] 
        if (adjTree >= tree){
            flags[2] = false
            break
        }
    }
   
    for (let c = col+1; c < trees.length; c++){
        scores[3]++
        const adjTree = trees[row][c] 
        if (adjTree >= tree){
            flags[3] = false
            break
        }
    }

    const flag = flags.includes(true)
    const score = scores.reduce((prod, current) => prod*current)
    return {flag, score}
}


const fillMap = (file: string) => {
    const arr = file.split("\n")
    arr.pop()
    const trees = arr.map((row) => new Array(1).fill([...row]).flat().map(Number))
    
    return trees
}


const visibleTrees = (file:string) => {
    let nVisible = 0
    let highScore = 0

    const trees = fillMap(file)

    for (let row = 0; row < trees.length; row++){
        for (let col = 0; col < trees[0].length; col++){
            if (row === 0 || row === trees.length-1 || col === 0 || col === trees[0].length){
                nVisible++
                continue
            }
            const tree = trees[row][col]
            const {flag, score} = visibleTree(tree, trees, row, col)
            if (flag){
                nVisible++
                // console.log(`[${row}][${col}]`);
                highScore =  Math.max(score, highScore)
                
            }
            // tallestTree(tree, trees, row, col) ? nVisible++ : null
        }
    }

    return {nVisible, highScore}

}




const file = readFileSync(join(__dirname,"/input.csv"), "utf-8")
const {nVisible, highScore} = visibleTrees(file)
console.log(nVisible);
console.log(highScore);







