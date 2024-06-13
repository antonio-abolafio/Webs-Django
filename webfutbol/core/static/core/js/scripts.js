document.addEventListener('DOMContentLoaded', function() {
    // Filtrar por posición
    const checkboxes = document.querySelectorAll('.filter-section input[type="checkbox"]');
    const playersGrid = document.getElementById('playersGrid');
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterPlayers);
    });

    function filterPlayers() {
        const selectedPositions = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.labels[0].textContent);

        const playerCards = playersGrid.querySelectorAll('.player-card');
        playerCards.forEach(card => {
            const position = card.getAttribute('data-position');
            if (selectedPositions.length === 0 || selectedPositions.includes(position)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Ordenar jugadores
    const sortOrder = document.getElementById('sortOrder');
    sortOrder.addEventListener('change', sortPlayers);

    function sortPlayers() {
        const order = sortOrder.value;
        const playerCards = Array.from(playersGrid.querySelectorAll('.player-card'));
        playerCards.sort((a, b) => {
            if (order === 'name') {
                return a.getAttribute('data-name').localeCompare(b.getAttribute('data-name'));
            } else {
                return parseInt(a.getAttribute('data-number')) - parseInt(b.getAttribute('data-number'));
            }
        });

        playerCards.forEach(card => playersGrid.appendChild(card));
    }

     // Filtrar por fecha y oponente
    const filterDate = document.getElementById('filterDate');
    const filterOpponent = document.getElementById('filterOpponent');
    const matchesGrid = document.getElementById('matchesGrid');

    filterDate.addEventListener('input', filterMatches);
    filterOpponent.addEventListener('input', filterMatches);

    function filterMatches() {
        const dateValue = filterDate.value;
        const opponentValue = filterOpponent.value.toLowerCase();
        const matchCards = matchesGrid.querySelectorAll('.match-card');

        matchCards.forEach(card => {
            const date = card.getAttribute('data-date');
            const opponent = card.getAttribute('data-opponent').toLowerCase();

            if ((dateValue === '' || date === dateValue) && (opponentValue === '' || opponent.includes(opponentValue))) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Ordenar partidos
    const sortOrder = document.getElementById('sortOrder');
    sortOrder.addEventListener('change', sortMatches);

    function sortMatches() {
        const order = sortOrder.value;
        const matchCards = Array.from(matchesGrid.querySelectorAll('.match-card'));
        matchCards.sort((a, b) => {
            if (order === 'date') {
                return new Date(a.getAttribute('data-date')) - new Date(b.getAttribute('data-date'));
            } else {
                return a.getAttribute('data-result').localeCompare(b.getAttribute('data-result'));
            }
        });

        matchCards.forEach(card => matchesGrid.appendChild(card));
    }
});
