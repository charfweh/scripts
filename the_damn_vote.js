const open = require('open')
const cron = require('node-cron')
const ion = "https://top.gg/bot/449719890312691715/vote"
console.log("Script is up")
open(ion).then(()=>{
 let dateobj = new Date()
 console.log("Its time to vote")
 console.log(dateobj.getHours())
}).catch((e)=>{
  console.log(e)
})
