var updateBtn = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function() {
        var productID = this.dataset.product
        var action = this.dataset.action

        if (user == 'AnonymousUser') {
            window.location.href = '/signup';
            // console.log("nono")
            // addCoolieItem(productID, action)

        } else {

            updateUserOrder(productID, action)

        }
    })

}


function addCoolieItem(productID, action) {
    console.log('not authenticated', productID, action)
    if (action == 'add') {
        if (cart[productID] == undefined) {
            cart[productID] = { 'quantity': 1 }
        } else {
            cart[productID]['quantity'] += 1
        }
    }
    if (action == 'remove') {
        cart[productID]['quantity'] -= 1

        if (cart[productID]['quantity'] <= 0) {
            delete cart[productID]
            console.log('remove')
        }

    }
    console.log(cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}


function updateUserOrder(productID, action) {

    var url = '/update_Item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productID': productID,
                'action': action,

            })
        })
        .then((resp) => {
            return resp.json()
        })
        .then((data) => {
            console.log(data)
            location.reload()
        })
}