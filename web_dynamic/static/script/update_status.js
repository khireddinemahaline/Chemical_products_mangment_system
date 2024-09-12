document.getElementById('updateStatusForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const order_id = document.getElementById('order_id').value;
    const status = document.getElementById('status').value;

    fetch('/update_order_status', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            order_id: order_id,
            status: status
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error); // Handle success or error
    })
    .catch(error => {
        console.error('Error:', error);
    });
});