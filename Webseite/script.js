// Hole die Formularreferenz und die Message-Div
const form = document.getElementById('form-entry');
const messageDiv = document.getElementById('message');

// Event Listener für das Absenden des Formulars
form.addEventListener('submit', async function(event) {
    event.preventDefault(); // Verhindert erneutes Laden der Seite

    // Datensammlung aus dem Formular
    const data = {
        type: form.type.value,
        date: form.date.value,
        title: form.title.value,
        details: form.details.value
    };

    // Optionale Validierung
    if (!data.type || !data.date || !data.title || !data.details) {
        messageDiv.textContent = 'Bitte alle Felder ausfüllen.';
        messageDiv.style.color = 'red';
        return;
    }

    try {
        // Hier Beispiel für das Senden an deine Python-API (URL anpassen!)
        const response = await fetch('http://localhost:5000/api/eintrag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            messageDiv.textContent = 'Eintrag erfolgreich übertragen!';
            messageDiv.style.color = 'green';
            form.reset();
        } else {
            messageDiv.textContent = 'Übertragung fehlgeschlagen. Versuche es später erneut.';
            messageDiv.style.color = 'red';
        }
    } catch(error) {
        messageDiv.textContent = 'Fehler bei der Verbindung zur API.';
        messageDiv.style.color = 'red';
    }
});
