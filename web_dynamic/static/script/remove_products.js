function deleteProduct(event) {
    event.preventDefault();
    const productId = document.getElementById('product_id').value;

    fetch(`/products/${productId}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            alert('Product deleted successfully');
        } else {
            alert('Error deleting product');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}