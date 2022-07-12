var addBtn = document.getElementsByClassName('add-cart')

for (var i = 0; i < addBtn.length; i++) {
    addBtn[i].addEventListener('click', function() {
        var productID = this.dataset.product
        var action = this.dataset.action

        if (user == 'AnonymousUser') {
            addCoolieItem(productID, action)
        } else {
            console.log("1")
            addItemOrder(productID, action)

        }
    })

}

function addItemOrder(productID, action) {

    var url = '/add_Item/'

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
            document.getElementById('add-butt').innerHTML = "Done"

        })
}