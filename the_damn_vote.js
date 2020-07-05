const open = require('open')
const cron = require('node-cron')
const ion = "https://top.gg/bot/449719890312691715/vote"
console.log("yep ive started")
// reference cron help : minute hours day-of-month month day-of-week
cron.schedule("5,15,17,30 10,11,23,16 * * *",()=>{
    console.log("started the cron job")
    open(ion).then(console.log("Its time to vote"))
})

