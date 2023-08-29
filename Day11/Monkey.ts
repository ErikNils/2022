interface MonkeyInterface{
    id: number
    items: string[]
    nInspections: number
    test(worry: string, mod: number): [number, number]
}

export class Monkey implements MonkeyInterface{
    id: number;
    items: string[];
    nInspections: number
    test: (worry: string, mod: number)=> [number, number]

    constructor(
        id: number, 
        items: string[],
        nInspections: number,
        test: (worry: string, mod: number) => [number, number]
        ){
            
        this.id = id
        this.items = items
        this.nInspections = nInspections
        this.test = test
    }
    
}
