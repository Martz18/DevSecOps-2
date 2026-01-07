const API_URL = "/quests"; 
let quetesEnSursis = [];

function ouvrirTaverne() {
    document.getElementById('page-entree').classList.remove('active');
    document.getElementById('page-taverne').classList.add('active');
    actualiserAffichage();
}

async function actualiserAffichage() {
    try {
        const response = await fetch(API_URL);
        const quests = await response.json();

        const zones = {
            "disponible": document.getElementById('available-quests'),
            "en cours": document.getElementById('in-progress-quests'),
            "terminée": document.getElementById('completed-quests')
        };

        Object.values(zones).forEach(z => z.innerHTML = "");

        const compteurs = { "disponible": 0, "en cours": 0, "terminée": 0 };
        const totalParZone = { "disponible": 0, "en cours : 0", "terminée": 0 };

        // Filtrage des quêtes terminées
        const quetesAAfficher = quests.filter(q => {
            if (q.status === "terminée") {
                return quetesEnSursis.includes(q.id);
            }
            return true;
        });

        // Comptage total par statut
        quetesAAfficher.forEach(q => {
            if (totalParZone.hasOwnProperty(q.status)) totalParZone[q.status]++;
        });

        // Affichage des cartes (limite de 3 par zone)
        quetesAAfficher.forEach(q => {
            if (compteurs[q.status] < 3) {
                const card = document.createElement('div');
                card.className = `quest-card ${q.status === 'terminée' ? 'just-finished' : ''}`;
                
                card.innerHTML = `
                    <h3>${q.name}</h3>
                    <p>${q.description}</p>
                    <div class="card-footer">
                        <strong>💰 ${q.reward} or</strong>
                        ${q.status !== 'terminée' ? 
                            `<button onclick="passerEtape(${q.id})">OK</button>` : 
                            `<span class="status-done">✨ TERMINÉ</span>`}
                    </div>
                `;
                zones[q.status].appendChild(card);
                compteurs[q.status]++;
            }
        });

        // Badges d'attente
        Object.keys(zones).forEach(status => {
            const reste = totalParZone[status] - 3;
            if (reste > 0) {
                const badge = document.createElement('div');
                badge.className = 'plus-badge';
                badge.innerText = `+ ${reste} contrat(s) en attente...`;
                zones[status].appendChild(badge);
            }
        });
    } catch (e) {
        console.error("Erreur API :", e);
    }
}

async function passerEtape(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: 'PUT' });
        const queteMiseAJour = await response.json();

        if (queteMiseAJour.status === "terminée") {
            quetesEnSursis.push(id);
            // On attend 15 secondes (durée de ton animation CSS) avant de supprimer
            setTimeout(() => {
                quetesEnSursis = quetesEnSursis.filter(qid => qid !== id);
                actualiserAffichage();
            }, 15000); 
        }
        actualiserAffichage();
    } catch (e) {
        alert("Erreur lors de la mise à jour");
    }
}