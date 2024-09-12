
const status_va = document.querySelectorAll(".order-status");

status_va.forEach(function(status_element) {
    const status_content = status_element.textContent.replace('Status:', '').trim() 
    console.log(status_content)
    if (status_content === 'confirmed') {
        $(status_element).removeClass('pending').addClass('confirmed');
    } else if (status_content === 'pending') {
        $(status_element).removeClass('confirmed').addClass('pending');
    }


})

