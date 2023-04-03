const express = require("express")
const app = express()
const mongoose = require("mongoose") 
const routes = require("./routes") 
const { Sequelize, DataTypes } = require("sequelize");

const sequelize = new Sequelize(
    'db',
    'root',
    'password',
     {
       host: 'localhost',
       dialect: 'mariadb'
     }
   );


console.log("test")
sequelize.authenticate().then(() => {
    console.log('Connection has been established successfully.');
 }).catch((error) => {
    console.error('Unable to connect to the database: ', error);
 });



 const User = sequelize.define("loyalty_users", {
    loyalty_id: {
      type: DataTypes.STRING
    },
    first_name: {
      type: DataTypes.STRING
    },
    last_name: {
      type: DataTypes.STRING,
    },
    loyalty_points: {
      type: DataTypes.INTEGER,
    },
    phone_number: {
      type: DataTypes.STRING,
    },
    email: {
      type: DataTypes.STRING,
    }
 });

 User.sequelize.sync();




mongoose
	.connect("mongodb+srv://alannahhenry1999:Mongopassword@cluster0.4ix8qcd.mongodb.net/?retryWrites=true&w=majority", { useNewUrlParser: true })
	.then(() => {
		const app = express()
        app.use(express.json())
		app.use("/api", routes) // new
        app.get('/api/users',async (req, res) => {
            User.findAll().then(data => {
                res.send(data)
            }).catch(err =>{
                console.log(err)
            })
        })
        app.post('/api/users',async (req, res) => {
            const thisUser = {
                loyalty_id:req.body.loyalty_id,
                first_name:req.body.first_name,
                last_name:req.body.last_name,
                loyalty_points:req.body.loyalty_points,
                phone_number:req.body.phone_number,
                email:req.body.email
            }
            User.create(thisUser).then(user =>
                res.send(user)
            ).catch(err=>{
                console.log(err.message)
            })
        })
        app.put('/api/users',async (req, res) => {
           
            User.update(req.body, {
              where: { id: req.body.id }
            })
              .then(num => {
                if (num == 1) {
                  res.send({
                    message: " updated successfully."
                  });
                } else {
                  res.send({
                    message: `Cannot update  with id=${id}.`
                  });
                }
              })
              .catch(err => {
                res.status(500).send({
                  message: "Error updating  with id=" + id
                });
              });
        })

		app.listen(5000, () => {
			console.log("Server has started!")
		})
	})