import express
from controllers.propertyController import createProperty, deleteProperty, fullyUpdateProperty, getAllProperty, getProperty, parttiallyUpdateProperty

propertyRouter = express.Router()
propertyRouter.route("/").get(getAllProperty).post(createProperty)
propertyRouter.route("/:id").get(getProperty).put(fullyUpdateProperty).patch(parttiallyUpdateProperty).delete(deleteProperty)

export

