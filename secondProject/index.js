/* DEPENDENCIES */


/* MIDDLEWARES */

/* USER-DEFINED MIDDLEWARES */
const app = require('./app')

/* ENVIRONMENT */

/* DATABASE */

/* SERVER */
app.listen(3000, (req,res) => {
    console.log('Server running on http://localhost:3000')
});