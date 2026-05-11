const express=require("express")

const app=express()


app.get("/",(req,res)=>{
    res.send("GET")
})



app.listen(3000,()=>{
    console.log("Serveur en écoute...")
})