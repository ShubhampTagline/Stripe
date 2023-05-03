console.log("HELLO")

fetch("/config/")
.then((result) => {return result.json();})
.then((data) => {const stripe = Stripe(data.public_key)});