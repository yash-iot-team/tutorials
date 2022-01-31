/* DEPENDENCIES */
const express = require('express');

/* MIDDLEWARES */
const app = express();

app.use('/test1/test2/test3/test4', (req,res, next)=>{
    console.log('Inside Route /test1/test2/test3/test4');
    next();
})


/* ROUTES & CONTROLLER */
app.get('/test1/test2/test3/test4', (req, res) => {
    console.log('Inside Get Method');
    // console.log(req);
/*     console.log('Headers :',req.headers);
    console.log('Params :',req.params);
    console.log('Query :',req.query);
    console.log('Routes :', req.route); */

    const mess = 'Hello World';
//   res.send('Hello World');
    res.json({message : mess, status: 'success'});
});

app.post('/test1/test2/test3/test4', (req, res) => {
    console.log('Inside Post Method1');
    // console.log(req);
/*     console.log('Headers :',req.headers);
    console.log('Params :',req.params);
    console.log('Query :',req.query);
    console.log('Routes :', req.route); */
  res.send('Hello World')
});

app.patch('/test1/test2/test3/test4', (req, res) => {
    console.log('Inside Patch Method');
    // console.log(req);
/*     console.log('Headers :',req.headers);
    console.log('Params :',req.params);
    console.log('Query :',req.query);
    console.log('Routes :', req.route); */
  res.send('Hello World')
});

app.delete('/test1/test2/test3/test4', (req, res) => {
    console.log('Inside Delete Method');
    // console.log(req);
/*     console.log('Headers :',req.headers);
    console.log('Params :',req.params);
    console.log('Query :',req.query);
    console.log('Routes :', req.route); */
  res.send('Hello World')
});

module.exports = app;