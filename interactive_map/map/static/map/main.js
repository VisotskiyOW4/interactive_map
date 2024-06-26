document.addEventListener('DOMContentLoaded', () => {
    const floorSelect = document.getElementById('floor-select');
    const floors = document.querySelectorAll('.floor-map');
    const roomNumberTitle = document.getElementById('room-number-title');

    // Показати перший поверх за замовчуванням
    if (floors.length > 0) {
        floors[0].style.display = 'block';
    }

    floorSelect.addEventListener('change', function() {
        const selectedFloor = this.value;

        floors.forEach(floor => {
            floor.style.display = 'none';
        });

        const floorToShow = document.getElementById('floor-' + selectedFloor);
        if (floorToShow) {
            floorToShow.style.display = 'block';
        }
    });

    const rooms = document.querySelectorAll('.room');
    rooms.forEach(room => {
        room.addEventListener('click', function() {
            const roomNumber = this.getAttribute('data-room');
            roomNumberTitle.textContent = roomNumber; // Оновлення заголовка таблиці
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
