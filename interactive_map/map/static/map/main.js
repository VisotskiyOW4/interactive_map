document.addEventListener('DOMContentLoaded', () => {
    const rooms = document.querySelectorAll('.room');
    rooms.forEach(room => {
        room.addEventListener('click', function() {
            const roomNumber = this.getAttribute('data-room');
            fetch(`/get_room_items/${roomNumber}/`)
                .then(response => response.json())
                .then(data => {
                    const tableBody = document.querySelector('#items-table tbody');
                    tableBody.innerHTML = ''; // Clear existing rows
                    data.items.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${item.item_number}</td>
                            <td>${item.item_name}</td>
                            <td>${item.specification}</td>
                            <td>${item.category_name}</td>
                        `;
                        tableBody.appendChild(row);
                    });
                });
        });
    });
});
wd