document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('updateStatusForm');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        const orderId = document.getElementById('order_id').value;
        const status = document.getElementById('status').value;

        try {
            const response = await fetch('/update_order_status', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    order_id: orderId,
                    status: status
                }),
            });

            const data = await response.json();

            if (response.ok) {
                alert('Order status updated successfully!');
            } else {
                alert('Error updating order status: ' + data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while updating the order status.');
        }
    });
});
