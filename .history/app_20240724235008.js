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
            // Filter products based on the category
            if (category.toLowerCase() === 'streetwear') {
                products = products.filter(product => {
                    const name = product.shoeName.toLowerCase();
                    return !name.includes('jordan') && (
                        name.includes('fear of god') ||
                        name.includes('bape') ||
                        name.includes('supreme') ||
                        name.includes('hoodie') ||
                        name.includes('t-shirt') ||
                        name.includes('fleece')
                    );
                });
            } else if (category.toLowerCase() === 'sneakers') {
                products = products.filter(product => {
                    const name = product.shoeName.toLowerCase();
                    return !(
                        name.includes('fear of god') ||
                        name.includes('bape') ||
                        name.includes('supreme') ||
                        name.includes('hoodie') ||
                        name.includes('t-shirt') ||
                        name.includes('fleece')
                    ) && (
                        name.includes('sneaker') ||
                        name.includes('shoe') ||
                        name.includes('yeezy') ||
                        name.includes('jordan') ||
                        name.includes('nike') ||
                        name.includes('adidas')
                    );
                });
            }
            
            // Include image URL in the response
            const result = products.map(product => ({
                shoeName: product.shoeName,
                brand: product.brand,
                styleID: product.styleID,
                description: product.description,
                imageUrl: product.thumbnail,  // Assuming 'thumbnail' is the key for the image URL
            }));

            res.json(result);
        }
    });
});


const port = process.env.PORT || 4000;
app.listen(port, () => {
    console.log(`Sneaks app listening on port ${port}`);
});
