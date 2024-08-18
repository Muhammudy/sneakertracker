const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const SneaksAPI = require('sneaks-api');
const sneaks = new SneaksAPI();

// Enable CORS for all routes
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
    next();
});

app.use(bodyParser.json());

app.post('/get-sneaker-data', (req, res) => {
    const { category, info } = req.body;

    sneaks.getProducts(info, 10, function(err, products) {
        if (err) {
            console.error(err);
            res.status(500).send({ error: 'Failed to fetch data from API' });
        } else {
            if (category === 'streetwear') {
                products = products.filter(product => {
                    return !product.shoeName.toLowerCase().includes('sneaker') &&
                           !product.shoeName.toLowerCase().includes('shoe') &&
                           !product.shoeName.toLowerCase().includes('yeezy') &&
                           !product.shoeName.toLowerCase().includes('jordan') &&
                           !product.shoeName.toLowerCase().includes('nike') &&
                           !product.shoeName.toLowerCase().includes('adidas');
                });
            } else {
                products = products.filter(product => {
                    return product.shoeName.toLowerCase().includes('sneaker') ||
                           product.shoeName.toLowerCase().includes('shoe') ||
                           product.shoeName.toLowerCase().includes('yeezy') ||
                           product.shoeName.toLowerCase().includes('jordan') ||
                           product.shoeName.toLowerCase().includes('nike') ||
                           product.shoeName.toLowerCase().includes('adidas') ||
                           product.shoeName.toLowerCase().includes('hoodie') ||
                           product.shoeName.toLowerCase().includes('t-shirt') ||
                           product.shoeName.toLowerCase().includes('tee');
                });
            }
            
            // Add image URLs to the response
            const productsWithImages = products.map(product => ({
                shoeName: product.shoeName,
                brand: product.brand,
                styleID: product.styleID,
                description: product.description,
                imageUrl: product.thumbnail
            }));

            res.json(productsWithImages);
        }
    });
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
    console.log(`Sneaks app listening on port ${port}`);
});
