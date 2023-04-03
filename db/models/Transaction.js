const mongoose = require("mongoose")

const schema = mongoose.Schema({
	date:{type: Date, default: Date.now},
    payment_type:String,
    amount:Number,
    loyalty_id:String,
})

module.exports = mongoose.model("Transaction", schema)