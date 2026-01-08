const API_URL = "http://localhost:5678/quests";
// Liste pour stocker les IDs des quêtes qui viennent d'être terminées
let quetesEnSursis = [];

function ouvrirTaverne() {
    document.getElementById('page-entree').classList.remove('active');
    document.getElementById('page-taverne').classList.add('active');
    actualiserAffichage();
}

function ouvrirPost() {
    document.getElementById('page-taverne').classList.remove('active');
    document.getElementById('page-post').classList.add('active');
    actualiserAffichage();
}

function ouvrirTaverne2() {
    document.getElementById('page-post').classList.remove('active');
    document.getElementById('page-taverne').classList.add('active');
    actualiserAffichage();
}

async function ajouterNouvelleQuete() {
    const name = document.getElementById('quest-name').value;
    const description = document.getElementById('quest-desc').value;
    const reward = document.getElementById('quest-reward').value;

    if (!name || !description) return alert("Remplissez tous les champs !");

    const nouvelleQuete = {
        name: name,
        description: description,
        reward: parseInt(reward),
        status: "disponible"
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nouvelleQuete)
        });

        if (response.ok) {
            // Vider les champs
            document.getElementById('quest-name').value = "";
            document.getElementById('quest-desc').value = "";
            // Retourner à la taverne et rafraîchir
            ouvrirTaverne2();
        }
    } catch (e) {
        console.error("Erreur lors de l'ajout :", e);
    }
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

        // On vide les colonnes
        Object.values(zones).forEach(z => z.innerHTML = "");

        const compteurs = { "disponible": 0, "en cours": 0, "terminée": 0 };
        const totalParZone = { "disponible": 0, "en cours": 0, "terminée": 0 };

        // Filtrage : On n'affiche dans "terminée" que celles qui sont dans la liste des 15 secondes
        const quetesAAfficher = quests.filter(q => {
            if (q.status === "terminée") {
                return quetesEnSursis.includes(q.id);
            }
            return true;
        });

        // Calcul des totaux pour les badges
        quetesAAfficher.forEach(q => totalParZone[q.status]++);

        // Création des cartes
        quetesAAfficher.forEach(q => {
            if (compteurs[q.status] < 3) {
                const card = document.createElement('div');
                // Ajout d'une classe spéciale pour les quêtes terminées
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

        // Ajout des badges si plus de 3 quêtes
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

        // Si la quête passe en "terminée", on lance le compte à rebours de 15s
        if (queteMiseAJour.status === "terminée") {
            quetesEnSursis.push(id);
            setTimeout(() => {
                quetesEnSursis = quetesEnSursis.filter(qid => qid !== id);
                actualiserAffichage();
            }, 5000); 
        }
        actualiserAffichage();
    } catch (e) {
        alert("Erreur lors de la mise à jour");
    }
}