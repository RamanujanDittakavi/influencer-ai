
const API="https://your-backend-url.onrender.com"

function loadInfluencers(){

fetch(API+"/influencers")
.then(res=>res.json())
.then(data=>{

let table=document.getElementById("table")

data.forEach(user=>{

let row=table.insertRow()

row.insertCell(0).innerHTML=user.name
row.insertCell(1).innerHTML=user.followers
row.insertCell(2).innerHTML=user.score

})

})

}

function runCampaign(){

let product=document.getElementById("product").value

fetch(API+"/campaign",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({product:product})

})
.then(res=>res.json())
.then(data=>{

document.getElementById("result").innerHTML=
"Product: "+data.product+"<br>Expected Reach: "+data.reach

})

}
