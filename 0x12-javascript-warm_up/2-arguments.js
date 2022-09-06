#!/usr/bin/node
import { argv } from 'node:process'
let myVar = 0
argv.forEach((val, index) => {
    myVar++
});
if(myVar == 0){
    console.log('No argument')
}else if (myVar == 1){
    console.log('Argument found')
}else{
    console.log('Arguments found')
}
