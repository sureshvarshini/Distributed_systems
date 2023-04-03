const express = require("express")
const router = express.Router()
const Transaction = require("./models/Transaction") 



router.post("/transactions", async (req, res) => {
    console.log(req.body)
	const post = new Transaction(req.body)
	await post.save()
	res.send(post)
})
router.get("/transactions/:id", async (req, res) => {
	try {
        const post = await Transaction.findOne({ _id: req.params.id })
	    res.send(post)
    }catch {
		res.status(404)
		res.send({ error: "Transaction doesn't exist!" })
	}
})

router.get("/transactions", async (req, res) => {
	const posts = await Transaction.find()
	res.send(posts)
})





module.exports = router