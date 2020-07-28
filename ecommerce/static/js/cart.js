let updateBtn = document.getElementsByClassName('update-cart');


for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click',function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('product : ', productId,', action : ',action)
        console.log(user)
    })
}